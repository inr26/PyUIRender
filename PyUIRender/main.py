import sys
import os
from PySide6.QtWidgets import (
    QFileDialog, QApplication, QMainWindow, 
    QLabel, QVBoxLayout, QDialog, QMessageBox)
from PySide6.QtCore import QTimer, QSettings
from PySide6.QtGui import QIcon
from appWindow import Ui_AppMainWindow
from success_dia import Ui_success_dialog
from failed_dia import Ui_fail_dialog
from PyUIRender import resources_rc

class SuccessDialog(QDialog):
    """Wrapper for the success dialog"""
    def __init__(self, parent=None, output_dir="", converted_files=None):
        super().__init__(parent)
        self.ui = Ui_success_dialog()
        self.ui.setupUi(self)
        
        # Set output directory in the text field
        self.ui.saved_file_path.setPlainText(str(output_dir))  # Convert to string
        
        # Connect copy button
        self.ui.copy_path_btn.clicked.connect(self.copy_path)
    
    def copy_path(self):
        """Copy output directory to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.saved_file_path.toPlainText())

class FailureDialog(QDialog):
    """Wrapper for the failure dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fail_dialog()
        self.ui.setupUi(self)
        self.ui.try_again.clicked.connect(self.accept)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the UI
        self.ui = Ui_AppMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PyUIRender")
        
        # Set window icon using relative path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "icon", "ico.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            # Try alternative path structure
            alt_path = os.path.join(script_dir, "Py_Project", "PyUIRender", "icon", "ico.png")
            if os.path.exists(alt_path):
                self.setWindowIcon(QIcon(alt_path))
            else:
                # Try absolute path as last resort
                abs_path = r"C:\Code\Py_Project\PyUIRender\icon\ico.png"
                if os.path.exists(abs_path):
                    self.setWindowIcon(QIcon(abs_path))
                else:
                    print(f"Icon not found at: {icon_path}, {alt_path}, or {abs_path}")
        
        # Load settings
        self.settings = QSettings("PyUIRender", "AppConfig")
        last_output_dir = self.settings.value("last_output_dir", os.getcwd())
        
        # Connect signals
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.select_file_btn.clicked.connect(self.browse_ui_files)
        self.ui.clear_list_btn.clicked.connect(self.clear_file_list)
        self.ui.destination_folder_btn.clicked.connect(self.select_output_directory)
        self.ui.convert_btn.clicked.connect(self.convert_files)
        
        # Initialize scroll area
        self.setup_scroll_area()
        
        # Reset progress bar
        self.ui.progressBar.setValue(0)
        
        # Store selected files
        self.selected_files = []
        
        # Set initial output path from settings
        self.ui.file_path.setText(str(last_output_dir))
        
        # Conversion status tracking
        self.conversion_in_progress = False
        self.current_file_index = 0
        self.failed_files = []
        self.successful_files = []  # Track successfully converted files

    def setup_scroll_area(self):
        """Initialize the scroll area for file display"""
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_layout.setSpacing(5)
        
        # Add placeholder text
        self.placeholder_label = QLabel("No files selected. Click 'Browse .ui Files' to add files.")
        self.placeholder_label.setStyleSheet("color: gray; font-style: italic;")
        self.scroll_layout.addWidget(self.placeholder_label)
        self.scroll_layout.addStretch(1)

    def browse_ui_files(self):
        """Open file dialog to select multiple .ui files"""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)  # Use full enum path
        file_dialog.setNameFilter("UI Files (*.ui)")
        file_dialog.setWindowTitle("Select UI Files")
        
        if file_dialog.exec():
            new_files = file_dialog.selectedFiles()
            for file_path in new_files:
                if (file_path.lower().endswith('.ui') and 
                    file_path not in self.selected_files):
                    self.selected_files.append(file_path)
            self.update_file_list()

    def update_file_list(self):
        """Update scroll area with selected files"""
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if widget := item.widget():
                widget.deleteLater()
        
        if self.selected_files:
            for file_path in self.selected_files:
                file_label = QLabel(os.path.basename(file_path))
                file_label.setStyleSheet("""
                    QLabel {
                        padding: 5px;
                        border-bottom: 1px solid #e0e0e0;
                    }
                    QLabel:hover {
                        background-color: #f0f5ff;
                    }
                """)
                file_label.setToolTip(file_path)
                self.scroll_layout.addWidget(file_label)
        else:
            self.placeholder_label = QLabel("No files selected. Click 'Browse .ui Files' to add files.")
            self.placeholder_label.setStyleSheet("color: gray; font-style: italic;")
            self.scroll_layout.addWidget(self.placeholder_label)
        
        self.scroll_layout.addStretch(1)

    def clear_file_list(self):
        """Clear all selected files from the list"""
        self.selected_files = []
        self.update_file_list()
        
    def select_output_directory(self):
        """Open dialog to select output directory"""
        folder_dialog = QFileDialog(self)
        folder_dialog.setFileMode(QFileDialog.FileMode.Directory)  # Use full enum path
        folder_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)  # Use full enum path
        folder_dialog.setWindowTitle("Select Output Directory")
        
        if folder_dialog.exec():
            selected_dirs = folder_dialog.selectedFiles()
            if selected_dirs:
                output_dir = selected_dirs[0]
                self.ui.file_path.setText(output_dir)
                return True
        return False
    
    def validate_inputs(self):
        """Validate inputs before conversion"""
        errors = []
        
        # Check if files are selected
        if not self.selected_files:
            errors.append("No files selected. Please add .ui files to convert.")
            
        # Check if output directory is valid
        output_dir = self.ui.file_path.text()
        if not output_dir:
            errors.append("Output directory is not set. Please select an output directory.")
        elif not os.path.isdir(output_dir):
            errors.append("Selected output directory does not exist. Please select a valid directory.")
            
        # Show errors if any
        if errors:
            QMessageBox.warning(
                self,
                "Missing Information",
                "\n\n".join(errors),
                QMessageBox.StandardButton.Ok  # Use full enum path
            )
            return False
            
        return True
    
    def convert_files(self):
        """Start the conversion process for all selected files"""
        if self.conversion_in_progress:
            return
            
        # Validate inputs before proceeding
        if not self.validate_inputs():
            return
            
        output_dir = self.ui.file_path.text()
        
        # Save output directory to settings
        self.settings.setValue("last_output_dir", output_dir)
        
        method = self.ui.method_dropdown.currentText()
        self.set_ui_enabled(False)
        self.conversion_in_progress = True
        self.current_file_index = 0
        self.failed_files = []
        self.successful_files = []  # Reset successful files list
        self.ui.progressBar.setValue(0)
        
        QTimer.singleShot(100, lambda: self.convert_next_file(method, output_dir))
    
    def convert_next_file(self, method, output_dir):
        """Convert the next file in the queue"""
        if self.current_file_index >= len(self.selected_files):
            self.conversion_complete(output_dir)
            return
            
        input_path = self.selected_files[self.current_file_index]
        filename = os.path.basename(input_path)
        output_path = None  # Initialize to avoid unbound warning
        
        try:
            if method == "PyQt5":
                from convert_pyqt5 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            elif method == "PyQt6":
                from convert_pyqt6 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            elif method == "PySide6":
                from convert_pyside6 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            # Add to successful files only if conversion succeeded
            if output_path:
                self.successful_files.append(output_path)
                print(f"Converted: {filename} -> {os.path.basename(output_path)}")
            
        except Exception as e:
            error_msg = f"Error converting {filename}:\n{str(e)}"
            print(error_msg)
            self.failed_files.append((filename, str(e)))
        
        # Update progress
        self.current_file_index += 1
        progress = int((self.current_file_index / len(self.selected_files)) * 100)
        self.ui.progressBar.setValue(progress)
        
        # Process next file
        QTimer.singleShot(50, lambda: self.convert_next_file(method, output_dir))
    
    def conversion_complete(self, output_dir):
        """Handle conversion completion"""
        self.conversion_in_progress = False
        self.set_ui_enabled(True)
        
        if not self.failed_files:
            self.show_success_dialog(output_dir, self.successful_files)
        else:
            error_msg = f"{len(self.failed_files)} out of {len(self.selected_files)} files failed to convert."
            self.show_failure_dialog("Conversion Failed", error_msg)
    
    def show_success_dialog(self, output_dir, converted_files):
        """Show the success dialog"""
        dialog = SuccessDialog(self, output_dir)
        dialog.exec()
        self.ui.progressBar.setValue(0)
    
    def show_failure_dialog(self, title, message):
        """Show the failure dialog"""
        dialog = FailureDialog(self)
        dialog.exec()
        self.ui.progressBar.setValue(0)
    
    def set_ui_enabled(self, enabled):
        """Enable/disable UI controls during conversion"""
        self.ui.select_file_btn.setEnabled(enabled)
        self.ui.clear_list_btn.setEnabled(enabled)
        self.ui.destination_folder_btn.setEnabled(enabled)
        self.ui.convert_btn.setEnabled(enabled)
        self.ui.method_dropdown.setEnabled(enabled)
        self.ui.file_path.setEnabled(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application icon using relative path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "icon", "ico.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    else:
        # Try alternative path structure
        alt_path = os.path.join(script_dir, "Py_Project", "PyUIRender", "icon", "ico.png")
        if os.path.exists(alt_path):
            app.setWindowIcon(QIcon(alt_path))
        else:
            # Try absolute path as last resort
            abs_path = r"C:\Code\Py_Project\PyUIRender\icon\ico.png"
            if os.path.exists(abs_path):
                app.setWindowIcon(QIcon(abs_path))
            else:
                print(f"Icon not found at: {icon_path}, {alt_path}, or {abs_path}")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
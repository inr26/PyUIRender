import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, 
                               QLabel, QVBoxLayout, QDialog)
from PySide6.QtCore import QTimer
from appWindow import Ui_AppMainWindow
from success_dia import Ui_success_dialog  # Import success dialog
from failed_dia import Ui_fail_dialog      # Import failure dialog

class SuccessDialog(QDialog):
    """Wrapper for the success dialog"""
    def __init__(self, parent=None, output_dir=""):
        super().__init__(parent)
        self.ui = Ui_success_dialog()
        self.ui.setupUi(self)
        
        # Set output directory in the text field
        self.ui.saved_file_pathj.setPlainText(output_dir)
        
        # Connect copy button
        self.ui.copy_path_btn.clicked.connect(self.copy_path)
        
    def copy_path(self):
        """Copy output path to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.saved_file_pathj.toPlainText())

class FailureDialog(QDialog):
    """Wrapper for the failure dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fail_dialog()
        self.ui.setupUi(self)
        
        # Connect try again button
        self.ui.try_again.clicked.connect(self.accept)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the UI
        self.ui = Ui_AppMainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("PyUIRender")
        
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
        
        # Set initial output path to current directory
        self.ui.file_path.setText(os.getcwd())
        
        # Conversion status tracking
        self.conversion_in_progress = False
        self.current_file_index = 0
        self.failed_files = []  # Track failed files

    def setup_scroll_area(self):
        """Initialize the scroll area for file display"""
        # Create a layout for the scroll area contents
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_layout.setSpacing(5)
        
        # Add placeholder text
        self.placeholder_label = QLabel("No files selected. Click 'Browse .ui Files' to add files.")
        self.placeholder_label.setStyleSheet("color: gray; font-style: italic;")
        self.scroll_layout.addWidget(self.placeholder_label)
        
        # Add stretch to push content to top
        self.scroll_layout.addStretch(1)

    def browse_ui_files(self):
        """Open file dialog to select multiple .ui files"""
        # Create and configure file dialog
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("UI Files (*.ui)")
        file_dialog.setWindowTitle("Select UI Files")
        
        # Execute dialog and get selected files
        if file_dialog.exec():
            new_files = file_dialog.selectedFiles()
            
            # Filter only .ui files and avoid duplicates
            for file_path in new_files:
                if (file_path.lower().endswith('.ui') and 
                    file_path not in self.selected_files):
                    self.selected_files.append(file_path)
            
            # Update UI
            self.update_file_list()

    def update_file_list(self):
        """Update scroll area with selected files"""
        # Clear existing widgets
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if widget := item.widget():
                widget.deleteLater()
        
        # Add files to list
        if self.selected_files:
            for file_path in self.selected_files:
                # Create file label
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
                file_label.setToolTip(file_path)  # Show full path on hover
                self.scroll_layout.addWidget(file_label)
        else:
            # Add placeholder text if no files
            self.placeholder_label = QLabel("No files selected. Click 'Browse .ui Files' to add files.")
            self.placeholder_label.setStyleSheet("color: gray; font-style: italic;")
            self.scroll_layout.addWidget(self.placeholder_label)
        
        # Add stretch to push content to top
        self.scroll_layout.addStretch(1)

    def clear_file_list(self):
        """Clear all selected files from the list"""
        self.selected_files = []
        self.update_file_list()
        
    def select_output_directory(self):
        """Open dialog to select output directory"""
        # Create folder selection dialog
        folder_dialog = QFileDialog(self)
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly, True)
        folder_dialog.setWindowTitle("Select Output Directory")
        
        # Execute dialog and get selected folder
        if folder_dialog.exec():
            selected_dirs = folder_dialog.selectedFiles()
            if selected_dirs:
                output_dir = selected_dirs[0]
                # Set the selected path in the QLineEdit
                self.ui.file_path.setText(output_dir)
                return True
        return False
    
    def convert_files(self):
        """Start the conversion process for all selected files"""
        # Check if conversion is already in progress
        if self.conversion_in_progress:
            return
            
        # Validate inputs
        if not self.selected_files:
            self.show_failure_dialog("No files selected!", "Please select at least one .ui file to convert.")
            return
            
        output_dir = self.ui.file_path.text()
        if not os.path.isdir(output_dir):
            self.show_failure_dialog("Invalid directory!", "Please select a valid output directory.")
            return
            
        # Get selected conversion method
        method = self.ui.method_dropdown.currentText()
        
        # Disable UI during conversion
        self.set_ui_enabled(False)
        self.conversion_in_progress = True
        self.current_file_index = 0
        self.failed_files = []  # Reset failed files list
        self.ui.progressBar.setValue(0)
        
        # Start conversion process
        QTimer.singleShot(100, lambda: self.convert_next_file(method, output_dir))
    
    def convert_next_file(self, method, output_dir):
        """Convert the next file in the queue"""
        if self.current_file_index >= len(self.selected_files):
            # Conversion complete
            self.conversion_complete(output_dir)
            return
            
        # Get current file
        input_path = self.selected_files[self.current_file_index]
        filename = os.path.basename(input_path)
        
        try:
            # Convert based on selected method
            if method == "PyQt5":
                from convert_pyqt5 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            elif method == "PyQt6":
                from convert_pyqt6 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            elif method == "PySide6":
                from convert_pyside6 import convert_ui_to_py
                output_path = convert_ui_to_py(input_path, output_dir)
                
            # Success
            print(f"Converted: {filename} -> {os.path.basename(output_path)}")
            
        except Exception as e:
            # Error handling
            error_msg = f"Error converting {filename}:\n{str(e)}"
            print(error_msg)
            self.failed_files.append((filename, str(e)))
        
        # Update progress
        self.current_file_index += 1
        progress = int((self.current_file_index / len(self.selected_files)) * 100)
        self.ui.progressBar.setValue(progress)
        
        # Process next file after a short delay (allows UI to update)
        QTimer.singleShot(50, lambda: self.convert_next_file(method, output_dir))
    
    def conversion_complete(self, output_dir):
        """Handle conversion completion"""
        self.conversion_in_progress = False
        self.set_ui_enabled(True)
        
        # Show appropriate dialog based on success/failure
        if not self.failed_files:
            self.show_success_dialog(output_dir)
        else:
            error_msg = f"{len(self.failed_files)} out of {len(self.selected_files)} files failed to convert."
            self.show_failure_dialog("Conversion Failed", error_msg)
    
    def show_success_dialog(self, output_dir):
        """Show the success dialog"""
        dialog = SuccessDialog(self, output_dir)
        dialog.exec()
        
        # Reset progress bar after dialog closes
        self.ui.progressBar.setValue(0)
    
    def show_failure_dialog(self, title, message):
        """Show the failure dialog"""
        dialog = FailureDialog(self)
        
        # Customize dialog if possible (your UI doesn't have a message field)
        # If you want to show the message, you'd need to modify your failure dialog UI
        # For now, we'll just show the dialog as is
        dialog.exec()
        
        # Reset progress bar after dialog closes
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
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Execute the application
    sys.exit(app.exec())


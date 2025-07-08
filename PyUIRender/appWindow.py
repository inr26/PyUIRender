from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (
    QComboBox, QLabel, QLineEdit, QProgressBar, 
    QPushButton, QScrollArea, QWidget)
from PyUIRender import resources_rc

class Ui_AppMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 527)
        icon = QIcon(QIcon.fromTheme(u"0"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: rgb(237, 236, 234);\n"
"    border-radius: 12px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.select_file_btn = QPushButton(self.centralwidget)
        self.select_file_btn.setObjectName(u"select_file_btn")
        self.select_file_btn.setGeometry(QRect(10, 384, 130, 29))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.select_file_btn.setFont(font)
        self.select_file_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(70, 130, 230);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20); /* Black hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60, 120, 220);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(75, 135, 235);\n"
"    }\n"
"}\n"
"\n"
"QPushButton {\n"
"    transition: background-color 150ms ease;\n"
"}")
        self.clear_list_btn = QPushButton(self.centralwidget)
        self.clear_list_btn.setObjectName(u"clear_list_btn")
        self.clear_list_btn.setGeometry(QRect(691, 147, 90, 30))
        self.clear_list_btn.setFont(font)
        self.clear_list_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(70, 130, 230);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    padding-left: 3px;\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20); /* Black hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60, 120, 220);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(75, 135, 235);\n"
"    }\n"
"}\n"
"\n"
"QPushButton {\n"
"    transition: background-color 150ms ease;\n"
"}")
        self.method_dropdown = QComboBox(self.centralwidget)
        self.method_dropdown.addItem("")
        self.method_dropdown.addItem("")
        self.method_dropdown.addItem("")
        self.method_dropdown.setObjectName(u"method_dropdown")
        self.method_dropdown.setGeometry(QRect(660, 385, 120, 28))
        self.method_dropdown.setFont(font)
        self.method_dropdown.setStyleSheet(u"QPushButton { background-color: rgb(70, 130, 230); color: white;}\n")

        self.file_path = QLineEdit(self.centralwidget)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setGeometry(QRect(10, 430, 560, 27))
        self.file_path.setFont(font)
        self.file_path.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-radius: 4px;\n"
"    padding: 5px 8px;\n"
"    color: rgb(30, 30, 30);\n"
"    selection-background-color: rgb(100, 160, 255);\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(70, 130, 230);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLineEdit {\n"
"        background-color: rgb(55, 55, 58);\n"
"        border: 1px solid rgb(85, 85, 90);\n"
"        color: rgb(240, 240, 240);\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 1px solid rgb(90, 150, 250);\n"
"    }\n"
"}")
        self.destination_folder_btn = QPushButton(self.centralwidget)
        self.destination_folder_btn.setObjectName(u"destination_folder_btn")
        self.destination_folder_btn.setGeometry(QRect(582, 430, 200, 29))
        self.destination_folder_btn.setFont(font)
        self.destination_folder_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 130, 230);\n"
"        color: white;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20); /* Black hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60, 120, 220);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(75, 135, 235);\n"
"    }\n"
"}\n"
"\n"
"QPushButton {\n"
"    transition: background-color 150ms ease;\n"
"}")
        self.convert_btn = QPushButton(self.centralwidget)
        self.convert_btn.setObjectName(u"convert_btn")
        self.convert_btn.setGeometry(QRect(10, 474, 110, 29))
        self.convert_btn.setFont(font)
        self.convert_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(70, 130, 230);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20); /* Black hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60, 120, 220);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(75, 135, 235);\n"
"    }\n"
"}\n"
"\n"
"QPushButton {\n"
"    transition: background-color 150ms ease;\n"
"}")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(126, 480, 590, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.progressBar.setFont(font1)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(210, 210, 210);\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(170, 170, 170);\n"
"    text-align: center;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(244,85,29); \n"
"    border-radius: 2px;\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QProgressBar {\n"
"        background-color: rgb(50, 50, 53);\n"
"        border: 1px solid rgb(65, 65, 70);\n"
"    }\n"
"}")
        self.progressBar.setValue(24)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 152, 130, 20))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel, QCheckBox, QRadioButton {\n"
"    color: rgb(30, 30, 30);\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QLabel[accessibleName=\"title\"] {\n"
"    font: bold 11pt \"Segoe UI\";\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel, QCheckBox, QRadioButton {\n"
"        color: rgb(240, 240, 240);\n"
"    }\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 389, 210, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel, QCheckBox, QRadioButton {\n"
"    color: rgb(30, 30, 30);\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QLabel[accessibleName=\"title\"] {\n"
"    font: bold 11pt \"Segoe UI\";\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel, QCheckBox, QRadioButton {\n"
"        color: rgb(240, 240, 240);\n"
"    }\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 9, 471, 131))
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro"])
        self.label_3.setFont(font2)
        self.label_3.setPixmap(QPixmap(u":/images/images/ban_new_s.png"))
        self.label_3.setScaledContents(True)
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(725, 471, 56, 30))
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 130, 230);\n"
"        color: white;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20); /* Black hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60, 120, 220);\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(75, 135, 235);\n"
"    }\n"
"}\n"
"\n"
"QPushButton {\n"
"    transition: background-color 150ms ease;\n"
"}")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 180, 771, 191))
        self.scrollArea.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 189))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_file_btn.setText(QCoreApplication.translate("MainWindow", u"Browse .ui Files", None))
        self.clear_list_btn.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.method_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"PyQt5", None))
        self.method_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"PyQt6", None))
        self.method_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"PySide6", None))

        self.destination_folder_btn.setText(QCoreApplication.translate("MainWindow", u"Choose Destination Folder", None))
        self.convert_btn.setText(QCoreApplication.translate("MainWindow", u"Convert Now", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selected .ui Files:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Choose your preferred method:", None))
        self.label_3.setText("")
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
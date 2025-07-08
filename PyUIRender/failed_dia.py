from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QLabel, QPushButton, QPlainTextEdit)
from PyUIRender import resources_rc

class Ui_fail_dialog(object):
    def setupUi(self, fail_dialog):
        if not fail_dialog.objectName():
            fail_dialog.setObjectName(u"fail_dialog")
        fail_dialog.resize(414, 290)  # Increased height to show error messages
        fail_dialog.setStyleSheet(u"""
            QDialog {
                background-color: rgb(238, 80, 67);
                border-radius: 15px;
                border: none;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            QPlainTextEdit {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas, monospace;
                color: #f0f0f0;
                border: 1px solid rgba(0, 0, 0, 0.1);
            }
        """)
        
        # Error icon
        self.f_icon = QLabel(fail_dialog)
        self.f_icon.setObjectName(u"f_icon")
        self.f_icon.setGeometry(QRect(20, 20, 80, 80))
        self.f_icon.setStyleSheet(u"""
            QLabel {
                qproperty-alignment: AlignCenter;
                border-radius: 40px;
                min-width: 80px;
                min-height: 80px;
                max-width: 80px;
                max-height: 80px;
                background-color: rgba(226, 117, 117, 1);
            }
            @media (prefers-color-scheme: dark) {
                QLabel {
                    border: 1px solid rgb(75, 75, 80);
                }
            }
        """)
        self.f_icon.setPixmap(QPixmap(u":/images/images/sad_r.png"))
        self.f_icon.setScaledContents(True)
        
        # Main failure message
        self.f_msf = QLabel(fail_dialog)
        self.f_msf.setObjectName(u"f_msf")
        self.f_msf.setGeometry(QRect(115, 20, 281, 40))
        self.f_msf.setStyleSheet(u"""
            QLabel {
                font-family: "Source Sans 3 Semibold";
                font-size: 20px;
                color: rgb(30, 30, 30);
                qproperty-alignment: AlignCenter;
            }
            @media (prefers-color-scheme: dark) {
                QLabel {
                    color: rgb(240, 240, 240);
                }
            }
        """)
        
        # Subtitle with file count
        self.subtitle = QLabel(fail_dialog)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(115, 60, 281, 20))
        self.subtitle.setStyleSheet(u"""
            QLabel {
                font-family: "Source Sans 3";
                font-size: 12px;
                color: rgb(30, 30, 30);
                qproperty-alignment: AlignCenter;
            }
            @media (prefers-color-scheme: dark) {
                QLabel {
                    color: rgb(240, 240, 240);
                }
            }
        """)
        
        # Error details display
        self.error_details = QPlainTextEdit(fail_dialog)
        self.error_details.setObjectName(u"error_details")
        self.error_details.setGeometry(QRect(20, 110, 374, 130))
        self.error_details.setReadOnly(True)
        
        # Try again button
        self.try_again = QPushButton(fail_dialog)
        self.try_again.setObjectName(u"try_again")
        self.try_again.setGeometry(QRect(160, 250, 100, 29))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.try_again.setFont(font)
        self.try_again.setStyleSheet(u"""
            QPushButton {
                background-color: rgb(70, 130, 230);
                color: white;
                border-radius: 4px;
                padding: 6px 12px;
                border: none;
                font: 9pt "Segoe UI";
            }
            QPushButton:hover {
                background-color: rgb(20, 20, 20);
            }
            QPushButton:pressed {
                background-color: rgb(60, 120, 220);
            }
            @media (prefers-color-scheme: dark) {
                QPushButton {
                    background-color: rgb(90, 150, 250);
                }
                QPushButton:pressed {
                    background-color: rgb(75, 135, 235);
                }
            }
            QPushButton {
                transition: background-color 150ms ease;
            }
        """)
        
        # Connect slots
        self.retranslateUi(fail_dialog)
        QMetaObject.connectSlotsByName(fail_dialog)

    def retranslateUi(self, fail_dialog):
        fail_dialog.setWindowTitle(QCoreApplication.translate("fail_dialog", u"Conversion Failed!!!", None))
        self.f_icon.setText("")
        self.f_msf.setText(QCoreApplication.translate("fail_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Task Failed!</span></p></body></html>", None))
        self.subtitle.setText(QCoreApplication.translate("fail_dialog", u"", None))
        self.error_details.setPlaceholderText(QCoreApplication.translate("fail_dialog", u"Error details will appear here...", None))
        self.try_again.setText(QCoreApplication.translate("fail_dialog", u"Try Again", None))
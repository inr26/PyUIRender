from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QLabel, QPushButton,)
import resources_rc

class Ui_fail_dialog(object):
    def setupUi(self, fail_dialog):
        if not fail_dialog.objectName():
            fail_dialog.setObjectName(u"fail_dialog")
        fail_dialog.resize(414, 151)
        fail_dialog.setStyleSheet(u"QDialog {\n"
"    background-color: rgb(238, 80, 67);  \n"
"    border-radius: 15px;                  \n"
"   \n"
"    border: none;\n"
"    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);\n"
"}")
        self.f_icon = QLabel(fail_dialog)
        self.f_icon.setObjectName(u"f_icon")
        self.f_icon.setGeometry(QRect(20, 20, 80, 80))
        self.f_icon.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    max-width: 80px;\n"
"    max-height: 80px;\n"
"    background-color: rgb(226, 117, 117, 1);\n"
"}\n"
"\n"
"/* Dark mode adjustments */\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel {\n"
"        border: 1px solid rgb(75, 75, 80);\n"
"    }\n"
"}")
        self.f_icon.setPixmap(QPixmap(u":/images/images/sad_r.png"))
        self.f_icon.setScaledContents(True)
        self.f_msf = QLabel(fail_dialog)
        self.f_msf.setObjectName(u"f_msf")
        self.f_msf.setGeometry(QRect(115, 17, 281, 82))
        self.f_msf.setStyleSheet(u"\n"
"QLabel {\n"
"    font-family: \"Source Sans 3 Semibold\";\n"
"    font-size: 45px; /* Changed from 20pt to 20px */\n"
"    color: rgb(30, 30, 30);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"}\n"
"\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel {\n"
"        color: rgb(240, 240, 240);\n"
"    }\n"
"}")
        self.try_again = QPushButton(fail_dialog)
        self.try_again.setObjectName(u"try_again")
        self.try_again.setGeometry(QRect(160, 108, 100, 29))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.try_again.setFont(font)
        self.try_again.setStyleSheet(u"QPushButton {\n"
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
#if QT_CONFIG(shortcut)
        self.f_msf.setBuddy(self.f_msf)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(fail_dialog)

        QMetaObject.connectSlotsByName(fail_dialog)
    # setupUi

    def retranslateUi(self, fail_dialog):
        fail_dialog.setWindowTitle(QCoreApplication.translate("fail_dialog", u"Failed!!!", None))
        self.f_icon.setText("")
        self.f_msf.setText(QCoreApplication.translate("fail_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:27pt; font-weight:700;\">Task Failed!</span></p></body></html>", None))
        self.try_again.setText(QCoreApplication.translate("fail_dialog", u"Try Again!", None))
    # retranslateUi


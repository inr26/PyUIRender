from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_success_dialog(object):
    def setupUi(self, success_dialog):
        if not success_dialog.objectName():
            success_dialog.setObjectName(u"success_dialog")
        success_dialog.resize(448, 211)
        success_dialog.setStyleSheet(u"QDialog {\n"
"    background-color: rgb(237, 236, 234);\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}\n"
"@media (prefers-color-scheme: dark) {\n"
"    QDialog {\n"
"        background-color: rgb(30, 30, 32);\n"
"    }\n"
"}")
        self.s_msg = QLabel(success_dialog)
        self.s_msg.setObjectName(u"s_msg")
        self.s_msg.setGeometry(QRect(123, 25, 311, 70))
        self.s_msg.setStyleSheet(u"QLabel {\n"
"    font-family: \"Source Sans 3 Semibold\";\n"
"    font-size: 45px; /* Changed from 20pt to 20px */\n"
"    color: rgb(0, 128, 0);\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel {\n"
"        color: rgb(0, 128, 0);\n"
"    }\n"
"}\n"
"")
        self.msg = QLabel(success_dialog)
        self.msg.setObjectName(u"msg")
        self.msg.setGeometry(QRect(20, 109, 261, 20))
        self.msg.setStyleSheet(u"QLabel {\n"
"    font-family: \"Source Sans 3 Black\";\n"
"    font-size: 9pt;\n"
"    color: rgb(0, 0, 0);          /* pure black */\n"
"    qproperty-alignment: AlignCenter;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"@media (prefers-color-scheme: dark) {\n"
"    #msg {\n"
"        color: rgb(0, 0, 0);      /* override dark-mode color to black */\n"
"    }\n"
"}\n"
"")
        self.s_icon = QLabel(success_dialog)
        self.s_icon.setObjectName(u"s_icon")
        self.s_icon.setGeometry(QRect(20, 20, 80, 80))
        self.s_icon.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    max-width: 80px;\n"
"    max-height: 80px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Dark mode adjustments */\n"
"@media (prefers-color-scheme: dark) {\n"
"    QLabel {\n"
"        border: 1px solid rgb(75, 75, 80);\n"
"    }\n"
"}")
        self.s_icon.setPixmap(QPixmap(u":/images/images/happy_a.png"))
        self.s_icon.setScaledContents(True)
        self.copy_path_btn = QPushButton(success_dialog)
        self.copy_path_btn.setObjectName(u"copy_path_btn")
        self.copy_path_btn.setGeometry(QRect(393, 135, 35, 35))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.copy_path_btn.setFont(font)
        self.copy_path_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(70, 135, 235);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    border: none;\n"
"    min-width: 35px;\n"
"    min-height: 35px;\n"
"    max-width: 35px;\n"
"    max-height: 35px;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    transition: background-color 150ms ease;\n"
"    qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"\n"
"QPushButton::icon {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"QPushButton:hover::icon {\n"
"    filter: invert(100%);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 200, 0);\n"
"}\n"
"\n"
"\n"
"/* Dark-mode adjustments */\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPushButton {\n"
"        background-color: rgb(90, 150, 250);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(20, 20, 20);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(0, 180, 0);\n"
"    }\n"
"   "
                        " QPushButton:hover::icon {\n"
"        filter: invert(100%);\n"
"    }\n"
"	\n"
"	\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/copy_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy_path_btn.setIcon(icon)
        self.copy_path_btn.setIconSize(QSize(30, 30))
        self.saved_file_path = QPlainTextEdit(success_dialog)
        self.saved_file_path.setObjectName(u"saved_file_path")
        self.saved_file_path.setGeometry(QRect(18, 133, 361, 41))
        self.saved_file_path.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: rgb(245, 245, 245); \n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-radius: 6px; \n"
"    padding: 10px;\n"
"    font-family: \"Source Sans 3 Black\", \"Consolas\", monospace;\n"
"    font-size: 10pt;\n"
"    color: rgb(30, 30, 30);\n"
"    selection-background-color: rgb(70, 130, 230);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(70, 130, 230);\n"
"}\n"
"\n"
"\n"
"@media (prefers-color-scheme: dark) {\n"
"    QPlainTextEdit {\n"
"        background-color: rgb(45, 45, 48);\n"
"        border: 1px solid rgb(70, 70, 75);\n"
"        color: rgb(240, 240, 240);\n"
"    }\n"
"    \n"
"    QPlainTextEdit:focus {\n"
"        border: 1px solid rgb(90, 150, 250);\n"
"    }\n"
"    \n"
"    QPlainTextEdit QScrollBar:vertical {\n"
"        background: rgb(45, 45, 48);\n"
"    }\n"
"    \n"
"    QPlainTextEdit QScrollBar::handle:vertical {\n"
"        background: rgb(80, 80, 85);\n"
"    }\n"
"}")

        self.retranslateUi(success_dialog)

        QMetaObject.connectSlotsByName(success_dialog)
    # setupUi

    def retranslateUi(self, success_dialog):
        success_dialog.setWindowTitle(QCoreApplication.translate("success_dialog", u"Success!!!", None))
        self.s_msg.setText(QCoreApplication.translate("success_dialog", u"<html><head/><body><p><span style=\" font-size:27pt; font-weight:700;\">Task Finished</span></p></body></html>", None))
        self.msg.setText(QCoreApplication.translate("success_dialog", u"Your data was converted and stored at:", None))
        self.s_icon.setText("")
        self.copy_path_btn.setText("")
        self.saved_file_path.setPlainText("")
    # retranslateUi


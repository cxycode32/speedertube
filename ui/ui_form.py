# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QListView, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_SpeederTubeGUI(object):
    def setupUi(self, SpeederTubeGUI):
        if not SpeederTubeGUI.objectName():
            SpeederTubeGUI.setObjectName(u"SpeederTubeGUI")
        SpeederTubeGUI.resize(620, 820)
        self.gridLayoutWidget = QWidget(SpeederTubeGUI)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 600, 800))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 4, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 4, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 2)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 2)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 7, 0, 1, 2)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 2)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 2)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 2)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 11, 0, 1, 2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 13, 1, 1, 1)

        self.listView = QListView(self.gridLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 16, 0, 1, 1)

        self.listView_2 = QListView(self.gridLayoutWidget)
        self.listView_2.setObjectName(u"listView_2")

        self.gridLayout.addWidget(self.listView_2, 16, 1, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 17, 0, 1, 2)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 18, 0, 1, 1)

        self.progressBar = QProgressBar(self.gridLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 19, 0, 1, 2)

        self.listView_3 = QListView(self.gridLayoutWidget)
        self.listView_3.setObjectName(u"listView_3")

        self.gridLayout.addWidget(self.listView_3, 20, 0, 1, 2)


        self.retranslateUi(SpeederTubeGUI)

        QMetaObject.connectSlotsByName(SpeederTubeGUI)
    # setupUi

    def retranslateUi(self, SpeederTubeGUI):
        SpeederTubeGUI.setWindowTitle(QCoreApplication.translate("SpeederTubeGUI", u"SpeederTube", None))
        self.label.setText(QCoreApplication.translate("SpeederTubeGUI", u"Select the Spotify playlist you want to migrate:", None))
        self.label_3.setText(QCoreApplication.translate("SpeederTubeGUI", u"Create a new YouTube playlist to migrate to:", None))
        self.radioButton.setText(QCoreApplication.translate("SpeederTubeGUI", u"Public", None))
        self.radioButton_2.setText(QCoreApplication.translate("SpeederTubeGUI", u"Private", None))
        self.label_2.setText(QCoreApplication.translate("SpeederTubeGUI", u"Or select the YouTube playlist you want to migrate to:", None))
        self.label_6.setText(QCoreApplication.translate("SpeederTubeGUI", u"After you've selected the Spotify and YouTube playlists, click the button to start migrating:", None))
        self.pushButton.setText(QCoreApplication.translate("SpeederTubeGUI", u"Start Migrating", None))
        self.label_4.setText(QCoreApplication.translate("SpeederTubeGUI", u"Song(s) successfully migrated:", None))
        self.label_5.setText(QCoreApplication.translate("SpeederTubeGUI", u"Song(s) failed to migrate:", None))
        self.label_7.setText(QCoreApplication.translate("SpeederTubeGUI", u"Progress:", None))
    # retranslateUi
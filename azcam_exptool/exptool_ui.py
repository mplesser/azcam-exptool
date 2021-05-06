# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exptool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ExposureTool(object):
    def setupUi(self, ExposureTool):
        if not ExposureTool.objectName():
            ExposureTool.setObjectName(u"ExposureTool")
        ExposureTool.resize(643, 412)
        ExposureTool.setMinimumSize(QSize(260, 100))
        ExposureTool.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setPointSize(8)
        ExposureTool.setFont(font)
        ExposureTool.setIconSize(QSize(15, 15))
        self.centralwidget = QWidget(ExposureTool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 270, 461, 21))
        self.progressBar.setValue(100)
        self.testimage_CheckBox = QCheckBox(self.centralwidget)
        self.testimage_CheckBox.setObjectName(u"testimage_CheckBox")
        self.testimage_CheckBox.setGeometry(QRect(390, 30, 81, 20))
        self.imagetitle_LineEdit = QLineEdit(self.centralwidget)
        self.imagetitle_LineEdit.setObjectName(u"imagetitle_LineEdit")
        self.imagetitle_LineEdit.setGeometry(QRect(120, 80, 261, 22))
        self.messages_PlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.messages_PlainTextEdit.setObjectName(u"messages_PlainTextEdit")
        self.messages_PlainTextEdit.setGeometry(QRect(10, 300, 461, 31))
        self.exposuretime_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.exposuretime_SpinBox.setObjectName(u"exposuretime_SpinBox")
        self.exposuretime_SpinBox.setGeometry(QRect(210, 30, 81, 22))
        self.exposuretime_SpinBox.setDecimals(3)
        self.exposuretime_SpinBox.setMaximum(999999.000000000000000)
        self.exposuretime_SpinBox.setValue(1.000000000000000)
        self.imagetype_ComboBox = QComboBox(self.centralwidget)
        self.imagetype_ComboBox.setObjectName(u"imagetype_ComboBox")
        self.imagetype_ComboBox.setGeometry(QRect(120, 30, 73, 22))
        self.imagetype_Label = QLabel(self.centralwidget)
        self.imagetype_Label.setObjectName(u"imagetype_Label")
        self.imagetype_Label.setGeometry(QRect(120, 10, 91, 16))
        self.camtemp_Label = QLabel(self.centralwidget)
        self.camtemp_Label.setObjectName(u"camtemp_Label")
        self.camtemp_Label.setGeometry(QRect(120, 220, 71, 16))
        self.exposuretime_Label = QLabel(self.centralwidget)
        self.exposuretime_Label.setObjectName(u"exposuretime_Label")
        self.exposuretime_Label.setGeometry(QRect(210, 10, 91, 16))
        self.dewtemp_Label = QLabel(self.centralwidget)
        self.dewtemp_Label.setObjectName(u"dewtemp_Label")
        self.dewtemp_Label.setGeometry(QRect(220, 220, 71, 16))
        self.imagetitleLabel = QLabel(self.centralwidget)
        self.imagetitleLabel.setObjectName(u"imagetitleLabel")
        self.imagetitleLabel.setGeometry(QRect(120, 60, 91, 16))
        self.numseq_SpinBox = QSpinBox(self.centralwidget)
        self.numseq_SpinBox.setObjectName(u"numseq_SpinBox")
        self.numseq_SpinBox.setGeometry(QRect(310, 30, 61, 22))
        self.numseq_SpinBox.setMinimum(1)
        self.numseq_SpinBox.setMaximum(999999)
        self.numseq_label = QLabel(self.centralwidget)
        self.numseq_label.setObjectName(u"numseq_label")
        self.numseq_label.setGeometry(QRect(310, 10, 61, 16))
        self.buttons_splitter = QSplitter(self.centralwidget)
        self.buttons_splitter.setObjectName(u"buttons_splitter")
        self.buttons_splitter.setGeometry(QRect(10, 20, 91, 241))
        self.buttons_splitter.setOrientation(Qt.Vertical)
        self.expose_Button = QPushButton(self.buttons_splitter)
        self.expose_Button.setObjectName(u"expose_Button")
        self.buttons_splitter.addWidget(self.expose_Button)
        self.sequence_Button = QPushButton(self.buttons_splitter)
        self.sequence_Button.setObjectName(u"sequence_Button")
        self.buttons_splitter.addWidget(self.sequence_Button)
        self.filename_Button = QPushButton(self.buttons_splitter)
        self.filename_Button.setObjectName(u"filename_Button")
        self.buttons_splitter.addWidget(self.filename_Button)
        self.detector_Button = QPushButton(self.buttons_splitter)
        self.detector_Button.setObjectName(u"detector_Button")
        self.buttons_splitter.addWidget(self.detector_Button)
        self.reset_Button = QPushButton(self.buttons_splitter)
        self.reset_Button.setObjectName(u"reset_Button")
        self.buttons_splitter.addWidget(self.reset_Button)
        self.abort_Button = QPushButton(self.buttons_splitter)
        self.abort_Button.setObjectName(u"abort_Button")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.abort_Button.setFont(font1)
        self.buttons_splitter.addWidget(self.abort_Button)
        self.preferences_Button = QPushButton(self.buttons_splitter)
        self.preferences_Button.setObjectName(u"preferences_Button")
        self.buttons_splitter.addWidget(self.preferences_Button)
        self.pause_splitter = QSplitter(self.centralwidget)
        self.pause_splitter.setObjectName(u"pause_splitter")
        self.pause_splitter.setGeometry(QRect(10, 340, 225, 31))
        self.pause_splitter.setOrientation(Qt.Horizontal)
        self.pause_Button = QPushButton(self.pause_splitter)
        self.pause_Button.setObjectName(u"pause_Button")
        self.pause_Button.setEnabled(True)
        self.pause_splitter.addWidget(self.pause_Button)
        self.resume_Button = QPushButton(self.pause_splitter)
        self.resume_Button.setObjectName(u"resume_Button")
        self.resume_Button.setEnabled(True)
        self.pause_splitter.addWidget(self.resume_Button)
        self.readout_Button = QPushButton(self.pause_splitter)
        self.readout_Button.setObjectName(u"readout_Button")
        self.readout_Button.setEnabled(True)
        self.pause_splitter.addWidget(self.readout_Button)
        self.camtempvalue_label = QLabel(self.centralwidget)
        self.camtempvalue_label.setObjectName(u"camtempvalue_label")
        self.camtempvalue_label.setGeometry(QRect(120, 240, 51, 21))
        self.camtempvalue_label.setAutoFillBackground(False)
        self.camtempvalue_label.setFrameShape(QFrame.Box)
        self.camtempvalue_label.setScaledContents(False)
        self.dewtempvalue_label = QLabel(self.centralwidget)
        self.dewtempvalue_label.setObjectName(u"dewtempvalue_label")
        self.dewtempvalue_label.setGeometry(QRect(220, 240, 51, 21))
        self.dewtempvalue_label.setAutoFillBackground(False)
        self.dewtempvalue_label.setFrameShape(QFrame.Box)
        self.dewtempvalue_label.setFrameShadow(QFrame.Plain)
        self.dewtempvalue_label.setScaledContents(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 380, 461, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bar_label_1 = QLabel(self.layoutWidget)
        self.bar_label_1.setObjectName(u"bar_label_1")
        self.bar_label_1.setMinimumSize(QSize(16, 0))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.bar_label_1.setFont(font2)
        self.bar_label_1.setFrameShape(QFrame.Box)
        self.bar_label_1.setFrameShadow(QFrame.Raised)
        self.bar_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.bar_label_1)

        self.bar_label_2 = QLabel(self.layoutWidget)
        self.bar_label_2.setObjectName(u"bar_label_2")
        self.bar_label_2.setMinimumSize(QSize(16, 0))
        self.bar_label_2.setFont(font2)
        self.bar_label_2.setFrameShape(QFrame.Box)
        self.bar_label_2.setFrameShadow(QFrame.Raised)
        self.bar_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.bar_label_2)

        self.mode_label = QLabel(self.layoutWidget)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setMinimumSize(QSize(34, 0))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setWeight(50)
        self.mode_label.setFont(font3)
        self.mode_label.setFrameShape(QFrame.Box)
        self.mode_label.setFrameShadow(QFrame.Raised)
        self.mode_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mode_label)

        self.exposurestatus_label = QLabel(self.layoutWidget)
        self.exposurestatus_label.setObjectName(u"exposurestatus_label")
        self.exposurestatus_label.setMinimumSize(QSize(81, 0))
        self.exposurestatus_label.setFont(font3)
        self.exposurestatus_label.setFrameShape(QFrame.Box)
        self.exposurestatus_label.setFrameShadow(QFrame.Raised)
        self.exposurestatus_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.exposurestatus_label)

        ExposureTool.setCentralWidget(self.centralwidget)
        self.detpars_dockWidget = QDockWidget(ExposureTool)
        self.detpars_dockWidget.setObjectName(u"detpars_dockWidget")
        self.detpars_dockWidget.setMinimumSize(QSize(168, 38))
        self.detpars_dockWidget.setAutoFillBackground(False)
        self.detpars_dockWidget.setStyleSheet(u"background-color: lightgray")
        self.detpars_dockWidget.setFloating(True)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.layoutWidget_2 = QWidget(self.dockWidgetContents)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 80, 55, 41))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.colbin_label_2 = QLabel(self.layoutWidget_2)
        self.colbin_label_2.setObjectName(u"colbin_label_2")

        self.verticalLayout_2.addWidget(self.colbin_label_2)

        self.firstcol_spinBox = QSpinBox(self.layoutWidget_2)
        self.firstcol_spinBox.setObjectName(u"firstcol_spinBox")
        self.firstcol_spinBox.setMinimum(1)
        self.firstcol_spinBox.setMaximum(99999)
        self.firstcol_spinBox.setValue(1)

        self.verticalLayout_2.addWidget(self.firstcol_spinBox)

        self.layoutWidget_3 = QWidget(self.dockWidgetContents)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(80, 30, 39, 41))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rowbin_label = QLabel(self.layoutWidget_3)
        self.rowbin_label.setObjectName(u"rowbin_label")

        self.verticalLayout_3.addWidget(self.rowbin_label)

        self.rowbin_spinBox = QSpinBox(self.layoutWidget_3)
        self.rowbin_spinBox.setObjectName(u"rowbin_spinBox")
        self.rowbin_spinBox.setMinimum(1)
        self.rowbin_spinBox.setValue(1)

        self.verticalLayout_3.addWidget(self.rowbin_spinBox)

        self.layoutWidget_4 = QWidget(self.dockWidgetContents)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 130, 55, 41))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.colbin_label_4 = QLabel(self.layoutWidget_4)
        self.colbin_label_4.setObjectName(u"colbin_label_4")

        self.verticalLayout_4.addWidget(self.colbin_label_4)

        self.firstrow_spinBox = QSpinBox(self.layoutWidget_4)
        self.firstrow_spinBox.setObjectName(u"firstrow_spinBox")
        self.firstrow_spinBox.setMinimum(1)
        self.firstrow_spinBox.setMaximum(99999)
        self.firstrow_spinBox.setValue(1)

        self.verticalLayout_4.addWidget(self.firstrow_spinBox)

        self.layoutWidget_5 = QWidget(self.dockWidgetContents)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(80, 130, 55, 41))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.colbin_label_5 = QLabel(self.layoutWidget_5)
        self.colbin_label_5.setObjectName(u"colbin_label_5")

        self.verticalLayout_5.addWidget(self.colbin_label_5)

        self.lastrow_spinBox = QSpinBox(self.layoutWidget_5)
        self.lastrow_spinBox.setObjectName(u"lastrow_spinBox")
        self.lastrow_spinBox.setMinimum(1)
        self.lastrow_spinBox.setMaximum(99999)
        self.lastrow_spinBox.setValue(1)

        self.verticalLayout_5.addWidget(self.lastrow_spinBox)

        self.layoutWidget_6 = QWidget(self.dockWidgetContents)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(80, 80, 55, 41))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.colbin_label_6 = QLabel(self.layoutWidget_6)
        self.colbin_label_6.setObjectName(u"colbin_label_6")

        self.verticalLayout_6.addWidget(self.colbin_label_6)

        self.lastcol_spinBox = QSpinBox(self.layoutWidget_6)
        self.lastcol_spinBox.setObjectName(u"lastcol_spinBox")
        self.lastcol_spinBox.setMinimum(1)
        self.lastcol_spinBox.setMaximum(99999)
        self.lastcol_spinBox.setValue(1)

        self.verticalLayout_6.addWidget(self.lastcol_spinBox)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 141, 21))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)
        self.setroi_Button = QPushButton(self.dockWidgetContents)
        self.setroi_Button.setObjectName(u"setroi_Button")
        self.setroi_Button.setGeometry(QRect(10, 180, 151, 30))
        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 39, 41))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.colbin_label = QLabel(self.widget)
        self.colbin_label.setObjectName(u"colbin_label")

        self.verticalLayout.addWidget(self.colbin_label)

        self.colbin_spinBox = QSpinBox(self.widget)
        self.colbin_spinBox.setObjectName(u"colbin_spinBox")
        self.colbin_spinBox.setMinimum(1)
        self.colbin_spinBox.setValue(1)

        self.verticalLayout.addWidget(self.colbin_spinBox)

        self.detpars_dockWidget.setWidget(self.dockWidgetContents)
        self.colbin_spinBox.raise_()
        self.colbin_label.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()
        self.layoutWidget_5.raise_()
        self.layoutWidget_6.raise_()
        self.colbin_spinBox.raise_()
        self.label.raise_()
        self.setroi_Button.raise_()
        ExposureTool.addDockWidget(Qt.RightDockWidgetArea, self.detpars_dockWidget)

        self.retranslateUi(ExposureTool)

        QMetaObject.connectSlotsByName(ExposureTool)

    # setupUi

    def retranslateUi(self, ExposureTool):
        ExposureTool.setWindowTitle(QCoreApplication.translate("ExposureTool", u"ExpStatus", None))
        # if QT_CONFIG(tooltip)
        ExposureTool.setToolTip(
            QCoreApplication.translate("ExposureTool", u"azcam exposure status", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        ExposureTool.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.testimage_CheckBox.setText(
            QCoreApplication.translate("ExposureTool", u"Test Image", None)
        )
        self.imagetype_Label.setText(
            QCoreApplication.translate("ExposureTool", u"Image Type", None)
        )
        self.camtemp_Label.setText(QCoreApplication.translate("ExposureTool", u"CamTemp", None))
        self.exposuretime_Label.setText(
            QCoreApplication.translate("ExposureTool", u"Exposure Time", None)
        )
        self.dewtemp_Label.setText(QCoreApplication.translate("ExposureTool", u"DewTemp", None))
        self.imagetitleLabel.setText(
            QCoreApplication.translate("ExposureTool", u"Image Title", None)
        )
        self.numseq_label.setText(QCoreApplication.translate("ExposureTool", u"Num Seq.", None))
        self.expose_Button.setText(QCoreApplication.translate("ExposureTool", u"Expose", None))
        self.sequence_Button.setText(QCoreApplication.translate("ExposureTool", u"Sequence", None))
        self.filename_Button.setText(QCoreApplication.translate("ExposureTool", u"Filename", None))
        self.detector_Button.setText(QCoreApplication.translate("ExposureTool", u"Detector", None))
        self.reset_Button.setText(QCoreApplication.translate("ExposureTool", u"Reset", None))
        self.abort_Button.setText(QCoreApplication.translate("ExposureTool", u"Abort", None))
        self.preferences_Button.setText(
            QCoreApplication.translate("ExposureTool", u"Preferences", None)
        )
        self.pause_Button.setText(QCoreApplication.translate("ExposureTool", u"Pause", None))
        self.resume_Button.setText(QCoreApplication.translate("ExposureTool", u"Resume", None))
        self.readout_Button.setText(QCoreApplication.translate("ExposureTool", u"Readout", None))
        self.camtempvalue_label.setText(
            QCoreApplication.translate("ExposureTool", u"-999.99", None)
        )
        self.dewtempvalue_label.setText(
            QCoreApplication.translate("ExposureTool", u"-999.99", None)
        )
        # if QT_CONFIG(tooltip)
        self.bar_label_1.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.bar_label_1.setText("")
        # if QT_CONFIG(tooltip)
        self.bar_label_2.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.bar_label_2.setText("")
        # if QT_CONFIG(tooltip)
        self.mode_label.setToolTip(QCoreApplication.translate("ExposureTool", u"server mode", None))
        # endif // QT_CONFIG(tooltip)
        self.mode_label.setText(QCoreApplication.translate("ExposureTool", u"Mode", None))
        # if QT_CONFIG(tooltip)
        self.exposurestatus_label.setToolTip(
            QCoreApplication.translate("ExposureTool", u"exposure status", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.exposurestatus_label.setText(
            QCoreApplication.translate("ExposureTool", u"Exposure Status", None)
        )
        self.detpars_dockWidget.setWindowTitle(
            QCoreApplication.translate("ExposureTool", u"Detector Parameters", None)
        )
        self.colbin_label_2.setText(QCoreApplication.translate("ExposureTool", u"FirstCol", None))
        # if QT_CONFIG(tooltip)
        self.firstcol_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.rowbin_label.setText(QCoreApplication.translate("ExposureTool", u"rowbin", None))
        # if QT_CONFIG(tooltip)
        self.rowbin_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.colbin_label_4.setText(QCoreApplication.translate("ExposureTool", u"FirstRow", None))
        # if QT_CONFIG(tooltip)
        self.firstrow_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.colbin_label_5.setText(QCoreApplication.translate("ExposureTool", u"LastRow", None))
        # if QT_CONFIG(tooltip)
        self.lastrow_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.colbin_label_6.setText(QCoreApplication.translate("ExposureTool", u"LastCol", None))
        # if QT_CONFIG(tooltip)
        self.lastcol_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ExposureTool", u"Region-of_Interest", None))
        # if QT_CONFIG(tooltip)
        self.setroi_Button.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>Set Region-of-Interest with above parameters</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.setroi_Button.setText(QCoreApplication.translate("ExposureTool", u"Set ROI", None))
        self.colbin_label.setText(QCoreApplication.translate("ExposureTool", u"colbin", None))
        # if QT_CONFIG(tooltip)
        self.colbin_spinBox.setToolTip(
            QCoreApplication.translate(
                "ExposureTool",
                u"<html><head/><body><p>column binning</p></body></html>",
                None,
            )
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi

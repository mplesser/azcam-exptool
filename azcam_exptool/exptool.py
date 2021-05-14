import sys
import time

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication

import azcam
import azcam.console
from azcam import db
from azcam_exptool.exptool_ui import Ui_ExposureTool


class ExposureStatus(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        MainWindow = QMainWindow()
        self.ui = Ui_ExposureTool()
        self.ui.setupUi(self)

        self.update_interval = 300  # update time ms
        self.flags = db.exposureflags

        # connect buttons
        self.ui.detector_Button.released.connect(self.detector)
        self.ui.expose_Button.released.connect(self.expose)
        self.ui.filename_Button.released.connect(self.filename)
        self.ui.preferences_Button.released.connect(self.preferences)
        self.ui.reset_Button.released.connect(self.reset)
        self.ui.sequence_Button.released.connect(self.sequence)
        self.ui.abort_Button.released.connect(self.abort)
        self.ui.pause_Button.released.connect(self.pause)
        self.ui.resume_Button.released.connect(self.resume)
        self.ui.readout_Button.released.connect(self.readout)
        self.ui.setroi_Button.released.connect(self.set_roi)

        # add image types
        imagetypes = db.exposure.get_image_types()
        self.ui.imagetype_ComboBox.clear()
        self.ui.imagetype_ComboBox.addItems(imagetypes)

        # set initial values
        et = db.exposure.get_exposuretime()
        self.ui.exposuretime_SpinBox.setValue(et)

        # connect change events
        self.ui.imagetitle_LineEdit.editingFinished.connect(self.imagetitle_change)

        # make a timer
        self.timerID = self.ctimer = QtCore.QTimer()

        # connect timer
        QtCore.QObject.connect(
            self.ctimer, QtCore.SIGNAL("timeout()"), self.timer_update
        )

        # start timer
        self.ctimer.start(self.update_interval)

    def timer_update(self):
        """
        Called by timer.
        """

        return self.update()

    def update(self):
        """
        Update GUI indicators.
        """

        status = db.exposure.get_status()
        exp_label = status["exposurelabel"]
        expstate = status["exposurestate"]
        camtemp = float(status["camtemp"])
        dewtemp = float(status["dewtemp"])
        message = status["message"]
        progressbar = float(status["progressbar"])
        exposurecolor = status["exposurecolor"]
        mode = status["mode"]

        self.ui.progressBar.setValue(progressbar)

        if len(exp_label) > 0:
            message = f"{message}: {exp_label}"

        # set status text
        self.ui.messages_PlainTextEdit.setPlainText(message)
        self.ui.exposurestatus_label.setText(expstate)
        self.ui.mode_label.setText(mode)

        # temperatures
        self.ui.camtempvalue_label.setText(f"{camtemp:.02f}")
        self.ui.dewtempvalue_label.setText(f"{dewtemp:.02f}")
        if exposurecolor != "transparent":
            self.ui.exposurestatus_label.setStyleSheet(
                f"background-color: {exposurecolor}"
            )

        return

    def detector(self):
        """
        Detector button.
        """

        reply = db.exposure.get_roi()
        self.ui.firstcol_spinBox.setValue(reply[0])
        self.ui.lastcol_spinBox.setValue(reply[1])
        self.ui.firstrow_spinBox.setValue(reply[2])
        self.ui.lastrow_spinBox.setValue(reply[3])
        self.ui.rowbin_spinBox.setValue(reply[4])
        self.ui.colbin_spinBox.setValue(reply[5])

        return

    def expose(self):
        """
        Expose button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("Exposure started")
        self.ui.messages_PlainTextEdit.repaint()
        et = self.ui.exposuretime_SpinBox.value()
        itype = self.ui.imagetype_ComboBox.currentText()
        ititle = self.ui.imagetitle_LineEdit.text()
        db.exposure.expose1(et, itype, ititle)

        return

    def filename(self):
        """
        Filename button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("filename")

        return

    def preferences(self):
        """
        Preferences button.
        """

        return

    def reset(self):
        """
        Reset button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("resetting...")
        self.ui.messages_PlainTextEdit.repaint()
        db.exposure.reset()
        self.ui.messages_PlainTextEdit.setPlainText("")
        self.ui.messages_PlainTextEdit.repaint()

        return

    def sequence(self):
        """
        Sequence button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("sequence")

        return

    def abort(self):
        """
        Abort button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("abort")

        return

    def pause(self):
        """
        Pause button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("pause")

        return

    def resume(self):
        """
        Resume button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("resume")

        return

    def readout(self):
        """
        Readout button.
        """

        self.ui.messages_PlainTextEdit.setPlainText("readout")

        return

    def imagetitle_change(self):
        """
        Set image title.
        """

        ititle = self.ui.imagetitle_LineEdit.text()
        db.exposure.set_image_title(ititle)

        return

    def set_roi(self):
        """
        Set ROI.
        """

        firstcol = self.ui.firstcol_spinBox.value()
        lastcol = self.ui.lastcol_spinBox.value()
        firstrow = self.ui.firstrow_spinBox.value()
        lastrow = self.ui.lastrow_spinBox.value()
        colbin = self.ui.rowbin_spinBox.value()
        rowbin = self.ui.colbin_spinBox.value()
        db.exposure.set_roi(firstcol, lastcol, firstrow, lastrow, colbin, rowbin)

        return

    # *****************************************************************************
    # utilities
    # *****************************************************************************
    def start(self):

        # create
        if getattr(azcam.db, "qtapp", None) is None:
            db.qtapp = QApplication(["ExpStatus"])

        # set window location
        self.move(100, 100)

        # show GUI
        self.show()

        return


# execute when run directly
if __name__ == "__main__":

    # parse command line arguments
    try:
        i = sys.argv.index("-port")
        port = int(sys.argv[i + 1])
    except ValueError:
        port = 2402

    # create Qt app
    if db.get("atapp") is None:
        qtapp = QtCore.QCoreApplication.instance()
        if qtapp is None:
            qtapp = QApplication(sys.argv)
        db.qtapp = qtapp

    azcam.console_tools.load()

    # connect to azcamserver
    connected = db.server.connect(port=port)
    if connected:
        print("Connected to azcamserver")
    else:
        print("Not connected to azcamserver")
        time.sleep(2)
        raise azcam.AzcamError("Could not connect to azcamserver")

    gui = ExposureStatus()
    gui.start()

    # if not running in IPython, wait...
    try:
        get_ipython()
    except Exception as m:
        qtapp.exec_()

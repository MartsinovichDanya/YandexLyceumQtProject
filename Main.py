import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QLabel, QErrorMessage, QHBoxLayout, QInputDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow
import shutil
import os.path

import grayimg
import negativ
import noise
import threeDAnagliph
import bwimg

import turns

import save


class Image:
    def __init__(self):
        self.last_op = ''
        self.name = 'img.jpg'
        self.path = ''
        self.backup = ''


class Picture(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Просмотр')
        self.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.hbox = QHBoxLayout(self)
        self.pixmap = QPixmap(im.name)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        self.show()


class MainWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showButton.clicked.connect(self.show_pic)
        self.GrayButton.clicked.connect(self.mk_gray)
        self.NegButton.clicked.connect(self.mk_neg)
        self.WNButton.clicked.connect(self.mk_noise)
        self.ThreeDButton.clicked.connect(self.mk_threeD)
        self.BWButton.clicked.connect(self.mk_bw)
        self.BackButton.clicked.connect(self.back)
        self.TurnLButton.clicked.connect(self.turn_L)
        self.TurnRButton.clicked.connect(self.turn_R)
        self.SaveChangesDialog.clicked.connect(self.save_changes)
        self.SaveChangesDialog.rejected.connect(self.discard_changes)
        self.OpenFileButton.clicked.connect(self.open)

    def show_pic(self):
        self.pic = Picture()

    def mk_gray(self):
        self.StatusLabel.hide()
        grayimg.gray(im)
        self.StatusLabel.show()
        im.last_op = 'gray'

    def mk_neg(self):
        self.StatusLabel.hide()
        negativ.neg(im)
        self.StatusLabel.show()
        im.last_op = 'neg'

    def mk_noise(self):
        self.StatusLabel.hide()
        noise.noise(im)
        self.StatusLabel.show()
        im.last_op = 'noise'

    def mk_threeD(self):
        self.StatusLabel.hide()
        threeDAnagliph.makeanagliph(im)
        self.StatusLabel.show()
        im.last_op = '3d'

    def mk_bw(self):
        self.StatusLabel.hide()
        bwimg.bw(im)
        self.StatusLabel.show()
        im.last_op = 'bw'

    def back(self):
        if im.last_op == 'gray':
            grayimg.back(im)
        elif im.last_op == 'neg':
            negativ.back(im)
        elif im.last_op == '3d':
            threeDAnagliph.back(im)
        elif im.last_op == 'bw':
            bwimg.back(im)
        elif im.last_op == 'noise':
            noise.back(im)

    def turn_L(self):
        self.StatusLabel.hide()
        turns.TL(im)
        self.StatusLabel.show()

    def turn_R(self):
        self.StatusLabel.hide()
        turns.TR(im)
        self.StatusLabel.show()

    def save_changes(self):
        save.save(im)
        self.pic.close()
        if os.path.exists('img.jpg'):
            os.remove('img.jpg')

    def discard_changes(self):
        self.pic.close()
        if os.path.exists('img.jpg'):
            os.remove('img.jpg')

    def open(self):
        fname = QFileDialog.getOpenFileName(ex, 'Open file', '/home')
        if fname[0]:
            im.path = fname[0]
            shutil.copy(fname[0], im.name)


app = QApplication(sys.argv)
ex = MainWidget()
fname = QFileDialog.getOpenFileName(ex, 'Open file', '/home')
if not fname[0]:
    sys.exit()
else:
    im = Image()
    im.path = fname[0]
    shutil.copy(fname[0], im.name)
    ex.show()
sys.exit(app.exec_())

# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
import sys
import pytube
import requests
from pytube import YouTube
import re
import os
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('mainwindow.ui', self)
        self.setupUi(self)
        self.downloadButton.clicked.connect(self.download)
        self.pathButton.clicked.connect(self.choose_path)
        self.file_size = None
        self.path.setText(os.getcwd())
        self.setWindowIcon(QIcon('app.ico'))

    def download(self):
        url = self.lineEdit.text()
        try:
            options = tuple(map(lambda element: str(element), self.get_variants(url))) 
        except BaseException as exa:
            print(exa)
            QMessageBox.warning(self, "Error", "Somthing went wrong\n Please try again", QMessageBox.Ok)
        else:
            option, state = QInputDialog.getItem(self, "Варианты для скачивания: ", 
                                        "", tuple(options), 1, False)
            if state:
                if option != '--------':
                    part_itag = re.search(r'itag="[\d]+"', option)
                    itag = ""
                    for i in part_itag.group():
                        if i.isdigit():
                            itag += i
                    self.name.setText(self.get_title(url))
                    self.image.setPixmap(QPixmap(self.get_picture(url)))
                    self.download_video(url, itag)

    def choose_path(self):
        directory = QFileDialog.getExistingDirectory(self, "Choode folder", ".")
        self.path.setText(directory)

    def get_picture(self, url):
        img = requests.get(YouTube(url).thumbnail_url)
        out = open("temp.jpg", "wb")
        out.write(img.content)
        out.close()
        return "temp.jpg"

    def get_title(self, url):
        return YouTube(url).title

    def get_variants(self, url):
        try:
            yt = YouTube(url)
        except pytube.exceptions.RegexMatchError:
            QMessageBox.warning(self, 'No url detected', "No url detected", QMessageBox.Ok)
            return None
        else:
            video = yt.streams.filter(progressive=True).order_by('resolution')
            audio = yt.streams.filter(only_audio=True)
            options = list()
            for option in video:
                options.append(option)
            options.append('--------')
            for option in audio:
                options.append(option)
            return tuple(options)
        QApplication.processEvents()

    def progress_check(self, stream, chunk, remaining):
        percent = (100*(self.file_size-remaining)) // self.file_size
        self.pBar.setValue(percent)
        QApplication.processEvents()

    def download_video(self, url, itag):    
        yt = YouTube(url, on_progress_callback=self.progress_check, on_complete_callback=self.download_complete)
        downloa_video = yt.streams.get_by_itag(str(itag))
        self.file_size = downloa_video.filesize
        downloa_video.download(self.path.text())
        QApplication.processEvents()

    def download_complete(self, *args):
        QMessageBox.information(self, "Task complete", "Task was successfully complete", QMessageBox.Ok)
        self.pBar.setValue(0)
        self.image.setPixmap(QPixmap())
        self.name.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

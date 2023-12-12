# pip install pytesseract
# pip install PILLOW
# brew install tesseract

# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QPushButton,QFileDialog,QApplication,QLabel,QTextEdit)

class ImageOCRUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('打开图片', self)
        btn.move(5, 5)
        btn.clicked.connect(self.showFileDialog)

        self.img = QLabel(self)
        self.img.setScaledContents(True)
        self.img.resize(200, 400)
        self.img.move(5, 40)

        self.textarea = QTextEdit(self)
        self.textarea.resize(200, 400)
        self.textarea.move(210, 40)

        self.setGeometry(300, 300, 450, 500)
        self.setWindowTitle('图片OCR')
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.img.setPixmap(QPixmap(fname[0]))

            image = Image.open(fname[0])
            # image.show() #打开显示图片
            text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
            self.textarea.setText(text)
            with open("output.txt", "a") as f:  # 将识别出来的文字存到本地
                f.write(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageOCRUI()
    sys.exit(app.exec_())
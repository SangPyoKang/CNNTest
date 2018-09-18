from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, 
                             QTextEdit, QPushButton)
from view.QImgFrame import QImageDialog



class MyWidget01(QWidget):
    def __init__(self):
        super().__init__()
        self.myLabel()


    def myLabel(self):
        # label 생성

        xPos = 15
        yPos = 10

        title_lbl = QLabel('Title', self)
        author_lbl = QLabel('Author', self)
        review_lbl = QLabel('Review', self)
        org_viewFame_lbl = QLabel('Original', self)
        process_viewFame_lbl = QLabel('Processed', self)


        # label 위치 설정 - 절대위치
        yPos2 = yPos + 30
        yPos3 = yPos2 + 30
        yPos4 = yPos3 + 200
        yPos5 = yPos4 + 200

        title_lbl.move(xPos, yPos)
        author_lbl.move(xPos, yPos2)
        review_lbl.move(xPos, yPos3)
        org_viewFame_lbl.move(xPos,yPos4)
        # process_viewFame_lbl.move(xPos, yPos5)
        # edit

        xPos += 85
        self.title_edit = QLineEdit(self)
        self.title_edit.setGeometry(xPos, yPos, 250, 20)
        # title_edit.move(100, 10)

        self.author_edit = QLineEdit(self)
        self.author_edit.setGeometry(xPos, yPos2, 250, 20)
        # author_edit.move(100, 40)

        self.review_edit = QTextEdit(self)
        self.review_edit.setGeometry(xPos, yPos3, 250, 150)
        # review_edit.move(100, 70)

        self.imageViewFrame = QImageDialog(self)
        self.imageViewFrame.setGeometry(xPos,yPos4,200,200)
        # self.viewFrame.initBoard(bool(1))

        # self.org_viewFrame = QImageDialog(self)
        # self.org_viewFrame.setGeometry(xPos,yPos5,200,200)
        # self.org_viewFrame.initBoard(bool(0))


        # button
        # exBtn = QPushButton('test btn', self)
        # exBtn.move(267, 230)
        # exBtn.clicked.connect(self.onClickedBtn)

        # main window
        self.setGeometry(60, 60, 1000, 1000)
        self.setWindowTitle('CNN Test Program')
        self.show()

    def onClickedBtn(self):
        self.review_edit.append(self.title_edit.text() +'\n'+self.author_edit.text())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    pos = MyWidget01()
    sys.exit(app.exec_())

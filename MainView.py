from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, 
                             QTextEdit, QPushButton)


class MyWidget01(QWidget):
    def __init__(self):
        super().__init__()
        self.myLabel()

    def myLabel(self):
        # label 생성
        title_lbl = QLabel('Title', self)
        author_lbl = QLabel('Author', self)
        review_lbl = QLabel('Review', self)
        # label 위치 설정 - 절대위치
        title_lbl.move(15, 10)
        author_lbl.move(15, 40)
        review_lbl.move(15, 70)
        # edit
        self.title_edit = QLineEdit(self)
        self.title_edit.setGeometry(100, 10, 250, 20)
        # title_edit.move(100, 10)

        self.author_edit = QLineEdit(self)
        self.author_edit.setGeometry(100, 40, 250, 20)
        # author_edit.move(100, 40)

        self.review_edit = QTextEdit(self)
        self.review_edit.setGeometry(100, 70, 250, 150)
        # review_edit.move(100, 70)

        # button
        exBtn = QPushButton('test btn', self)
        exBtn.move(267, 230)
        exBtn.clicked.connect(self.onClickedBtn)

        # main window
        self.setGeometry(60, 60, 370, 270)
        self.setWindowTitle('Widgets-Label, Edit, Button')
        self.show()

    def onClickedBtn(self):
        self.review_edit.append(self.title_edit.text() +'\n'+self.author_edit.text())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    pos = MyWidget01()
    sys.exit(app.exec_())

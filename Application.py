import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit

class MyWindow(QMainWindow):
    textFilePath = ""
    presFilePath = ""

    def __init__(self):
        super().__init__()

        self.text_edit = QPlainTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # перенаправление sys.stderr в self.text_edit
        sys.stderr = self.text_edit

        self.initUI()
        
    def initUI(self):
        # Создаем главный виджет и вертикальный контейнер для кнопок
        main_widget = QWidget(self)
        vbox = QVBoxLayout()

        # Создаем первую кнопку "Browse" и поле ввода для первого файла
        self.button1 = QPushButton('Browse', self)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setReadOnly(True)

        # Создаем вторую кнопку "Browse" и поле ввода для второго файла
        self.button2 = QPushButton('Browse', self)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setReadOnly(True)

        # Добавляем кнопки и поля ввода в контейнер
        vbox.addWidget(self.button1)
        vbox.addWidget(self.lineedit1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.lineedit2)

        # Устанавливаем контейнер как главный виджет окна
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

        # Устанавливаем заголовок окна и размеры
        self.setWindowTitle('File Browser')
        self.setGeometry(100, 100, 400, 200)
        
    def on_button1_clicked(self):
        # Открываем диалог выбора файла для первого файла
        textFilePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '')
        if textFilePath:
            # Обновляем текст в поле ввода для первого файла
            self.lineedit1.setText(textFilePath)

    def on_button2_clicked(self):
        # Открываем диалог выбора файла для второго файла
        presFilePath, _ = QFileDialog.getSaveFileName(self, 'Open file', '')
        if presFilePath:
            # Обновляем текст в поле ввода для второго файла
            self.lineedit2.setText(presFilePath)

def main():
    app = QApplication(sys.argv)
    #app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
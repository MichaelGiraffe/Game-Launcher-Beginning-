import subprocess
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QScrollArea, QMenu,
                               QFileDialog)
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from AppOpener import open
from subprocess import Popen


def button_get(self) -> str:  # формат кнопок в проекте (сеттер дизайна кнопки CSS)
    return ("""
        QPushButton 
        {
            background-color: #1A1A1A; /* Темный фон */
            color: white;
            font-size: 16px;
            text-align: left;
            padding: 10px;
            border: none;
        }
        QPushButton:hover 
        {
            background-color: #292929;
        }
        QPushButton:pressed 
        {
            background-color: #0072ff;
        }
        """)


def qmenu_set(self) -> str:
    return ("""
                QMenu {
                    background-color: #1A1A1A;
                    color: white;
                    font-size: 14px;
                    border: 1px solid #444;
                }
                QMenu::item {
                    padding: 8px 20px;
                }
                QMenu::item:selected {
                    background-color: #0072ff;
                }
            """)


# border-radius: 5px;
def label_get(self) -> str:  # формат кнопок в проекте (сеттер дизайна кнопки CSS)
    return ("""
        QLabel
        {
            background-color: #333333;
            color: white;
            font-size: 16px;
            padding: 10px;
            border: 1px solid #555;
        }
        """)


# class MainWindow(object):  # наследуем QMainWindow
class UI_MainWindow(QMainWindow):  # наследуем QMainWindow
    def __init__(self):
        super().__init__()

    # база формата
    def application(self) -> None:
        self.setWindowTitle("Backrooms_CG Launcher")
        self.setGeometry(120, 40, 1444, 960)  # первые 2 параметра-смещение(вправо и вниз),ширина и высота окна
        # self.setMinimumSize(a,b)
        self.showMaximized()  # установка полноэкранного режима (выше в свернутом)

        self.setWindowIcon(QIcon("y6tpXGzUwTY.jpg"))  # Устанавливаем иконку
        self.setStyleSheet("background-color: rgba(255, 231, 194, 1);")

    # дизайн приложения в стиле CSS объектов
    def add_button_and_rectangle(self):
        widget = QWidget(self)  # Контейнер для виджетов
        self.setCentralWidget(widget)  # Делаем контейнер центральным виджетом
        # layout = QVBoxLayout()  # Размещение элементов по вертикали

        # Прямоугольник (метка с фоном)
        rectangle = QLabel(widget)
        rectangle.setFixedSize(200, 100)  # Размер прямоугольника
        rectangle.setStyleSheet("background-color: blue;")  # Цвет прямоугольника

        # Кнопка
        button = QPushButton("Нажми меня", widget)
        button.setFixedSize(120, 40)  # Размер кнопки
        button.move(100, 50)

        # Кастомный дизайн лаунчера из виджетов

        # верхний label
        topLabel = QLabel(widget)
        topLabel.setStyleSheet(label_get(self))
        topLabel.setGeometry(0, 0, 2000, 80)

        # левый label
        leftLabel = QLabel(widget)
        leftLabel.setStyleSheet(label_get(self))
        leftLabel.setGeometry(0, 79, 200, 1024)

        # нижний label
        downLabel = QLabel(widget)
        downLabel.setStyleSheet(label_get(self))
        downLabel.setStyleSheet("background-color: #999999")
        downLabel.setGeometry(0, 848, 2500, 170)

        downerLabel = QLabel(widget)
        downerLabel.setStyleSheet(label_get(self))
        downerLabel.setStyleSheet("background-color: #ffffff")
        downerLabel.setGeometry(0, 933, 2500, 85)


        # усвоить еще раз
        # кнопка аккаунта
        button1 = QPushButton("Аккаунт стим\n(в разработке)", widget)
        (button1.setStyleSheet(button_get(self)))
        button1.setGeometry(0, 0, 180, 80)
        # контекстное меню для кнопки аккаунта
        account_menu = QMenu(self)
        account_menu.setStyleSheet(qmenu_set(self))  # Применяем стиль к QMenu
        account_menu.addAction("Управление профилем")
        # account_menu.addSeparator() - добавляет разделитель
        account_menu.addAction("Выход")
        # Привязываем меню к кнопке
        button1.setMenu(account_menu)
        # усвоить еще раз


        # кнопка "игра/играть -думайте сами"
        self.play_button = QPushButton("игра", widget)
        (self.play_button.setStyleSheet(button_get(self)))
        self.play_button.setGeometry(180, 0, 180, 80)

        # pushbutton "версия игры(лаунчера)+открывает значится хрень со списками уровней (потом изображу)"
        version_button = QPushButton("version: alfa 0.01", widget)
        (version_button.setStyleSheet(button_get(self)))
        version_button.setGeometry(360, 0, 180, 80)

        # скины (то ли просто как в расте на рандом всем выдавать, то ли...)
        # skins_button = QPushButton("version: alfa 0.01", widget)
        # (skins_button.setStyleSheet(self.button_get()))
        # skins_button.setGeometry(540, 0, 180, 80)

        # pushbutton "версия игры(лаунчера)+открывает значится хрень со списками уровней (потом изображу)"
        changelog_button = QPushButton("changelog", widget)
        (changelog_button.setStyleSheet(button_get(self)))
        changelog_button.setGeometry(540, 0, 180, 80)

        # отсылка к функционалу
        self.play_func()

        # демка выбора файла (сделать функционал к другой кнопке)
        self.Hbutton = QPushButton("what", widget)
        self.Hbutton.clicked.connect(self.BrowseFunc)
        button.setStyleSheet(button_get(self))
        self.Hbutton.setGeometry(600, 600, 500, 500)

        # Добавляем в макет
        # layout.addWidget(button)
        # layout.addWidget(rectangle)

        # тут дальше эксперимент с расширяемостью
        # widget.setLayout(layout)  # Устанавливаем макет в контейнер
        # self.setCentralWidget(widget)  # Делаем контейнер центральным виджетом

    # функция запуска приложения
    def play_func(self):
        self.play_button.clicked.connect(lambda: subprocess.Popen(r"D:\ProgramsNecesary\Steam\steam.exe"))

    # основные поля
    # функция обзора файлов ()
    def BrowseFunc(self):  # указать ссылку (пример button)
        try:
            file_path = QFileDialog.getExistingDirectory(self, "Выберите местоположение ресурсов игры")
            if file_path:
                self.Hbutton.setText(file_path)
        except:
            raise Exception("все таки поломалась")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = UI_MainWindow()
    ui.application()
    ui.add_button_and_rectangle()
    ui.show()
    sys.exit(app.exec())

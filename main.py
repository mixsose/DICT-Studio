import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QPushButton,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Titre de la fenetre
        self.setWindowTitle("DICT - Dual-In-Line Integrated Circuit Tester")

        #Crée la barre de menu
        menu = self.menuBar()

        #edit la barre de menu en haut
        file_menu = menu.addMenu("&File")
        file_menu = menu.addSeparator()
        file_menu = menu.addMenu("&Edit")
        file_menu = menu.addSeparator()
        file_menu = menu.addMenu("&View")

        #Crée la barre d'outils a gauche
        toolbar = QToolBar("My main toolbar")
        toolbar.setMovable(False)
        toolbar.setStyleSheet("background-color: #21252B;") #On decrit la fenetre en css
        toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        toolbar.setIconSize(QSize(40, 40))
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        #Ajoute le bouton editeur de code
        Logo_EditeurDeCode = QPixmap("assets/logo_editeur-de-code.png").scaled(
            54, 54, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        button_EditeurDeCode = QAction(QIcon(Logo_EditeurDeCode), "Éditeur de code", self)
        toolbar.addAction(button_EditeurDeCode)

        toolbar.addSeparator()

        #Ajoute le bouton Configurer le prober
        Logo_ConfigurationProber = QPixmap("assets/logo_configuration-prober.png").scaled(
            54, 54, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        button_ConfigurationProber = QAction(QIcon(Logo_ConfigurationProber), "Éditeur de code", self)
        toolbar.addAction(button_ConfigurationProber)

        toolbar.addSeparator()

        #Ajoute le bouton Configurer le prober
        Logo_Run = QPixmap("assets/logo_run.png").scaled(
            54, 54, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        button_Run = QAction(QIcon(Logo_Run), "Éditeur de code", self)
        toolbar.addAction(button_Run)

        self.setStatusBar(QStatusBar(self))





app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()

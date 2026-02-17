import os
from PySide6.QtCore import Qt
import sys
from PySide6.QtWidgets import QApplication
from src.views.main_window import MainWindow

def main():
    # instancia de la aplicacion
    app = QApplication(sys.argv)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    #creamos y mostramos la ventana
    window = MainWindow()
    window.show()

    #inicia el bucle de eventos
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Fiscal Pro")
        self.resize(800, 600)
        
        # 1. Cargar el archivo .ui dinámicamente
        loader = QUiLoader()
        ui_file_path = os.path.join(os.path.dirname(__file__), "main_view.ui")
        ui_file = QFile(ui_file_path)
        
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
            
        # 2. Acceder a los elementos del Designer por su objectName
        self.ui.btn_dashboard.clicked.connect(self.ir_a_dashboard)
        self.ui.btn_nuevo_ticket.clicked.connect(self.ir_a_formulario)

        self.ui.btn_enviar_datos.clicked.connect(self.procesar_y_navegar)
        self.ui.btn_volver.clicked.connect(self.volver_atras)
    def ir_a_dashboard(self):
        print("Cambiando a Dashboard...")
        # Aquí puedes usar lógica similar a la de limpiar_vista() que hicimos antes

    def ir_a_formulario(self):
        print("Abriendo Formulario de Facturación...")

    def procesar_y_navegar(self):
        # A. Capturamos el valor del LineEdit (como un input de HTML)
        valor_escrito = self.ui.input_nombre.text()

        if valor_escrito.strip() == "":
            self.ui.label_bienvenida.setText("Por favor, escribe un nombre")
        else:
            # B. "Mandamos" el valor a la otra vista (el Label de la página 2)
            self.ui.label_bienvenida.setText(f", {valor_escrito}!")
            
            # C. Cambiamos la página del StackedWidget
            # El índice 1 es la segunda página que creaste
            self.ui.stackedWidget.setCurrentIndex(1)

    def volver_atras(self):
        # Simplemente regresamos al índice 0
        self.ui.stackedWidget.setCurrentIndex(0)

    # En src/views/main_window.py

def ir_a_dashboard(self):
    # El índice 0 suele ser la primera página
    self.ui.stackedWidget.setCurrentIndex(0)

def ir_a_formulario(self):
    # El índice 1 es la segunda página
    self.ui.stackedWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
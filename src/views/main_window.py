import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFrame, 
                             QHBoxLayout, QVBoxLayout, QPushButton, 
                             QStackedWidget, QLabel, QLineEdit)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana Principal
        self.setWindowTitle("Sistema Fiscal Pro - Pure Python")
        self.resize(800, 600)
        self.setMinimumSize(700, 500)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 2. Creación del Sidebar
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setObjectName("sidebar")
        self.sidebar_frame.setFixedWidth(220)
        
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.sidebar_layout.setSpacing(20)
        self.sidebar_layout.setContentsMargins(20, 50, 20, 20)

        # --- CORRECCIÓN: Crear los botones ANTES de agregarlos al layout ---
        self.btn_dashboard = QPushButton("Escritorio")
        self.btn_nuevo_ticket = QPushButton("Nuevo ticket")
        self.btn_tema_oscuro = QPushButton("Tema Oscuro")
        self.btn_tema_claro = QPushButton("Tema Claro")

        # Ahora sí los agregamos
        self.sidebar_layout.addWidget(self.btn_dashboard)
        self.sidebar_layout.addWidget(self.btn_nuevo_ticket)
        self.sidebar_layout.addStretch() 
        self.sidebar_layout.addWidget(self.btn_tema_oscuro)
        self.sidebar_layout.addWidget(self.btn_tema_claro)

        # 3. Área de Contenido
        self.content_frame = QFrame()
        self.content_layout = QVBoxLayout(self.content_frame)
        self.stacked_widget = QStackedWidget()
        self.content_layout.addWidget(self.stacked_widget)

        # PÁGINA 1
        self.page_1 = QWidget()
        self.layout_p1 = QVBoxLayout(self.page_1)
        self.layout_p1.setAlignment(Qt.AlignCenter)
        self.label_p1 = QLabel("Página 1 - Dashboard")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Escribe tu nombre aquí...")
        self.input_nombre.setFixedWidth(250)
        self.btn_enviar_datos = QPushButton("Enviar datos")
        self.layout_p1.addWidget(self.label_p1)
        self.layout_p1.addWidget(self.input_nombre)
        self.layout_p1.addWidget(self.btn_enviar_datos)

        # PÁGINA 2
        self.page_2 = QWidget()
        self.layout_p2 = QVBoxLayout(self.page_2)
        self.layout_p2.setAlignment(Qt.AlignCenter)
        self.label_p2 = QLabel("Página 2 - Resultados")
        self.label_bienvenida = QLabel("Esperando datos...")
        self.btn_volver = QPushButton("Volver")
        self.layout_p2.addWidget(self.label_p2)
        self.layout_p2.addWidget(self.label_bienvenida)
        self.layout_p2.addWidget(self.btn_volver)

        self.stacked_widget.addWidget(self.page_1)
        self.stacked_widget.addWidget(self.page_2)

        self.main_layout.addWidget(self.sidebar_frame)
        self.main_layout.addWidget(self.content_frame)

        # 4. Conexiones
        self.btn_dashboard.clicked.connect(self.ir_a_dashboard)
        self.btn_nuevo_ticket.clicked.connect(self.ir_a_formulario)
        self.btn_enviar_datos.clicked.connect(self.procesar_y_navegar)
        self.btn_volver.clicked.connect(self.volver_atras)
        self.btn_tema_oscuro.clicked.connect(lambda: self.cambiar_tema("dark"))
        self.btn_tema_claro.clicked.connect(lambda: self.cambiar_tema("light"))

        # Iniciar tema
        self.cambiar_tema("dark")

    def ir_a_dashboard(self):
        self.stacked_widget.setCurrentIndex(0)

    def ir_a_formulario(self):
        self.stacked_widget.setCurrentIndex(1)

    def procesar_y_navegar(self):
        texto = self.input_nombre.text()
        self.label_bienvenida.setText(f"¡Hola, {texto}!" if texto.strip() else "¡Por favor escribe algo!")
        self.stacked_widget.setCurrentIndex(1)

    def volver_atras(self):
        self.stacked_widget.setCurrentIndex(0)

    def cambiar_tema(self, tema):
        base_path = os.path.dirname(__file__)
        main_qss_path = os.path.join(base_path, "..", "styles", "main.qss")
        file_path = os.path.join(base_path, "..", "styles", f"{tema}.qss")
        
        completo_qss = ""
        try:
            if os.path.exists(main_qss_path):
                with open(main_qss_path, "r") as f:
                    completo_qss += f.read()
            
            # CORRECCIÓN: Usar la variable correcta 'file_path'
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    completo_qss += "\n" + f.read()
            
            self.setStyleSheet(completo_qss)
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
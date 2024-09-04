import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon

app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("Aplicación de Tareas")
widget.setGeometry(300, 300, 400, 400)

layout = QVBoxLayout()
widget.setLayout(layout)

layout_entrada = QHBoxLayout()
entrada_tarea = QLineEdit()
entrada_tarea.setPlaceholderText("Introduce una nueva tarea...")
boton_agregar = QPushButton("Agregar Tarea")

icono_agregar = QIcon.fromTheme("list-add")
boton_agregar.setIcon(icono_agregar)

layout_entrada.addWidget(entrada_tarea)
layout_entrada.addWidget(boton_agregar)

lista_tareas = QListWidget()

boton_eliminar = QPushButton("Eliminar Tarea Seleccionada")

icono_eliminar = QIcon.fromTheme("edit-delete")
boton_eliminar.setIcon(icono_eliminar)

layout.addLayout(layout_entrada)
layout.addWidget(lista_tareas)
layout.addWidget(boton_eliminar)

def agregar_tarea():
    texto_tarea = entrada_tarea.text()
    if texto_tarea:
        item = QListWidgetItem(texto_tarea)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        lista_tareas.addItem(item)
        entrada_tarea.clear()

def eliminar_tarea():
    for item in lista_tareas.selectedItems():
        lista_tareas.takeItem(lista_tareas.row(item))

boton_agregar.clicked.connect(agregar_tarea)
boton_eliminar.clicked.connect(eliminar_tarea)
widget.show()
sys.exit(app.exec())

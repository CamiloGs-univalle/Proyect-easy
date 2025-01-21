# vista/vista_calculadora.py

import tkinter as tk
from tkinter import messagebox

class VistaCalculadora(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Calculadora Interactiva")
        self.geometry("400x600")
        self.config(bg="#2C3E50")  # Fondo oscuro elegante

        self.resultado_var = tk.StringVar()
        self.crear_interfaz()
        self.configurar_eventos_teclado()

    def crear_interfaz(self):
        # Marco para el resultado
        marco_resultado = tk.Frame(self, bg="#34495E", bd=10, relief="ridge")
        marco_resultado.pack(pady=20, padx=20, fill="x")

        # Campo de texto para el resultado
        resultado_entry = tk.Entry(
            marco_resultado,
            textvariable=self.resultado_var,
            font=("Consolas", 24),
            bg="#ECF0F1",
            fg="#2C3E50",
            justify="right",
            bd=0,
            relief="flat",
            state="readonly",
        )
        resultado_entry.pack(fill="x", ipady=15)

        # Marco para los botones
        marco_botones = tk.Frame(self, bg="#2C3E50")
        marco_botones.pack(pady=20)

        # Configuración de botones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("←", 5, 0),  # Nuevo botón para borrar
        ]

        for (texto, fila, columna) in botones:
            # Estilo de los botones
            boton = tk.Button(
                marco_botones,
                text=texto,
                font=("Consolas", 18, "bold"),
                bg="#16A085" if texto.isdigit() else "#E74C3C",
                fg="white",
                activebackground="#1ABC9C" if texto.isdigit() else "#C0392B",
                activeforeground="white",
                bd=0,
                width=5,
                height=2,
                command=lambda t=texto: self.controlador.procesar_boton(t),
            )
            boton.grid(row=fila, column=columna, padx=5, pady=5)

    def configurar_eventos_teclado(self):
        """Vincula las teclas del teclado con los botones de la calculadora."""
        for tecla in "0123456789+-*/=":
            self.bind(tecla, self.evento_teclado)

        self.bind("<Return>", lambda event: self.controlador.procesar_boton("="))  # Enter como igual
        self.bind("<BackSpace>", lambda event: self.controlador.procesar_boton("←"))  # Borrar último carácter
        self.bind("c", lambda event: self.controlador.procesar_boton("C"))  # Tecla 'C' para limpiar

    def evento_teclado(self, event):
        """Maneja los eventos de las teclas presionadas."""
        self.controlador.procesar_boton(event.char)

    def actualizar_resultado(self, texto):
        self.resultado_var.set(texto)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

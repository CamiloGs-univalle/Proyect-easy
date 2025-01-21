class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.expresion = ""  # Expresión acumulada
        self.es_resultado = False  # Indica si el contenido mostrado es un resultado

    def procesar_boton(self, texto):
        if texto.isdigit():
            # Si hay un resultado previo, reiniciar la expresión
            if self.es_resultado:
                self.expresion = texto  # Reiniciar con el nuevo número
                self.es_resultado = False
            else:
                self.expresion += texto  # Agregar el número
            self.vista.actualizar_resultado(self.expresion)

        elif texto in "+-*/":
            # Si hay un resultado previo, continuar desde él
            if self.es_resultado:
                self.es_resultado = False
                self.expresion += texto  # Continuar con el operador
            else:
                self.expresion += texto  # Agregar el operador
            self.vista.actualizar_resultado(self.expresion)

        elif texto == "=":
            try:
                # Evaluar la expresión
                resultado = eval(self.expresion)
                self.vista.actualizar_resultado(str(resultado))
                self.expresion = str(resultado)  # Usar el resultado como nueva base
                self.es_resultado = True
            except ZeroDivisionError:
                self.vista.mostrar_error("Error: División por cero")
                self.expresion = ""
                self.es_resultado = False
            except Exception:
                self.vista.mostrar_error("Error: Expresión inválida")
                self.expresion = ""
                self.es_resultado = False

        elif texto == "C":
            # Limpiar todo
            self.expresion = ""
            self.es_resultado = False
            self.vista.actualizar_resultado("")

        elif texto == "←":
            # Borrar el último carácter solo si no es resultado
            if not self.es_resultado:
                self.expresion = self.expresion[:-1]
                self.vista.actualizar_resultado(self.expresion)

# main.py
from MVC.Model.logic_Calculadora import ModeloCalculadora
from MVC.Controlador.contro_Calculadora import ControladorCalculadora
from MVC.Vist.Vist_Calculadora import VistaCalculadora


if __name__ == "__main__":
    modelo = ModeloCalculadora()
    vista = VistaCalculadora(None)
    controlador = ControladorCalculadora(modelo, vista)
    vista.controlador = controlador
    vista.mainloop()

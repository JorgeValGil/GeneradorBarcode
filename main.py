import events
import sys
import var
from ventana import *


class Main(QtWidgets.QMainWindow):
    """Clase principal del programa"""

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        events.Eventos.cargar_tipos_barcodes(self)
        var.ui.pushButton_salir.clicked.connect(events.Eventos.close)
        var.ui.pushButton_limpiar.clicked.connect(events.Eventos.clean_data)
        var.ui.pushButton_aceptar.clicked.connect(events.Eventos.code)

        var.ui.statusbar.addPermanentWidget(var.ui.labelstatusbar, 1)


if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

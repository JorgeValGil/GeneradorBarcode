from datetime import datetime
from PyQt5 import QtWidgets
import sys
import var
from barcode import EAN8
from barcode import EAN13
from barcode import EAN14
from barcode import ISBN13
from barcode import ISBN10
from barcode import UPCA
from barcode import errors


class Eventos:

    def close(self):
        sys.exit()

    def cargar_tipos_barcodes(self):
        tipos = ['EAN-13', 'EAN-8', 'EAN14', 'UPC-A', 'ISBN-13', 'ISBN-10']
        var.tiposbarcode = tipos
        for i in tipos:
            var.ui.comboBox_tipos.addItem(i)

    def code(self):
        code = var.ui.lineEdit_texto.text()
        if code != "":
            typecode = var.ui.comboBox_tipos.currentIndex()
            Eventos.code_type(self, code, typecode)
        else:
            Eventos.no_text(self)

    def code_type(self, code, typecode):
        if typecode == 0:
            Eventos.code_ean13(self, code)
        if typecode == 1:
            Eventos.code_ean8(self, code)
        if typecode == 2:
            Eventos.code_ean14(self, code)
        if typecode == 3:
            Eventos.code_upca(self, code)
        if typecode == 4:
            Eventos.code_isbn13(self, code)
        if typecode == 5:
            Eventos.code_isbn10(self, code)

    def code_ean13(self, code):
        try:
            my_code = EAN13(code)
            Eventos.process(self, my_code)
        except errors.IllegalCharacterError:
            var.ui.labelstatusbar.setText('EAN solo puede contener números.')
        except errors.NumberOfDigitsError:
            var.ui.labelstatusbar.setText('EAN13 debe contener 12 dígitos.')

    def code_ean8(self, code):
        try:
            my_code = EAN8(code)
            Eventos.process(self, my_code)
        except errors.IllegalCharacterError:
            var.ui.labelstatusbar.setText('EAN solo puede contener números.')
        except errors.NumberOfDigitsError:
            var.ui.labelstatusbar.setText('EAN13 debe contener 7 dígitos.')

    def code_ean14(self, code):
        try:
            my_code = EAN14(code)
            Eventos.process(self, my_code)
        except errors.IllegalCharacterError:
            var.ui.labelstatusbar.setText('EAN solo puede contener números.')
        except errors.NumberOfDigitsError:
            var.ui.labelstatusbar.setText('EAN13 debe contener 14 dígitos.')

    def code_upca(self, code):
        try:
            my_code = UPCA(code)
            Eventos.process(self, my_code)
        except errors.IllegalCharacterError:
            var.ui.labelstatusbar.setText('UPC solo puede contener números.')
        except errors.NumberOfDigitsError:
            var.ui.labelstatusbar.setText('UPC debe tener 11 dígitos.')

    def code_isbn13(self, code):
        try:
            my_code = ISBN13(code)
            Eventos.process(self, my_code)
        except errors.WrongCountryCodeError:
            var.ui.labelstatusbar.setText('ISBN debe comenzar por 978 o 979.')
        except errors.BarcodeError:
            var.ui.labelstatusbar.setText('ISBN debe comenzar por 97910 o 97911.')

    def code_isbn10(self, code):
        try:
            my_code = ISBN10(code)
            Eventos.process(self, my_code)
        except errors.WrongCountryCodeError:
            var.ui.labelstatusbar.setText('ISBN debe comenzar por 978 o 979.')
        except errors.BarcodeError:
            var.ui.labelstatusbar.setText('ISBN debe comenzar por 97910 o 97911.')

    def clean_data(self):
        var.ui.lineEdit_texto.setText("")
        var.ui.comboBox_tipos.setCurrentIndex(0)

    def process(self, my_code):
        ventana_carpeta = QtWidgets.QFileDialog
        carpeta_destino = ventana_carpeta.getExistingDirectory(None, 'Selecciona la carpeta de destino')
        if ventana_carpeta.Accepted and carpeta_destino != '':
            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
            nombre = carpeta_destino + '/' + dt_string
            my_code.save(nombre)
            var.ui.labelstatusbar.setText('GENERADA IMAGEN  ' + dt_string)

    def no_text(self):
        var.ui.labelstatusbar.setText('DEBES INTRODUCIR TEXTO PARA GENERAR EL CÓDIGO')

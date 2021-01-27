from PyQt5 import uic, QtWidgets


def encrypt():
    message = form.textEdit.toPlainText()
    key = form.lineEdit.text()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _key = len(key)
    encrypt = ''
    for c in message:
        position = alphabet.find(c)
        new_position = (position + _key) %26
        encrypt += alphabet[new_position]
    form.textEdit_2.setPlainText(encrypt)


def decrypt():
    message = form.textEdit.toPlainText()
    key = form.lineEdit.text()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _key = len(key)
    encrypt = ''
    for c in message:
        position = alphabet.find(c)
        new_position = (position - _key) %26
        encrypt += alphabet[new_position]
    form.textEdit_2.setPlainText(encrypt.replace('z', ' '))


app = QtWidgets.QApplication([])
form = uic.loadUi('prismacrypt.ui')
form.pushButton.clicked.connect(encrypt)
form.pushButton_2.clicked.connect(decrypt)

form.show()
app.exec()
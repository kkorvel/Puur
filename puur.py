import signal
import sys
#from PyMata.pymata import PyMata
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QTextEdit
app = QApplication([])

mainwindow = QMainWindow()
mainwindow.setWindowTitle("Puuri koordinaadid")

vbox = QVBoxLayout()
vbox.addStretch(1)

textedit = QTextEdit("box 1")
textedit2 = QTextEdit("box 2")
textedit3 = QTextEdit("box 3")


vbox.addWidget(textedit)
vbox.addWidget(textedit2)
vbox.addWidget(textedit3)
# This is some silly Qt-ism
container = QWidget()
container.setLayout(vbox)
mainwindow.setCentralWidget(container)
mainwindow.show()


sys.exit(app.exec_()) # This is basically infinite loop here, it blocks everything else!

import signal
import sys
#from PyMata.pymata import PyMata
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QTextEdit
app = QApplication([])
button_convert = QPushButton("Convert order")
mainwindow = QMainWindow()
mainwindow.setWindowTitle("Puuri koordinaadid")

vbox = QVBoxLayout()
vbox.addStretch(1)

textedit = QTextEdit("First part")
textedit2 = QTextEdit("Second part")
textedit3 = QTextEdit("Result")

vbox.addWidget(textedit)
vbox.addWidget(textedit2)
vbox.addWidget(textedit3)
vbox.addWidget(button_convert)

# This is some silly Qt-ism
container = QWidget()
container.setLayout(vbox)
mainwindow.setCentralWidget(container)
mainwindow.show()


def convert_handler():
	value = textedit2.toPlainText()
	#print(value)
	sendList = value.split()
	sendList = [sendList[i] + ' ' + sendList[i+1] for i in range(0, len(sendList), 2)]
	#print(sendList)
	reversedList = sendList[::-1]
	print(reversedList)
	#correctList = ' '.join(reversedList)
	#print(correctList)
	
    


button_convert.clicked.connect(convert_handler)


sys.exit(app.exec_()) # This is basically infinite loop here, it blocks everything else!

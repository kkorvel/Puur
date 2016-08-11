import signal
import sys
#from PyMata.pymata import PyMata
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QTextEdit
app = QApplication([])
button_convert = QPushButton("Convert order")
#button_result = QPushButton("See my magical result!")
mainwindow = QMainWindow()
mainwindow.resize(230,400)
mainwindow.setWindowTitle("Puuri abi")

vbox = QVBoxLayout()
vbox.addStretch(1)

textedit = QTextEdit("First part")
textedit2 = QTextEdit("Second part")
textedit3 = QTextEdit(" ")

vbox.addWidget(textedit)
vbox.addWidget(textedit2)
vbox.addWidget(textedit3)
vbox.addWidget(button_convert)
#vbox.addWidget(button_result)

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
	#print(reversedList)
	secondpartvalue = ' '.join(reversedList)
	#print(secondpartvalue)
	firstpartvalue = textedit.toPlainText()
	#print(firstpartvalue)
	finalresult = firstpartvalue + ' ' + secondpartvalue
	print (finalresult)
	resultstring = textedit3.insertPlainText(finalresult)


	
#def result_handler():
	#firstpartvalue = textedit.toPlainText()
	#print (firstpartvalue)
	#finalresult = firstpartvalue + reversedList
	#print (finalresult)
	
	
    


button_convert.clicked.connect(convert_handler)
#button_result.clicked.connect(result_handler)


sys.exit(app.exec_()) # This is basically infinite loop here, it blocks everything else!

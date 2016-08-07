import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        firstpart = QtGui.QLabel('First part')
        secondpart = QtGui.QLabel('Second part')
        correctorder = QtGui.QLabel('Correct order')

        firstEdit = QtGui.QTextEdit()
        secondEdit = QtGui.QTextEdit()
        orderEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(firstpart, 1, 0)
        grid.addWidget(firstEdit, 1, 1)

        grid.addWidget(secondpart, 2, 0)
        grid.addWidget(secondEdit, 2, 1)

        grid.addWidget(correctorder, 3, 0)
        grid.addWidget(orderEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Puuri koordinaadid!')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

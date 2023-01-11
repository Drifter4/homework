from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array

def Affiche():
    ch1 = window.a.text()
    ch2 = window.b.text()
    R = ""
    
    for i in range(len(ch1)):
        if ch2.find(ch1[i]) != -1:
            R = R + ch1[i] + ","
    
    window.r.setText(R[:len(R)-1])
    print(ch1)
    print(ch2)
    print(R)


app = QApplication([])
window = loadUi("ex3.ui")
window.show()
window.c.clicked.connect(Affiche)
app.exec_()
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array


def Affiche():
    num1 = int(window.a.text())
    num2 = int(window.b.text())
    div1 = ""
    div2 = ""
    div = ""
    
    for i in range(1,num1+1):
        if(num1 % i == 0):
            div1 = div1 + str(i) + ","
            
    for i in range(1,num2+1):
        if(num2 % i == 0):
            div2 = div2 + str(i) + ","
            
    for i in range(len(div1)):
        if div1[i] != "," and div2.find(div1[i]) != -1:
            div = div + div1[i] + ","
    
    window.r.setText(div[:len(div)-1])
    print(div1)
    print(div2)
    print(div)
    
app = QApplication([])
window = loadUi("ex2.ui")
window.show()
window.c.clicked.connect(Affiche)
app.exec_()
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Verif():
    P = int(window.P.text())
    R = window.R
    if (P < 0):
        R.setText("donnez un nombre > 0")
        R.setStyleSheet("color: rgb(0,0,0)")
    elif Test(P):
        R.setText("c super-pairplus")
        R.setStyleSheet("color: rgb(0,0,0)")
    elif Test(P) == False:
        R.setText("c pas super-pairplus")
        R.setStyleSheet("color: rgb(0,0,0)")
        
def Test(N):
    ok0 = True
    ok1 = True
    ok2 = True
    i = 0
    j = 2
    strN = str(N)
    #verif de N: pair?
    if((N % 2) != 0):
        ok0 = False
    #verif des entiers pairs
    while i < len(str(N)) and ok1 == True:
        if ((int(strN[i]) % 2) == 0):
            i += 1
        else:
            ok1 = False
        
    #verif diviseurs pairs
    while j < N and ok2 == True:
        if(N % j == 0):
            if(j % 2 == 0):
                j += 1
            else:
                ok2 = False
            
    return ok0 and ok1 and ok2

app = QApplication([])
window = loadUi("ex1.ui")
window.show()
window.V.clicked.connect(Verif)
app.exec_()
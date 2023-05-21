from PyQt5.QtWidgets import*
import pygame
pygame.init()
app = QApplication([])
okno = QWidget()

okno.setWindowTitle('soundpad')
okno.resize(600,600)


but1 = QPushButton(okno)
but1.move(40,40)
but1.resize(70,100)

but2 = QPushButton(okno)
but2.move(130,40)
but2.resize(70,100)

but3 = QPushButton(okno)
but3.move(220,40)
but3.resize(70,100)

but4 = QPushButton(okno)
but4.move(310,40)
but4.resize(70,100)

but5 = QPushButton(okno)
but5.move(400,40)
but5.resize(70,100)

but6 = QPushButton(okno)
but6.move(490,40)
but6.resize(70,100)

but7 = QPushButton(okno)
but7.move(40,180)
but7.resize(70,100)

but8 = QPushButton(okno)
but8.move(130,180)
but8.resize(70,100)

but9 = QPushButton(okno)
but9.move(220,180)
but9.resize(70,100)

but10 = QPushButton(okno)
but10.move(310,180)
but10.resize(70,100)

but11 = QPushButton(okno)
but11.move(400,180)
but11.resize(70,100)

but12 = QPushButton(okno)
but12.move(490,180)
but12.resize(70,100)

but13 = QPushButton(okno)
but13.move(40,320)
but13.resize(70,100)

but14 = QPushButton(okno)
but14.move(130,320)
but14.resize(70,100)

but15= QPushButton(okno)
but15.move(220,320)
but15.resize(70,100)

but16= QPushButton(okno)
but16.move(310,320)
but16.resize(70,100)

but17= QPushButton(okno)
but17.move(400,320)
but17.resize(70,100)

but18= QPushButton(okno)
but18.move(490,320)
but18.resize(70,100)

but19= QPushButton(okno)
but19.move(40,460)
but19.resize(70,100)

but20= QPushButton(okno)
but20.move(130,460)
but20.resize(70,100)

but21= QPushButton(okno)
but21.move(220,460)
but21.resize(70,100)

but22 = QPushButton(okno)
but22.move(310,460)
but22.resize(70,100)

but23 = QPushButton(okno)
but23.move(400,460)
but23.resize(70,100)

but24 = QPushButton(okno)
but24.move(490,460)
but24.resize(70,100)

sound1 = pygame.mixer.Sound('bolotnyie1.wav')
def tuk():
    sound1.play()
but1.clicked.connect(tuk)

sound2 = pygame.mixer.Sound('bryanchaniebanki2.wav')
def tuk():
    sound2.play()
but2.clicked.connect(tuk)

sound3 = pygame.mixer.Sound('dengi3.wav')
def tuk():
    sound3.play()
but3.clicked.connect(tuk)

sound4 = pygame.mixer.Sound('derevyashku4.wav')
def tuk():
    sound4.play()
but4.clicked.connect(tuk)

sound5 = pygame.mixer.Sound('kryishki5.wav')
def tuk():
    sound5.play()
but5.clicked.connect(tuk)

sound6 = pygame.mixer.Sound('kubik6.wav')
def tuk():
    sound6.play()
but6.clicked.connect(tuk)

sound7 = pygame.mixer.Sound('medlennyiy7.wav')
def tuk():
    sound7.play()
but7.clicked.connect(tuk)

sound8 = pygame.mixer.Sound('monetka8.wav')
def tuk():
    sound8.play()
but8.clicked.connect(tuk)

sound9 = pygame.mixer.Sound('musor9.wav')
def tuk():
    sound9.play()
but9.clicked.connect(tuk)

sound10 = pygame.mixer.Sound('otkryitiezonta10.wav')
def tuk():
    sound10.play()
but10.clicked.connect(tuk)

sound11 = pygame.mixer.Sound('otkryitiya11.wav')
def tuk():
    sound11.play()
but11.clicked.connect(tuk)

sound12 = pygame.mixer.Sound('podzontom12.wav')
def tuk():
    sound12.play()
but12.clicked.connect(tuk)

sound13 = pygame.mixer.Sound('portfel13.wav')
def tuk():
    sound13.play()
but13.clicked.connect(tuk)

sound14 = pygame.mixer.Sound('posuda14.wav')
def tuk():
    sound14.play()
but14.clicked.connect(tuk)

sound15 = pygame.mixer.Sound('razbitogo15.wav')
def tuk():
    sound15.play()
but15.clicked.connect(tuk)

sound16 = pygame.mixer.Sound('skrip16.wav')
def tuk():
    sound16.play()
but16.clicked.connect(tuk)

sound17 = pygame.mixer.Sound('stopkamonet17.wav')
def tuk():
    sound17.play()
but17.clicked.connect(tuk)

sound18 = pygame.mixer.Sound('stuk18.wav')
def tuk():
    sound18.play()
but18.clicked.connect(tuk)

sound19 = pygame.mixer.Sound('vyibili19.wav')
def tuk():
    sound19.play()
but19.clicked.connect(tuk)

sound20 = pygame.mixer.Sound('zvukzvonka20.wav')
def tuk():
    sound20.play()
but20.clicked.connect(tuk)
sound21 = pygame.mixer.Sound('provodka21.wav')
def tuk():
    sound21.play()
but21.clicked.connect(tuk)

sound22 = pygame.mixer.Sound('lazer22.wav')
def tuk():
    sound22.play()
but22.clicked.connect(tuk)

sound23 = pygame.mixer.Sound('zamah23.wav')
def tuk():
    sound23.play()
but23.clicked.connect(tuk)

sound24 = pygame.mixer.Sound('piu24.wav')
def tuk():
    sound24.play()
but24.clicked.connect(tuk)

but1.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but2.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but3.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but4.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but5.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but6.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but7.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but8.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but9.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but10.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but11.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but12.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but13.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but14.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but15.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but16.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but17.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but18.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but19.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but20.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but21.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but22.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but23.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but24.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')


okno.setStyleSheet('''QWidget{background-image: url('4fon.jpg');
}''')
okno.show()
app.exec_()
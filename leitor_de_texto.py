from gtts import gTTS
from playsound import playsound
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def ler_texto():

    texto_escrito = le.text()
    audio = 'audio.mp3'
    language = 'pt-br'

    sp = gTTS(
        text=texto_escrito,
        lang=language
    )

    sp.save(audio)
    playsound(audio)


app = QApplication(sys.argv)

wind = QWidget()
wind.resize(800, 600)
wind.setStyleSheet('background-color:rgb(63, 63, 63)')

bt = QPushButton('mudar texto', wind)
bt.setGeometry(100, 50, 100, 50)
bt.setStyleSheet('background-color: rgb(79, 255, 25)')
bt.clicked.connect(ler_texto)


le = QLineEdit('', wind)
le.setGeometry(400, 50, 200, 40)


wind.show()

app.exec()

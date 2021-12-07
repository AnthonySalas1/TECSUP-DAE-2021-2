import pyfirmata

##puerto = "\.\COM3" #Puerto COM de emulación en USB
pin = (2) #PIN donde va conectado el LED
pin = (3) #PIN donde va conectado el LED
pin = (4) #PIN donde va conectado el LED
pin = (5) #PIN donde va conectado el LED
##board = pyfirmata.Arduino(puerto)

def blueOn():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Encendiendo AZUL")
def redOn():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Encendiendo ROJO")
def greenOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)
    print("Encendiendo VERDE")
def yellowOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)
    print("Encendiendo AMARILLO")
def allOff():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Apagando todas")
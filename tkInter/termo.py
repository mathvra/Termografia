# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import numpy as np
import tkinter.filedialog as fdlg
import cv2

#VERMELHO
def vermelho(foto):
    total = foto.shape[1] * foto.shape[0]
    imagemHSV = cv2.cvtColor(foto, cv2.COLOR_BGR2HSV)
    lowVermelho = np.array([0,128,51])
    upVermelho = np.array([7, 255, 255])

    lowVermelho2 = np.array([173,128,51])
    upVermelho2 = np.array([179, 255, 255])

    maskVermelho =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
    maskVermelho2 =  cv2.inRange(imagemHSV, lowVermelho2, upVermelho2)
    outputVermelho= cv2.bitwise_and(imagemHSV, foto, mask = maskVermelho + maskVermelho2)

    preto = 0
    for y in range(0, outputVermelho.shape[0], 1):
        for x in range(0, outputVermelho.shape[1], 1):
            (h, s, v) = outputVermelho[y, x]
            if (v==0):
                preto = preto + 1

    vermelho = ((total - preto)/total)*100
    print('Vermelho: ', vermelho)

    return vermelho

# LARANJA
def laranja(foto):
    total = foto.shape[1] * foto.shape[0]
    imagemHSV = cv2.cvtColor(foto, cv2.COLOR_BGR2HSV)
    lowLaranja = np.array([8, 128, 51])
    upLaranja = np.array([25, 255, 255])

    maskLaranja = cv2.inRange(imagemHSV, lowLaranja, upLaranja)
    outputLaranja = cv2.bitwise_and(imagemHSV, foto, mask=maskLaranja)

    preto = 0
    for y in range(0, outputLaranja.shape[0], 1):
        for x in range(0, outputLaranja.shape[1], 1):
            (h, s, v) = outputLaranja[y, x]
            if (v == 0):
                preto = preto + 1

    laranja = total - preto
    print('Laranja: ', laranja)
    return laranja

#AMARELO
def amarelo(foto):
    total = foto.shape[1] * foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowAmarelo = np.array([26,128,51])
    upAmarelo = np.array([30,255,255])

    maskAmarelo =  cv2.inRange(imagemHSV, lowAmarelo, upAmarelo)
    outputAmarelo= cv2.bitwise_and( foto, imagemHSV, mask = maskAmarelo)

    preto = 0
    for y in range(0, outputAmarelo.shape[0], 1):
        for x in range(0, outputAmarelo.shape[1], 1):
            (h, s, v) = outputAmarelo[y, x]
            if (v==0):
                preto = preto + 1

    amarelo = total - preto
    print('Amarelo: ', amarelo)
    return amarelo

#VERDE
def verde(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowVerde = np.array([31,128,51])
    upVerde = np.array([83,255,255])

    maskVerde =  cv2.inRange(imagemHSV, lowVerde, upVerde)
    outputVerde= cv2.bitwise_and( foto, imagemHSV, mask = maskVerde)

    preto = 0
    for y in range(0, outputVerde.shape[0], 1):
        for x in range(0, outputVerde.shape[1], 1):
            (h, s, v) = outputVerde[y, x]
            if (v==0):
                preto = preto + 1

    verde = total - preto
    print('Verde ', verde)
    return verde

#CIANO
def ciano(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowCiano = np.array([84,128,51])
    upCiano = np.array([98,255,255])

    maskCiano =  cv2.inRange(imagemHSV, lowCiano, upCiano)
    outputCiano= cv2.bitwise_and( foto, imagemHSV, mask = maskCiano)

    preto = 0
    for y in range(0, outputCiano.shape[0], 1):
        for x in range(0, outputCiano.shape[1], 1):
            (h, s, v) = outputCiano[y, x]
            if (v==0):
                preto = preto + 1

    ciano = total - preto
    print('Ciano: ', ciano)
    return ciano

#AZUL
def azul(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowAzul = np.array([99,128,51])
    upAzul = np.array([128,255,255])

    maskAzul =  cv2.inRange(imagemHSV, lowAzul, upAzul)
    outputAzul = cv2.bitwise_and( foto, imagemHSV, mask = maskAzul)

    preto = 0
    for y in range(0, outputAzul.shape[0], 1):
        for x in range(0, outputAzul.shape[1], 1):
            (h, s, v) = outputAzul[y, x]
            if (v==0):
                preto = preto + 1

    azul = total - preto
    print('Azul ', azul)
    return azul

#VIOLETA
def violeta(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowVioleta = np.array([129,128,51])
    upVioleta = np.array([143,255,255])

    maskVioleta =  cv2.inRange(imagemHSV, lowVioleta, upVioleta)
    outputVioleta = cv2.bitwise_and( foto, imagemHSV, mask = maskVioleta)

    preto = 0
    for y in range(0, outputVioleta.shape[0], 1):
        for x in range(0, outputVioleta.shape[1], 1):
            (h, s, v) = outputVioleta[y, x]
            if (v==0):
                preto = preto + 1

    violeta = total - preto
    print('Violeta: ', violeta)
    return violeta

#MAGENTA
def magenta(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowMagenta = np.array([144,128,51])
    upMagenta = np.array([172,255,255])

    maskMagenta =  cv2.inRange(imagemHSV, lowMagenta, upMagenta)
    outputMagenta = cv2.bitwise_and( foto, imagemHSV, mask = maskMagenta)

    preto = 0
    for y in range(0, outputMagenta.shape[0], 1):
        for x in range(0, outputMagenta.shape[1], 1):
            (h, s, v) = outputMagenta[y, x]
            if (v==0):
                preto = preto + 1

    magenta = total - preto
    print('Magenta: ', magenta)
    return magenta

#BRANCO
def branco(foto):
    total =  foto.shape[1] *  foto.shape[0]
    imagemHSV = cv2.cvtColor( foto, cv2.COLOR_BGR2HSV)
    lowBranco = np.array([0,0,204])
    upBranco = np.array([179,127,255])

    maskBranco =  cv2.inRange(imagemHSV, lowBranco, upBranco)
    outputBranco = cv2.bitwise_and( foto, imagemHSV, mask = maskBranco)

    preto = 0
    for y in range(0, outputBranco.shape[0], 1):
        for x in range(0, outputBranco.shape[1], 1):
            (h, s, v) = outputBranco[y, x]
            if (v==0):
                preto = preto + 1

    branco = total - preto
    print('Branco: ', branco)
    return branco

def chamarFuncoes(foto):
    vrml = vermelho(foto)
    lrj = laranja(foto)
    amrl = amarelo(foto)
    vrd = verde(foto)
    cno = ciano(foto)
    azl = azul(foto)
    vlt = violeta(foto)
    mgt = magenta(foto)
    brc = branco(foto)

    result = [vrml, lrj, amrl, vrd, cno, azl, vlt, mgt, brc]
    return  result

def select_image():
    global panelA
    path = fdlg.askopenfilename()
    nome = ['Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Ciano', 'Azul', 'Violeta', 'Magenta', 'Branco']
    
    image = cv2.imread(path)
    resultado = chamarFuncoes(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    if panelA is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)

    else:
        panelA.configure(image=image)
        panelA.image = image

    lb['text'] = 'Vermelho: {}%\nLaranja: {}\nAmarelo: {}\nVerde: {}\nCiano: {}\nAzul: {}\nVioleta: {}\nMagenta: {}\nBranco: {}'.format(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8])

janela = Tk()
janela.title('TermoCrivo v0.1')
janela["bg"] = "blue"
janela.geometry('1000x700+200+200')
panelA = None

bt = Button(janela, text="Select an image", command=select_image)
bt.pack(side="bottom", fill="both", padx="10", pady="10")

lb = Label(janela, text='Selecione uma imagem!')
lb.pack(side='top', padx=10, pady=10)

janela.mainloop()
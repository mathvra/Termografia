import cv2
import numpy as np

imagem = cv2.imread('teste2.jpeg', 1)
imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
total = imagem.shape[1] * imagem.shape[0]

#VERMELHO
def vermelho(total):
    lowVermelho = np.array([0,128,51])
    upVermelho = np.array([7, 255, 255])

    lowVermelho2 = np.array([173,128,51])
    upVermelho2 = np.array([179, 255, 255])

    maskVermelho =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
    maskVermelho2 =  cv2.inRange(imagemHSV, lowVermelho2, upVermelho2)
    outputVermelho= cv2.bitwise_and(imagemHSV, imagem, mask = maskVermelho + maskVermelho2)

    preto = 0
    for y in range(0, outputVermelho.shape[0], 1):
        for x in range(0, outputVermelho.shape[1], 1):
            (h, s, v) = outputVermelho[y, x]
            if (v==0):
                preto = preto + 1

    vermelho = total - preto
    print('Vermelho: ', vermelho)

    cv2.imshow('Vermelho', np.hstack([imagem, outputVermelho]))

# LARANJA
def laranja(total):
    lowLaranja = np.array([8, 128, 51])
    upLaranja = np.array([25, 255, 255])

    maskLaranja = cv2.inRange(imagemHSV, lowLaranja, upLaranja)
    outputLaranja = cv2.bitwise_and(imagemHSV, imagem, mask=maskLaranja)

    preto = 0
    for y in range(0, outputLaranja.shape[0], 1):
        for x in range(0, outputLaranja.shape[1], 1):
            (h, s, v) = outputLaranja[y, x]
            if (v == 0):
                preto = preto + 1

    laranja = total - preto
    print('Laranja: ', laranja)
    cv2.imshow('Laranja', np.hstack([imagem, outputLaranja]))

#AMARELO
def amarelo(total):
    lowAmarelo = np.array([26,128,51])
    upAmarelo = np.array([30,255,255])

    maskAmarelo =  cv2.inRange(imagemHSV, lowAmarelo, upAmarelo)
    outputAmarelo= cv2.bitwise_and(imagem, imagemHSV, mask = maskAmarelo)

    preto = 0
    for y in range(0, outputAmarelo.shape[0], 1):
        for x in range(0, outputAmarelo.shape[1], 1):
            (h, s, v) = outputAmarelo[y, x]
            if (v==0):
                preto = preto + 1

    amarelo = total - preto
    print('Amarelo: ', amarelo)
    cv2.imshow("Amarelo", np.hstack([imagem, outputAmarelo]))

#VERDE
def verde(total):
    lowVerde = np.array([31,128,51])
    upVerde = np.array([83,255,255])

    maskVerde =  cv2.inRange(imagemHSV, lowVerde, upVerde)
    outputVerde= cv2.bitwise_and(imagem, imagemHSV, mask = maskVerde)

    preto = 0
    for y in range(0, outputVerde.shape[0], 1):
        for x in range(0, outputVerde.shape[1], 1):
            (h, s, v) = outputVerde[y, x]
            if (v==0):
                preto = preto + 1

    verde = total - preto
    print('Verde ', verde)
    cv2.imshow("Verde", np.hstack([imagem, outputVerde]))

#CIANO
def ciano(total):
    lowCiano = np.array([84,128,51])
    upCiano = np.array([98,255,255])

    maskCiano =  cv2.inRange(imagemHSV, lowCiano, upCiano)
    outputCiano= cv2.bitwise_and(imagem, imagemHSV, mask = maskCiano)

    preto = 0
    for y in range(0, outputCiano.shape[0], 1):
        for x in range(0, outputCiano.shape[1], 1):
            (h, s, v) = outputCiano[y, x]
            if (v==0):
                preto = preto + 1

    ciano = total - preto
    print('Ciano: ', ciano)
    cv2.imshow("Ciano", np.hstack([imagem, outputCiano]))

#AZUL
def azul(total):
    lowAzul = np.array([99,128,51])
    upAzul = np.array([128,255,255])

    maskAzul =  cv2.inRange(imagemHSV, lowAzul, upAzul)
    outputAzul = cv2.bitwise_and(imagem, imagemHSV, mask = maskAzul)

    preto = 0
    for y in range(0, outputAzul.shape[0], 1):
        for x in range(0, outputAzul.shape[1], 1):
            (h, s, v) = outputAzul[y, x]
            if (v==0):
                preto = preto + 1

    azul = total - preto
    print('Azul ', azul)
    cv2.imshow("Azul", np.hstack([imagem, outputAzul]))

#VIOLETA
def violeta(total):
    lowVioleta = np.array([129,128,51])
    upVioleta = np.array([143,255,255])

    maskVioleta =  cv2.inRange(imagemHSV, lowVioleta, upVioleta)
    outputVioleta = cv2.bitwise_and(imagem, imagemHSV, mask = maskVioleta)

    preto = 0
    for y in range(0, outputVioleta.shape[0], 1):
        for x in range(0, outputVioleta.shape[1], 1):
            (h, s, v) = outputVioleta[y, x]
            if (v==0):
                preto = preto + 1

    violeta = total - preto
    print('Violeta: ', violeta)
    cv2.imshow('Violeta', np.hstack([imagem, outputVioleta]))

#MAGENTA
def magenta(total):
    lowMagenta = np.array([144,128,51])
    upMagenta = np.array([172,255,255])

    maskMagenta =  cv2.inRange(imagemHSV, lowMagenta, upMagenta)
    outputMagenta = cv2.bitwise_and(imagem, imagemHSV, mask = maskMagenta)

    preto = 0
    for y in range(0, outputMagenta.shape[0], 1):
        for x in range(0, outputMagenta.shape[1], 1):
            (h, s, v) = outputMagenta[y, x]
            if (v==0):
                preto = preto + 1

    magenta = total - preto
    print('Magenta: ', magenta)
    cv2.imshow('Magenta', np.hstack([imagem, outputMagenta]))

#BRANCO
def branco(total):
    lowBranco = np.array([0,0,204])
    upBranco = np.array([179,127,255])

    maskBranco =  cv2.inRange(imagemHSV, lowBranco, upBranco)
    outputBranco = cv2.bitwise_and(imagem, imagemHSV, mask = maskBranco)

    preto = 0
    for y in range(0, outputBranco.shape[0], 1):
        for x in range(0, outputBranco.shape[1], 1):
            (h, s, v) = outputBranco[y, x]
            if (v==0):
                preto = preto + 1

    branco = total - preto
    print('Branco: ', branco)
    cv2.imshow("Branco", np.hstack([imagem, outputBranco]))

print("Total: {}" .format(imagem.shape[1] * imagem.shape[0]))

print("Canais: {}".format(imagem.shape[2]))

#Chamando func:
vermelho(total)
laranja(total)
amarelo(total)
verde(total)
ciano(total)
azul(total)
violeta(total)
magenta(total)
branco(total)

cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import numpy as np
from . import models

class Tratamento:
    def __init__(self, foto):
        self.foto = models.ContaCores.foto
        self.total = self.foto.shape[1] * self.foto.shape[0]
        self.imagemHSV = cv2.cvtColor(self.foto, cv2.COLOR_BGR2HSV)

    #VERMELHO
    def vermelho(self):
        lowVermelho = np.array([0,128,51])
        upVermelho = np.array([7, 255, 255])

        lowVermelho2 = np.array([173,128,51])
        upVermelho2 = np.array([179, 255, 255])

        maskVermelho =  cv2.inRange(self.imagemHSV, lowVermelho, upVermelho)
        maskVermelho2 =  cv2.inRange(self.imagemHSV, lowVermelho2, upVermelho2)
        outputVermelho= cv2.bitwise_and(self.imagemHSV, self.foto, mask = maskVermelho + maskVermelho2)

        preto = 0
        for y in range(0, outputVermelho.shape[0], 1):
            for x in range(0, outputVermelho.shape[1], 1):
                (h, s, v) = outputVermelho[y, x]
                if (v==0):
                    preto = preto + 1

        vermelho = self.total - preto
        print('Vermelho: ', vermelho)

        cv2.imshow('Vermelho', np.hstack([self.foto, outputVermelho]))

    # LARANJA
    def laranja(self):
        lowLaranja = np.array([8, 128, 51])
        upLaranja = np.array([25, 255, 255])

        maskLaranja = cv2.inRange(self.imagemHSV, lowLaranja, upLaranja)
        outputLaranja = cv2.bitwise_and(self.imagemHSV, self.foto, mask=maskLaranja)

        preto = 0
        for y in range(0, outputLaranja.shape[0], 1):
            for x in range(0, outputLaranja.shape[1], 1):
                (h, s, v) = outputLaranja[y, x]
                if (v == 0):
                    preto = preto + 1

        laranja = self.total - preto
        print('Laranja: ', laranja)
        cv2.imshow('Laranja', np.hstack([self.foto, outputLaranja]))

    #AMARELO
    def amarelo(self):
        lowAmarelo = np.array([26,128,51])
        upAmarelo = np.array([30,255,255])

        maskAmarelo =  cv2.inRange(self.imagemHSV, lowAmarelo, upAmarelo)
        outputAmarelo= cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskAmarelo)

        preto = 0
        for y in range(0, outputAmarelo.shape[0], 1):
            for x in range(0, outputAmarelo.shape[1], 1):
                (h, s, v) = outputAmarelo[y, x]
                if (v==0):
                    preto = preto + 1

        amarelo = self.total - preto
        print('Amarelo: ', amarelo)
        cv2.imshow("Amarelo", np.hstack([self.foto, outputAmarelo]))

    #VERDE
    def verde(self):
        lowVerde = np.array([31,128,51])
        upVerde = np.array([83,255,255])

        maskVerde =  cv2.inRange(self.imagemHSV, lowVerde, upVerde)
        outputVerde= cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskVerde)

        preto = 0
        for y in range(0, outputVerde.shape[0], 1):
            for x in range(0, outputVerde.shape[1], 1):
                (h, s, v) = outputVerde[y, x]
                if (v==0):
                    preto = preto + 1

        verde = self.total - preto
        print('Verde ', verde)
        cv2.imshow("Verde", np.hstack([self.foto, outputVerde]))

    #CIANO
    def ciano(self):
        lowCiano = np.array([84,128,51])
        upCiano = np.array([98,255,255])

        maskCiano =  cv2.inRange(self.imagemHSV, lowCiano, upCiano)
        outputCiano= cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskCiano)

        preto = 0
        for y in range(0, outputCiano.shape[0], 1):
            for x in range(0, outputCiano.shape[1], 1):
                (h, s, v) = outputCiano[y, x]
                if (v==0):
                    preto = preto + 1

        ciano = self.total - preto
        print('Ciano: ', ciano)
        cv2.imshow("Ciano", np.hstack([self.foto, outputCiano]))

    #AZUL
    def azul(self):
        lowAzul = np.array([99,128,51])
        upAzul = np.array([128,255,255])

        maskAzul =  cv2.inRange(self.imagemHSV, lowAzul, upAzul)
        outputAzul = cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskAzul)

        preto = 0
        for y in range(0, outputAzul.shape[0], 1):
            for x in range(0, outputAzul.shape[1], 1):
                (h, s, v) = outputAzul[y, x]
                if (v==0):
                    preto = preto + 1

        azul = self.total - preto
        print('Azul ', azul)
        cv2.imshow("Azul", np.hstack([self.foto, outputAzul]))

    #VIOLETA
    def violeta(self):
        lowVioleta = np.array([129,128,51])
        upVioleta = np.array([143,255,255])

        maskVioleta =  cv2.inRange(self.imagemHSV, lowVioleta, upVioleta)
        outputVioleta = cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskVioleta)

        preto = 0
        for y in range(0, outputVioleta.shape[0], 1):
            for x in range(0, outputVioleta.shape[1], 1):
                (h, s, v) = outputVioleta[y, x]
                if (v==0):
                    preto = preto + 1

        violeta = self.total - preto
        print('Violeta: ', violeta)
        cv2.imshow('Violeta', np.hstack([self.foto, outputVioleta]))

    #MAGENTA
    def magenta(self):
        lowMagenta = np.array([144,128,51])
        upMagenta = np.array([172,255,255])

        maskMagenta =  cv2.inRange(self.imagemHSV, lowMagenta, upMagenta)
        outputMagenta = cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskMagenta)

        preto = 0
        for y in range(0, outputMagenta.shape[0], 1):
            for x in range(0, outputMagenta.shape[1], 1):
                (h, s, v) = outputMagenta[y, x]
                if (v==0):
                    preto = preto + 1

        magenta = self.total - preto
        print('Magenta: ', magenta)
        cv2.imshow('Magenta', np.hstack([self.foto, outputMagenta]))

    #BRANCO
    def branco(self):
        lowBranco = np.array([0,0,204])
        upBranco = np.array([179,127,255])

        maskBranco =  cv2.inRange(self.imagemHSV, lowBranco, upBranco)
        outputBranco = cv2.bitwise_and(self.foto, self.imagemHSV, mask = maskBranco)

        preto = 0
        for y in range(0, outputBranco.shape[0], 1):
            for x in range(0, outputBranco.shape[1], 1):
                (h, s, v) = outputBranco[y, x]
                if (v==0):
                    preto = preto + 1

        branco = self.total - preto
        print('Branco: ', branco)
        cv2.imshow("Branco", np.hstack([self.foto, outputBranco]))



cv2.waitKey(0)

cv2.destroyAllWindows()
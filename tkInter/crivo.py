from PIL import Image
from PIL import ImageTk
import numpy as np
import cv2


class Crivo():
    def __init__(self, foto):
        self.foto = foto

    #VERMELHO
    def vermelho(self):
        total = self.foto.shape[1] * self.foto.shape[0]
        imagemHSV = cv2.cvtColor(self.foto, cv2.COLOR_BGR2HSV)
        lowVermelho = np.array([0,78,51])
        upVermelho = np.array([7, 255, 255])

        lowVermelho2 = np.array([173,78,51])
        upVermelho2 = np.array([179, 255, 255])

        maskVermelho =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
        maskVermelho2 =  cv2.inRange(imagemHSV, lowVermelho2, upVermelho2)
        outputVermelho= cv2.bitwise_and(imagemHSV, self.foto, mask = maskVermelho + maskVermelho2)

        preto = 0
        for y in range(0, outputVermelho.shape[0], 1):
            for x in range(0, outputVermelho.shape[1], 1):
                (h, s, v) = outputVermelho[y, x]
                if (v==0):
                    preto = preto + 1

        vermelhoQtd = ((total - preto)/total)*100
        print('Vermelho: ', vermelhoQtd)
        # cv2.imshow('Vermelho', np.hstack([self.foto, outputVermelho]))
        vermelho = [vermelhoQtd, outputVermelho]
        return vermelho

    # LARANJA
    def laranja(self):
        total = self.foto.shape[1] * self.foto.shape[0]
        imagemHSV = cv2.cvtColor(self.foto, cv2.COLOR_BGR2HSV)
        lowLaranja = np.array([8, 78, 51])
        upLaranja = np.array([25, 255, 255])

        maskLaranja = cv2.inRange(imagemHSV, lowLaranja, upLaranja)
        outputLaranja = cv2.bitwise_and(imagemHSV, self.foto, mask=maskLaranja)

        preto = 0
        for y in range(0, outputLaranja.shape[0], 1):
            for x in range(0, outputLaranja.shape[1], 1):
                (h, s, v) = outputLaranja[y, x]
                if (v == 0):
                    preto = preto + 1

        laranjaQtd = ((total - preto)/total)*100
        print('Laranja: ', laranjaQtd)
        # cv2.imshow('Laranja', np.hstack([self.foto, outputLaranja]))
        laranja = [laranjaQtd, outputLaranja]
        return laranja

    #AMARELO
    def amarelo(self):
        total = self.foto.shape[1] * self.foto.shape[0]
        imagemHSV = cv2.cvtColor(self.foto, cv2.COLOR_BGR2HSV)
        lowAmarelo = np.array([26,78,51])
        upAmarelo = np.array([30,255,255])

        maskAmarelo =  cv2.inRange(imagemHSV, lowAmarelo, upAmarelo)
        outputAmarelo= cv2.bitwise_and(self.foto, imagemHSV, mask = maskAmarelo)

        preto = 0
        for y in range(0, outputAmarelo.shape[0], 1):
            for x in range(0, outputAmarelo.shape[1], 1):
                (h, s, v) = outputAmarelo[y, x]
                if (v==0):
                    preto = preto + 1

        amareloQtd = ((total - preto)/total)*100
        print('Amarelo: ', amareloQtd)
        # cv2.imshow("Amarelo", np.hstack([self.foto, outputAmarelo]))
        amarelo = [amareloQtd, outputAmarelo]
        return amarelo

    #VERDE
    def verde(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor(self.foto, cv2.COLOR_BGR2HSV)
        lowVerde = np.array([31,78,51])
        upVerde = np.array([83,255,255])

        maskVerde =  cv2.inRange(imagemHSV, lowVerde, upVerde)
        outputVerde= cv2.bitwise_and(self.foto, imagemHSV, mask = maskVerde)

        preto = 0
        for y in range(0, outputVerde.shape[0], 1):
            for x in range(0, outputVerde.shape[1], 1):
                (h, s, v) = outputVerde[y, x]
                if (v==0):
                    preto = preto + 1

        verdeQtd = ((total - preto)/total)*100
        print('Verde ', verdeQtd)
        # cv2.imshow("Verde", np.hstack([self.foto, outputVerde]))
        verde = [verdeQtd, outputVerde]
        return verde

    #CIANO
    def ciano(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor( self.foto, cv2.COLOR_BGR2HSV)
        lowCiano = np.array([84,78,51])
        upCiano = np.array([98,255,255])

        maskCiano =  cv2.inRange(imagemHSV, lowCiano, upCiano)
        outputCiano= cv2.bitwise_and( self.foto, imagemHSV, mask = maskCiano)

        preto = 0
        for y in range(0, outputCiano.shape[0], 1):
            for x in range(0, outputCiano.shape[1], 1):
                (h, s, v) = outputCiano[y, x]
                if (v==0):
                    preto = preto + 1

        cianoQtd = ((total - preto)/total)*100
        print('Ciano: ', cianoQtd)
        # cv2.imshow("Ciano", np.hstack([self.foto, outputCiano]))
        ciano = [cianoQtd, outputCiano]
        return ciano

    #AZUL
    def azul(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor( self.foto, cv2.COLOR_BGR2HSV)
        lowAzul = np.array([99,78,51])
        upAzul = np.array([128,255,255])

        maskAzul =  cv2.inRange(imagemHSV, lowAzul, upAzul)
        outputAzul = cv2.bitwise_and( self.foto, imagemHSV, mask = maskAzul)

        preto = 0
        for y in range(0, outputAzul.shape[0], 1):
            for x in range(0, outputAzul.shape[1], 1):
                (h, s, v) = outputAzul[y, x]
                if (v==0):
                    preto = preto + 1

        azulQtd = ((total - preto)/total)*100
        print('Azul ', azulQtd)
        # cv2.imshow("Azul", np.hstack([self.foto, outputAzul]))
        azul = [azulQtd, outputAzul]
        return azul

    #VIOLETA
    def violeta(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor( self.foto, cv2.COLOR_BGR2HSV)
        lowVioleta = np.array([129,78,51])
        upVioleta = np.array([143,255,255])

        maskVioleta =  cv2.inRange(imagemHSV, lowVioleta, upVioleta)
        outputVioleta = cv2.bitwise_and( self.foto, imagemHSV, mask = maskVioleta)

        preto = 0
        for y in range(0, outputVioleta.shape[0], 1):
            for x in range(0, outputVioleta.shape[1], 1):
                (h, s, v) = outputVioleta[y, x]
                if (v==0):
                    preto = preto + 1

        violetaQtd = ((total - preto)/total)*100
        print('Violeta: ', violetaQtd)
        # cv2.imshow('Violeta', np.hstack([self.foto, outputVioleta]))
        violeta = [violetaQtd, outputVioleta]
        return violeta

    #MAGENTA
    def magenta(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor( self.foto, cv2.COLOR_BGR2HSV)
        lowMagenta = np.array([144,78,51])
        upMagenta = np.array([172,255,255])

        maskMagenta =  cv2.inRange(imagemHSV, lowMagenta, upMagenta)
        outputMagenta = cv2.bitwise_and( self.foto, imagemHSV, mask = maskMagenta)

        preto = 0
        for y in range(0, outputMagenta.shape[0], 1):
            for x in range(0, outputMagenta.shape[1], 1):
                (h, s, v) = outputMagenta[y, x]
                if (v==0):
                    preto = preto + 1

        magentaQtd = ((total - preto)/total)*100
        print('Magenta: ', magentaQtd)
        # cv2.imshow('Magenta', np.hstack([self.foto, outputMagenta]))
        magenta = [magentaQtd, outputMagenta]
        return magenta

    #BRANCO
    def branco(self):
        total =  self.foto.shape[1] *  self.foto.shape[0]
        imagemHSV = cv2.cvtColor( self.foto, cv2.COLOR_BGR2HSV)
        lowBranco = np.array([0,0,204])
        upBranco = np.array([179,77,255])

        maskBranco =  cv2.inRange(imagemHSV, lowBranco, upBranco)
        outputBranco = cv2.bitwise_and( self.foto, imagemHSV, mask = maskBranco)

        preto = 0
        for y in range(0, outputBranco.shape[0], 1):
            for x in range(0, outputBranco.shape[1], 1):
                (h, s, v) = outputBranco[y, x]
                if (v==0):
                    preto = preto + 1

        brancoQtd = ((total - preto)/total)*100
        print('Branco: ', brancoQtd)
        # cv2.imshow("Branco", np.hstack([self.foto, outputBranco]))
        branco = [brancoQtd, outputBranco]
        return branco
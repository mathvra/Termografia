import cv2
import numpy as np

verde=0
vermelho=0
azul=0
amarelo=0
ciano =0
magenta=0
preto=0
preto2=0
preto3=0
preto4=0
preto5=0
preto6=0
preto7=0
preto8=0
preto9=0
branco=0

total=0
imagem = cv2.imread('teste2.jpeg', 1)
imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#VERMELHO
lowVermelho = np.array([0,128,77])
upVermelho = np.array([7, 255, 255])

lowVermelho2 = np.array([172,128,77])
upVermelho2 = np.array([179, 255, 255])

maskVermelho =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
maskVermelho2 =  cv2.inRange(imagemHSV, lowVermelho2, upVermelho2)
outputVermelho= cv2.bitwise_and(imagemHSV, imagem, mask = maskVermelho + maskVermelho2)



for y in range(0, outputVermelho.shape[0], 1):
    for x in range(0, outputVermelho.shape[1], 1):
        (h, s, v) = outputVermelho[y, x]
        posicao=outputVermelho[y, x]

        if (v==0):
            preto=preto+1

# LARANJA
lowLaranja = np.array([8, 128, 77])
upLaranja = np.array([22, 255, 255])

maskLaranja = cv2.inRange(imagemHSV, lowLaranja, upLaranja)
outputLaranja = cv2.bitwise_and(imagemHSV, imagem, mask=maskLaranja)

for y in range(0, outputLaranja.shape[0], 1):
    for x in range(0, outputLaranja.shape[1], 1):
        (h, s, v) = outputLaranja[y, x]
        posicao = outputLaranja[y, x]
        if (v == 0):
            preto8 = preto8 + 1

#AMARELO
lowAmarelo = np.array([23,128,77])
upAmarelo = np.array([30,255,255])

maskAmarelo =  cv2.inRange(imagemHSV, lowAmarelo, upAmarelo)
outputAmarelo= cv2.bitwise_and(imagem, imagemHSV, mask = maskAmarelo)

for y in range(0, outputAmarelo.shape[0], 1):
    for x in range(0, outputAmarelo.shape[1], 1):
        (h, s, v) = outputAmarelo[y, x]
        posicao=outputAmarelo[y, x]

        if (v==0):
            preto2=preto2+1

#VERDE
lowVerde = np.array([31,128,77])
upVerde = np.array([83,255,255])

maskVerde =  cv2.inRange(imagemHSV, lowVerde, upVerde)
outputVerde= cv2.bitwise_and(imagem, imagemHSV, mask = maskVerde)

for y in range(0, outputVerde.shape[0], 1):
    for x in range(0, outputVerde.shape[1], 1):
        (h, s, v) = outputVerde[y, x]
        posicao=outputVerde[y, x]
        if (v==0):
            preto3=preto3+1

#CIANO
lowCiano = np.array([84,128,77])
upCiano = np.array([98,255,255])

maskCiano =  cv2.inRange(imagemHSV, lowCiano, upCiano)
outputCiano= cv2.bitwise_and(imagem, imagemHSV, mask = maskCiano)

for y in range(0, outputCiano.shape[0], 1):
    for x in range(0, outputCiano.shape[1], 1):
        (h, s, v) = outputCiano[y, x]
        posicao=outputCiano[y, x]
        if (v==0):
            preto4=preto4+1

#AZUL
lowAzul = np.array([99,128,77])
upAzul = np.array([128,255,255])

maskAzul =  cv2.inRange(imagemHSV, lowAzul, upAzul)
outputAzul = cv2.bitwise_and(imagem, imagemHSV, mask = maskAzul)

for y in range(0, outputAzul.shape[0], 1):
    for x in range(0, outputAzul.shape[1], 1):
        (h, s, v) = outputAzul[y, x]
        posicao=outputAzul[y, x]
        if (v==0):
            preto5=preto5+1

#VIOLETA
lowVioleta = np.array([129,128,77])
upVioleta = np.array([143,255,255])

maskVioleta =  cv2.inRange(imagemHSV, lowVioleta, upVioleta)
outputVioleta = cv2.bitwise_and(imagem, imagemHSV, mask = maskVioleta)

for y in range(0, outputVioleta.shape[0], 1):
    for x in range(0, outputVioleta.shape[1], 1):
        (h, s, v) = outputVioleta[y, x]
        posicao=outputVioleta[y, x]
        if (v==0):
            preto6=preto6+1


#MAGENTA
lowMagenta = np.array([144,128,77])
upMagenta = np.array([171,255,255])

maskMagenta =  cv2.inRange(imagemHSV, lowMagenta, upMagenta)
outputMagenta = cv2.bitwise_and(imagem, imagemHSV, mask = maskMagenta)

for y in range(0, outputMagenta.shape[0], 1):
    for x in range(0, outputMagenta.shape[1], 1):
        (h, s, v) = outputMagenta[y, x]
        posicao=outputMagenta[y, x]
        if (v==0):
            preto7=preto7+1

#BRANCO
lowBranco = np.array([0,0,204])
upBranco = np.array([179,127,255])

maskBranco =  cv2.inRange(imagemHSV, lowBranco, upBranco)
outputBranco = cv2.bitwise_and(imagem, imagemHSV, mask = maskBranco)

for y in range(0, outputBranco.shape[0], 1):
    for x in range(0, outputBranco.shape[1], 1):
        (h, s, v) = outputBranco[y, x]
        posicao=outputBranco[y, x]
        if (v==0):
            preto9=preto9+1

outputGeral = cv2.bitwise_and(imagem, imagemHSV, mask = maskBranco + maskMagenta + maskVioleta + maskVermelho2+maskVermelho+maskAmarelo+maskAzul+maskCiano+maskVerde+maskLaranja)

total=imagem.shape[1] * imagem.shape[0]

print("Total {}" .format(imagem.shape[1] * imagem.shape[0]))
vermelho = total - preto
laranja = total - preto8
amarelo=total-preto2
verde=total-preto3
ciano=total-preto4
azul=total-preto5
violeta=total-preto6
magenta=total-preto7
branco= total-preto9



print("Vermelho: {}\nLaranja {}\nAmarelo: {}\nVerde: {}\nCiano: {}\nAzul: {}\nVioleta: {}\nMagenta: {}\nBranco: {}".format(vermelho, laranja, amarelo, verde, ciano, azul, violeta, magenta,branco))
print("Canais: {}".format(imagem.shape[2]))

#Imprime Imagens!
cv2.imshow("Vermelho", np.hstack([imagem, outputVermelho]))
cv2.imshow("Laranja", np.hstack([imagem, outputLaranja]))
cv2.imshow("Amarelo", np.hstack([imagem, outputAmarelo]))
cv2.imshow("Verde", np.hstack([imagem, outputVerde]))
cv2.imshow("Ciano", np.hstack([imagem, outputCiano]))
cv2.imshow("Azul", np.hstack([imagem, outputAzul]))
cv2.imshow("Violeta", np.hstack([imagem, outputVioleta]))
cv2.imshow("Magenta", np.hstack([imagem, outputMagenta]))
cv2.imshow("Branco", np.hstack([imagem, outputBranco]))
cv2.imshow("Todos", np.hstack([imagem,outputGeral]))


cv2.waitKey(0)

cv2.destroyAllWindows()
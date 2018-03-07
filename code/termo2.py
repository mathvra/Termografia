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
branco=0

total=0
imagem = cv2.imread('teste2.jpeg', 1)
imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#VERMELHO
lowVermelho = np.array([0,128,128])
upVermelho = np.array([15, 255, 255])

lowVermelho2 = np.array([345,128,128])
upVermelho2 = np.array([359, 255, 255])

maskVermelho =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
maskVermelho2 =  cv2.inRange(imagemHSV, lowVermelho2, upVermelho2)
outputVermelho= cv2.bitwise_and(imagemHSV, imagem, mask = maskVermelho + maskVermelho2)

cv2.imshow("Vermelho", np.hstack([imagem, outputVermelho]))

for y in range(0, outputVermelho.shape[0], 1):
    for x in range(0, outputVermelho.shape[1], 1):
        (h, s, v) = outputVermelho[y, x]
        posicao=outputVermelho[y, x]

        if (v==0):
            preto=preto+1


vermelho = total - preto
#AMARELO
lowAmarelo = np.array([45,0,0])
upAmarelo = np.array([65, 255, 255])

maskAmarelo =  cv2.inRange(imagemHSV, lowAmarelo, upAmarelo)
outputAmarelo= cv2.bitwise_and(imagem, imagemHSV, mask = maskAmarelo)

cv2.imshow("imagens2", np.hstack([imagem, outputAmarelo]))

for y in range(0, outputAmarelo.shape[0], 1):
    for x in range(0, outputAmarelo.shape[1], 1):
        (h, s, v) = outputAmarelo[y, x]
        posicao=outputAmarelo[y, x]

        if (v==0):
            preto2=preto2+1

total=imagem.shape[1] * imagem.shape[0]

print("Total {}" .format(imagem.shape[1] * imagem.shape[0]))
amarelo=total-preto2
print("Vermelho: {}\nAmarelo: {}".format(vermelho, amarelo))
print("Canais: {}".format(imagem.shape[2]))

cv2.waitKey(0)

cv2.destroyAllWindows()
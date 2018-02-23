import cv2
import numpy as np

verde=0
vermelho=0
azul=0
amarelo=0
ciano =0
magenta=0
preto=0
branco=0

total=0
imagem = cv2.imread('lego.jpg', 1)
imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#VERMELHO
lowVermelho = np.array([-30,0,0])
upVermelho = np.array([30, 255, 255])

mask =  cv2.inRange(imagemHSV, lowVermelho, upVermelho)
output= cv2.bitwise_and(imagem, imagemHSV, mask = mask)

cv2.imshow("imagens", np.hstack([imagem, output]))

for y in range(0, output.shape[0],1):
    for x in range(0, output.shape[1],1):
        (h, s, v) = output[y, x]
        posicao=output[y, x]

        if (v==0):
            preto=preto+1

total=imagem.shape[1] * imagem.shape[0]

print("Total {}" .format(imagem.shape[1] * imagem.shape[0]))
vermelho=total-preto
print("Vermelho: {}".format(vermelho))
print("Canais: {}".format(imagem.shape[2]))

cv2.waitKey(0)

cv2.destroyAllWindows()
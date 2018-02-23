import cv2

verde=0
vermelho=0
azul=0
amarelo=0
ciano =0
magenta=0
preto=0
branco=0

total=0
imagemCarregada = cv2.imread("lego.jpg", 1)
for y in range(0, imagemCarregada.shape[0],1):
    for x in range(0, imagemCarregada.shape[1],1):
        (b, g, r) = imagemCarregada[y, x]
        posicao=imagemCarregada[y, x]

        #VERMELHO
        if ((b>=0 and b<=124) and (g>=0 and g<=124) and r==255):
            vermelho=vermelho+1

        #AMARELO
        if (b==0 and (g>=125 and g<=255) and (r>=124 and r<=255)):
            amarelo = amarelo + 1

        #VERDE
        if ((b>=0 and b<=124) and g==255 and (r>=0 and r<=125)):
            verde=verde+1

        #CIANO
        if ((b>=125 and b<=255) and (g>=124 and g<=255) and r==0):
            ciano=ciano+1

        #AZUL
        if (b==255 and (g>=0 and g<=125) and (r>=0 and r<=124)):
            azul=azul+1

        #MAGENTA
        if ((b>=124 and b<=255) and g==0 and (r>=125 and r<=255)):
            magenta=magenta+1

        #PRETO
        if (b==0 and g==0 and r==0):
            preto=preto+1

        #BRANCO
        if (b==255 and g==255 and r==255):
           branco=branco+1

#PORCETAGEM:
total = (imagemCarregada.shape[1] * imagemCarregada.shape[0])/100
vermelhoP=vermelho/total
amareloP=amarelo/total
verdeP=verde/total
cianoP=ciano/total
azulP=azul/total
magentaP=magenta/total
pretoP=preto/total
brancoP=branco/total


cv2.imshow("Imagem modificada", imagemCarregada)
print("Vermelho: {}\nAmarelo: {}\nVerde: {}\nCiano: {}\nAzul: {}\nMagenta: {}\nPreto: {}\nBranco: {}".format(vermelho, amarelo, verde, ciano, azul, magenta, preto, branco))
print('PORCENTAGENS:\n\n'
      'Vermelho: {:.2f}%\n'
      'Amarelo: {:.2f}%\n'
      'Verde: {:.2f}%\n'
      'Ciano: {:.2f}%\n'
      'Azul: {:.2f}%\n'
      'Magenta: {:.2f}%\n'
      'Preto: {:.2f}%\n'
      'Branco: {:.2f}%'.format(vermelhoP, amareloP, verdeP, cianoP, azulP, magentaP, pretoP, brancoP))
cv2.waitKey(0)


cv2.destroyAllWindows()

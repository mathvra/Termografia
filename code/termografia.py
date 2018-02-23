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
imagemCarregada = cv2.imread('vermelho1.png', 1)
for y in range(0, imagemCarregada.shape[0],1):
    for x in range(0, imagemCarregada.shape[1],1):
        (b, g, r) = imagemCarregada[y, x]
        posicao=imagemCarregada[y, x]

        #VERMELHO
        if ((b==0 and g==0 and (r>=45 and r<=255)) or((b>=0 and b<=124) and (g>=0 and g<=124) and r==255)):
            vermelho=vermelho+1
'''
        #AMARELO
        elif (b==0 and (g>=125 and g<=255) and (r>=124 and r<=255)):
                amarelo = amarelo + 1

        #VERDE
        elif (b==0 and r==0 and (g>=45 and g<=255)) or ((b>=0 and b<=124) and g==255 and (r>=0 and r<=125)):
            verde=verde+1

        #CIANO
        elif ((b>=125 and b<=255) and (g>=124 and g<=255) and r==0):
            ciano=ciano+1

        #AZUL
        elif (r==0 and g==0 and (b>=45 and b<=255)) or (b==255 and (g>=0 and g<=125) and (r>=0 and r<=124)):
            azul=azul+1

        #MAGENTA
        elif ((b>=124 and b<=255) and g==0 and (r>=125 and r<=255)):
            magenta=magenta+1

        #PRETO
        elif (((b>=0 and b<=44) and (g>=0 and g<=44) and (r>=0 and r<=44)) or (b==0 and g==0 and r==0)):
            preto=preto+1

        #BRANCO
        branco = (imagemCarregada.shape[1] * imagemCarregada.shape[0]) - (preto + magenta + azul + ciano + verde + amarelo + vermelho)

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
'''

cv2.imshow("Imagem modificada", imagemCarregada)
print("Vermelho: {}\nAmarelo: {}\nVerde: {}\nCiano: {}\nAzul: {}\nMagenta: {}\nPreto: {}\nBranco: {}".format(vermelho, amarelo, verde, ciano, azul, magenta, preto, branco))

'''
print('PORCENTAGENS:\n\n'
      'Vermelho: {:.2f}%\n'
      'Amarelo: {:.2f}%\n'
      'Verde: {:.2f}%\n'
      'Ciano: {:.2f}%\n'
      'Azul: {:.2f}%\n'
      'Magenta: {:.2f}%\n'
      'Preto: {:.2f}%\n'
      'Branco: {:.2f}%'.format(vermelhoP, amareloP, verdeP, cianoP, azulP, magentaP, pretoP, brancoP))
'''
print("Total {}" .format(imagemCarregada.shape[1] * imagemCarregada.shape[0]))
print("Canais: {}".format(imagemCarregada.shape[2]))

cv2.waitKey(0)

cv2.destroyAllWindows()

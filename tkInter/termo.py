# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import numpy as np
import tkinter.filedialog as fdlg
import cv2
from crivo import Crivo


def select_image():
    global panelA
    path = fdlg.askopenfilename()
    
    image = cv2.imread(path)
    crivo = Crivo(image)
    vrml = crivo.vermelho()
    lrj = crivo.laranja()
    amrl = crivo.amarelo()
    vrd = crivo.verde()
    cno = crivo.ciano()
    azl = crivo.azul()
    vlt = crivo.violeta()
    mgt = crivo.magenta()
    brc = crivo.branco()
    resultado = [vrml, lrj, amrl, vrd, cno, azl, vlt, mgt, brc]
    
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

    # vermelhoLb['text'] = 'Vermelho: {:.2f}%'.format(resultado[0][0])
    # laranjaLb['text'] = 'Laranja: {:.2f}%'.format(resultado[1][0])
    # amareloLb['text'] = 'Amarelo: {:.2f}%'.format(resultado[2][0])
    # verdeLb['text'] = 'Verde: {:.2f}%'.format(resultado[3][0])
    # cianoLb['text'] = 'Ciano: {:.2f}%'.format(resultado[4][0])
    # azulLb['text'] = 'Azul: {:.2f}%'.format(resultado[5][0])
    # violetaLb['text'] = 'Violeta: {:.2f}%'.format(resultado[6][0])
    # magentaLb['text'] = 'Magenta: {:.2f}%'.format(resultado[7][0])
    # brancoLb['text'] = 'Branco: {:.2f}%'.format(resultado[8][0])


    # lb['text'] = 'Vermelho: {:.2f}%'.format(resultado[0][0])
    # lb['text'] = 'Laranja: {:.2f}%'.format(resultado[1][0])
    # lb['text'] = 'Amarelo: {:.2f}%'.format(resultado[2][0])
    # lb['text'] = 'Verde: {:.2f}%'.format(resultado[3][0])
    # lb['text'] = 'Ciano: {:.2f}%'.format(resultado[4][0])
    # lb['text'] = 'Azul: {:.2f}%'.format(resultado[5][0])
    # lb['text'] = 'Violeta: {:.2f}%'.format(resultado[6][0])
    # lb['text'] = 'Magenta: {:.2f}%'.format(resultado[7][0])
    # lb['text'] = 'Branco: {:.2f}%'.format(resultado[8][0])


    lb['text'] = 'Vermelho: {:.2f}%\nLaranja: {:.2f}%\nAmarelo: {:.2f}%\nVerde: {:.2f}%\nCiano: {:.2f}%\nAzul: {:.2f}%\nVioleta: {:.2f}%\nMagenta: {:.2f}%\nBranco: {:.2f}%'.format(resultado[0][0], resultado[1][0], resultado[2][0], resultado[3][0], resultado[4][0], resultado[5][0], resultado[6][0], resultado[7][0], resultado[8][0])

janela = Tk()
janela.title('TermoCrivo v0.1')
janela["bg"] = "white"
janela.geometry('800x600+100+100')
panelA = None

bt = Button(janela, text="SELECIONAR IMAGEM", command=select_image)
bt.pack(side="bottom", fill="both", padx="10", pady="10", ipady='40')

# vermelhoLb = Label(janela, text='Vermelho: __%')
# laranjaLb = Label(janela, text='Laranja: __%')
# amareloLb = Label(janela, text='Amarelo: __%')
# verdeLb = Label(janela, text='Verde: __%')
# cianoLb = Label(janela, text='Ciano: __%')
# azulLb = Label(janela, text='Azul: __%')
# violetaLb = Label(janela, text='Violeta: __%')
# magentaLb = Label(janela, text='Magenta: __%')
# brancoLb = Label(janela, text='Branco: __%')

lb = Label(janela, text='Olá! Escolha uma imagem usando o botão abaixo!')
# lb = Label(janela, text='Laranja: __%')
# lb = Label(janela, text='Amarelo: __%')
# lb = Label(janela, text='Verde: __%')
# lb = Label(janela, text='Ciano: __%')
# lb = Label(janela, text='Azul: __%')
# lb = Label(janela, text='Violeta: __%')
# lb = Label(janela, text='Magenta: __%')
# lb = Label(janela, text='Branco: __%')


lb['bg'] = 'white'
lb.pack(side='left', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)
# lb.pack(side='right', padx=10, pady=10)


# vermelhoLb.pack(side='right', padx=10, pady=10)
# laranjaLb.pack(side='right', padx=10, pady=10)
# amareloLb.pack(side='right', padx=10, pady=10)
# verdeLb.pack(side='right', padx=10, pady=10)
# cianoLb.pack(side='right', padx=10, pady=10)
# azulLb.pack(side='right', padx=10, pady=10)
# violetaLb.pack(side='right', padx=10, pady=10)
# magentaLb.pack(side='right', padx=10, pady=10)
# brancoLb.pack(side='right', padx=10, pady=10)

janela.mainloop()
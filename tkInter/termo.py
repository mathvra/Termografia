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

    lb['text'] = 'Vermelho: {:.2f}%\nLaranja: {:.2f}%\nAmarelo: {:.2f}%\nVerde: {:.2f}%\nCiano: {:.2f}%\nAzul: {:.2f}%\nVioleta: {:.2f}%\nMagenta: {:.2f}%\nBranco: {:.2f}%'.format(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8])

janela = Tk()
janela.title('TermoCrivo v0.1')
janela["bg"] = "blue"
janela.geometry('1000x700+100+100')
panelA = None

bt = Button(janela, text="Select an image", command=select_image)
bt.pack(side="bottom", fill="both", padx="10", pady="10")

lb = Label(janela, text='Selecione uma imagem!')
lb.pack(side='top', padx=10, pady=10)

janela.mainloop()
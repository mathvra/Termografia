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
    progresso['text'] = 'Processando...'
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
        panelA.pack(side="top", padx=10, pady=10)

    else:
        panelA.configure(image=image)
        panelA.image = image

    lb['text'] = 'Identificação: {}\nData: {}\n============================\nVermelho: {:.2f}%\nLaranja: {:.2f}%\nAmarelo: {:.2f}%\nVerde: {:.2f}%\nCiano: {:.2f}%\nAzul: {:.2f}%\nVioleta: {:.2f}%\nMagenta: {:.2f}%\nBranco: {:.2f}%'.format(nome.get(), data.get(), resultado[0][0], resultado[1][0], resultado[2][0], resultado[3][0], resultado[4][0], resultado[5][0], resultado[6][0], resultado[7][0], resultado[8][0])
    progresso['text'] = 'Concluído!'
    return resultado

def salvar():
    fileName = fdlg.asksaveasfilename()
    try:
        file = open(fileName, 'w')        
        file.write(lb['text'])
    except:
        pass
    finally:
        file.close()

def sobre():
    root = Tk()
    root.wm_title("Sobre")
    texto=("TermoCrivo: Versão 0.1")
    textONlabel = Label(root, text=texto)
    textONlabel.pack()


janela = Tk()
janela.title('TermoCrivo v0.1')
janela["bg"] = "white"
janela.geometry('1080x720+250+0')
canvas = Canvas(janela, width = 939, height = 152)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("imgs/termocrivologo.png"))
canvas.create_image(0, 0, anchor=NW, image=img)
canvas["bg"] = "white"
panelA = None

nomelb = Label(text="Identificação:")
nomelb.place(x=90, y=200)
nomelb["bg"] = "white"
nome = Entry(janela)
nome.place(x=200, y=200)
nome["bg"] = "gray"

datalb = Label(text="Data (DD/MM/AA):")
datalb.place(x=90, y=250)
datalb["bg"] = "white"
data = Entry(janela)
data.place(x=200, y=250)
data["bg"] = "gray"

menubar = Menu(janela)
MENUarquivo = Menu(menubar)
MENUarquivo.add_command(label="Abrir", command=select_image)
MENUarquivo.add_command(label="Salvar", command=salvar)
menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

MENUajuda = Menu(menubar)
MENUajuda.add_command(label="Sobre", command=sobre)
menubar.add_cascade(label="Ajuda", menu=MENUajuda)
janela.config(menu=menubar)

lb = Label(janela, text='')

lb['bg'] = 'white'
lb.pack(side='top', padx=10, pady=10)

progresso = Label(janela, text='Nada a processar...', bd=1, relief=SUNKEN, anchor=W)
progresso.pack(side=BOTTOM, fill=X)

janela.mainloop()
# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import numpy as np
import tkinter.filedialog as fdlg
import cv2
from crivo import Crivo
import os

def select_image():
    global panelA
    global vermelhoImg
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
        panelA.pack(side="right", padx=10, pady=10)

    else:
        panelA.configure(image=image)
        panelA.image = image

    lb['text'] = 'Identificação: {}\nData: {}\n============================\nVermelho: {:.2f}%\nLaranja: {:.2f}%\nAmarelo: {:.2f}%\nVerde: {:.2f}%\nCiano: {:.2f}%\nAzul: {:.2f}%\nVioleta: {:.2f}%\nMagenta: {:.2f}%\nBranco: {:.2f}%'.format(nome.get(), data.get(), resultado[0][0], resultado[1][0], resultado[2][0], resultado[3][0], resultado[4][0], resultado[5][0], resultado[6][0], resultado[7][0], resultado[8][0])
    
    vermelho['text'] = 'Vermelho: {:.2f}%'.format(resultado[0][0])
    laranja['text'] = 'Laranja: {:.2f}%'.format(resultado[1][0])
    amarelo['text'] = 'Amarelo: {:.2f}%'.format(resultado[2][0])
    verde['text'] = 'Verde: {:.2f}%'.format(resultado[3][0])
    ciano['text'] = 'Ciano: {:.2f}%'.format(resultado[4][0])
    azul['text'] = 'Azul: {:.2f}%'.format(resultado[5][0])
    violeta['text'] = 'Violeta: {:.2f}%'.format(resultado[6][0])
    magenta['text'] = 'Magenta: {:.2f}%'.format(resultado[7][0])
    branco['text'] = 'Branco: {:.2f}%'.format(resultado[8][0])

    salvar.place(x=40, y=580, width=160, height=30)

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
janela["bg"] = "#333"
janela.geometry('1280x720+200+50')
canvas = Canvas(janela)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("imgs/termocrivologo2.png"))
canvas.create_image(35, 5, anchor=NW, image=img)
canvas.place(width='2000', height=50)
janela.iconbitmap(bitmap='2738favicon2.ico')

imgicon = PhotoImage(file='2738favicon2.ico')
janela.tk.call('wm', 'iconphoto', janela._w, imgicon)  

panelA = None
nomelb = Label(text="Identificação:", fg='white')
nomelb.place(x=40, y=80)
nomelb["bg"] = "#333"
nome = Entry(janela)
nome.place(x=40, y=100, width=150, height=25)
nome["bg"] = "gray"

datalb = Label(text="Data (DD/MM/AA):", fg='white')
datalb.place(x=40, y=130)
datalb["bg"] = "#333"
data = Entry(janela)
data.place(x=40, y=150, width=100, height=25)
data["bg"] = "gray"

abrir = Button(janela, text="Abrir", command=select_image)
abrir.place(x=140, y=150, width=50, height=25)

lb = Label(janela, text='')

resultado = Label(janela, text='Resultado:')
resultado['bg'] = 'white'

vermelho = Label(janela, text='')
vermelho['bg'] = 'white'
vermelho.place(x=45, y=220, width=150, height=20)
barraVermelho = Label(janela)
barraVermelho['bg'] = 'red'
barraVermelho.place(x=40, y=220, width=10, height=20)

laranja = Label(janela, text='')
laranja['bg'] = 'white'
laranja.place(x=45, y=260, width=150, height=20)

barraLaranja = Label(janela)
barraLaranja['bg'] = 'orange'
barraLaranja.place(x=40, y=260, width=10, height=20)

amarelo = Label(janela, text='')
amarelo['bg'] = 'white'
amarelo.place(x=45, y=300, width=150, height=20)
barraAmarelo = Label(janela)
barraAmarelo['bg'] = 'yellow'
barraAmarelo.place(x=40, y=300, width=10, height=20)

verde = Label(janela, text='')
verde['bg'] = 'white'
verde.place(x=45, y=340, width=150, height=20)
barraVerde = Label(janela)
barraVerde['bg'] = 'green'
barraVerde.place(x=40, y=340, width=10, height=20)

ciano = Label(janela, text='')
ciano['bg'] = 'white'
ciano.place(x=45, y=380, width=150, height=20)
barraCiano = Label(janela)
barraCiano['bg'] = 'cyan'
barraCiano.place(x=40, y=380, width=10, height=20)

azul = Label(janela, text='')
azul['bg'] = 'white'
azul.place(x=45, y=420, width=150, height=20)
barraAzul = Label(janela)
barraAzul['bg'] = 'blue'
barraAzul.place(x=40, y=420, width=10, height=20)

violeta = Label(janela, text='')
violeta['bg'] = 'white'
violeta.place(x=45, y=460, width=150, height=20)
barraVioleta = Label(janela)
barraVioleta['bg'] = 'purple'
barraVioleta.place(x=40, y=460, width=10, height=20)

magenta = Label(janela, text='')
magenta['bg'] = 'white'
magenta.place(x=45, y=500, width=150, height=20)
barraMagenta = Label(janela)
barraMagenta['bg'] = 'magenta'
barraMagenta.place(x=40, y=500, width=10, height=20)

branco = Label(janela, text='')
branco['bg'] = 'white'
branco.place(x=45, y=540, width=150, height=20)
barraBranco = Label(janela)
barraBranco['bg'] = 'gray'
barraBranco.place(x=40, y=540, width=10, height=20)

salvar = Button(janela, text="Salvar", command=salvar)

progresso = Label(janela, text='Nada a processar...', bd=1, relief=SUNKEN, anchor=W)
progresso.pack(side=BOTTOM, fill=X)

janela.mainloop()
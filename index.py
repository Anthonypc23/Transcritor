import tkinter as tk
from utils import BuscarArquivo
from utils import Transcrever

def Seleciona_arquivo():
    caminho  = BuscarArquivo()
    if caminho:
        label.config(text=f"Arquivo selecionado: \n {caminho}")
        Transcrever(caminho)

window = tk.Tk()

window.geometry("600x600")
window.title("Transcritor")
label = tk.Label(window, text="Busque uma Arquivo de Audio !", font=("Arial",14))
label.pack()
botao = tk.Button(window, text="Bucar", command= Seleciona_arquivo)
botao.pack()
label = tk.Label(window, text="Nenhum Arquivo Selecionado", font=("Arial",14))
label.pack()
window.mainloop()


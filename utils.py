from tkinter import filedialog
import whisper
import os


def BuscarArquivo():
    path = filedialog.askopenfilename(
        title= "Selecione um Arquivo",
        filetypes=(("Todos os Arquivos", "*"),)
    )
    return path

def Transcrever(caminho:str):
    modelo = whisper.load_model("base")
    
    texto = modelo.transcribe(caminho)
    print(texto["text"])
    if texto:
        EscreverArquivo(texto["text"])

def EscreverArquivo(texto):
    with open("legenda.txt", "w", encoding="utf-8") as legenda:

        legenda.write(texto)

    os.system("notepad legenda.txt")



    
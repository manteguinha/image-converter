from PIL import Image
import os

lista_arquivos = os.listdir(".")

for arquivo in lista_arquivos:
    try:
        os.mkdir('./Convertidas')
        print('Pasta criada')
    except:
        pass

    if arquivo.endswith(".jpeg"):
        imagem = Image.open(arquivo)
        imagem.save(f'Convertidas/{arquivo.replace(".jpeg", ".png")}')
        os.remove(arquivo)
        print("Convertido: " + arquivo)
    else:
        print("Não foi possível converter: " + arquivo)

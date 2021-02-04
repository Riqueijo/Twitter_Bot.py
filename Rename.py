import os


for nome in os.listdir('./fotos'):
    dados = str(nome).split(".")
    numero = dados[0].split("_")[1]
    subnumero = dados[1]
    novo_nome = numero + "_" + subnumero + ".jpg"

    os.rename("./fotos" + nome, "./fotos" + novo_nome)
    print("arquivo " + nome + " alterado para " + novo_nome)
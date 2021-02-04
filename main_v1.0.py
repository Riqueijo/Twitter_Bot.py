import tweepy
import os
from random import randint


def db(file):
    arquivo = open(file, 'r')
    historico = arquivo.read().strip()
    arquivo.close()
    return historico


def banco_armazenar(historico):
    arquivo = open('db.txt', 'a')
    arquivo.write(f'{historico} \n')


consumer_key = 'D3vHIJXY3XSgfGm26UM7PaLV6'
consumer_secret = 'BMVoiHCUi6HkQadtw0XSFNb6ZvZB74mKsMHtOkQh2uq4izVxes'
access_key = '1203454489077993472-oSaatY1f5rjqPcYQigmiqR8ObF5mF1'
access_secret = 'mPDDp44YLLoLASzhqCN3diGeaXY0BdIS1Rem3E4WMGRsF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #login tweepy
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

############################################### escolhe a foto
lista = os.listdir('C:/Users/dague/PycharmProject/twitter_bot/bot 2/fotos') #cria a lista de documentos
numero_de_docs = len(lista) #conta a lista
intervalo = randint(0, numero_de_docs -1) #escolhe um elemento da lista

#banco_armazenar(intervalo)
escolher_foto = lista[intervalo]
api.update_with_media(escolher_foto)



from ugcnormal import Normalizador

normalidador = Normalizador()

texto = "no ultimo fds fiz uma conpra pela net de um smartfone e jah to usando ele, eh incrivel a tecnologia: tem wifi, blutoth, etc....."
arquivo = open('arquivo.txt', 'rb')

conteudo = texto

resultado = normalidador.recebe_texto(6, 1, conteudo)
print resultado

from classes.GerenciarS3 import GerenciarS3
controla_S3 = GerenciarS3('aulanoitecamila')
controla_S3.lista_arquivos()
controla_S3.delete_arquivo('index.html')
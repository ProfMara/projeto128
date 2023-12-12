from bs4 import BeautifulSoup
import requests
import pandas as pd 
#LINK DA PAGINA DE ESTRELAS ANÃS MARRONS
link = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

#------------------------------------------------#
#---------------      PARTE 1   -----------------#
#---------------   CSV COMPLETO   ---------------#
#------------------------------------------------#

#obter a página


#obtenha a análise da página em python


#tabela de estrelas <table> com a classe 'wikitable sortable'


#crie a lista de todas as estrelas


#acesse o tbody da tabela de estrelas

#guarde todas as linhas <tr> da tabela 


#para cada linha, acesse os dados da coluna

    #guarde os dados da coluna <td>
    
    
    #repete para cada coluna
    
        #guarda o texto com a info daquela coluna
        
        #add na linha de dados o dado
        
    #add a lista de dados da estrela na lista de estrelas
    
#mostre o resultado


#defina os nomes das colunas
headers = [
    "Star", "Constellation", "Right Ascension", "Declination",
    "App. Mag.", "Distance", "Spectral Type", "Brown Dwarf", "Mass",
    "Radius", "Orbital Period", "Semimajor axis", "Ecc.", "Discovery Year"
]
#converta a lista de estrelas em um dataframe

#converta o dataframe em um arquivo csv


#------------------------------------------------#
#---------------      PARTE 2   -----------------#
#---------------   CSV RESUMIDO   ---------------#
#------------------------------------------------#

#lista de dados
listaNome = []
listaDistancia = []
listaMassa = []
listaRaio = []

#repete para cada estrela da lista

    #add o nome da estrela na lista
    
    #add a distancia da estrela da Terra na lista
    
    #add o peso da estrela na lista de peso
    
    #add o tamanho da estrela na lista de tamanho
    

headers = [
    "Star_name", "Distance", "Mass", "Radius"
]

#combinar as listas em uma variável só


#convertendo a lista final em dataframe


#convertendo o dataframe em arquivo csv com índices

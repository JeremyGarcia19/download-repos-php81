#Autor:       Jeremy García Meneses
#Fecha:       17/10/2022
#Descripción: Script para descargar los paquetes rpm de php81

import re
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Instanciación de objeto para opciones
OPCIONES_NAV = Options()
#Permitimos ejecución con chrome en segundo plano
OPCIONES_NAV.add_argument("--headless")
OPCIONES_NAV.add_argument('--disable-blink-features=AutomationControlled')
#Definición de la ruta del driver
DRIVER_PATH = 'webdrivers/chromedriver.exe'
#Instancición de objeto webdriver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#Obtención de la página repositorio de archivos rpm
#driver.get('https://rpms.remirepo.net/enterprise/7/php81/x86_64/')
driver.get('http://fr2.rpmfind.net/linux/remi/enterprise/7/php81/x86_64/')

#Obtención de todos los links
tabla = driver.find_element(By.TAG_NAME,'table')

tr = tabla.find_elements(By.TAG_NAME,'tr')

lista = []
for t in tr:
  td = t.find_elements(By.TAG_NAME,'a')
  for element in td:
    lista.append(element.get_attribute('href'))
#Fin webscraping
driver.quit()

#Escribimos la url en un archivo
with open('Recursos/links.txt','w') as archivo:
  for elemento in lista:
    archivo.write(elemento)
    archivo.write("\n")

#Filtrado de url
#url_modulos = []
#with open('Recursos/lista-modulos.txt','r') as archivo:
#  lineas = archivo.readlines()
#  for linea in lineas:
#    url_modulos.append(linea[:-1])
#  print(url_modulos)

url_modulos = [
'php-8',
'mcrypt',
'mysql',
'cli',
'ssh2',
'openssl',
'json',
'pdo',
'bcmath',
'ctype',
'fileinfo',
'mbstring',
'pdo',
'tokenizer',
'xml',
'dom',
'devel',
'pear',
'gd',
'soap']

filtrados = []

with open('Recursos/linksfiltrados.txt','w') as archivo:
  for elemento in lista:
    for i in range(len(url_modulos)):
      #print(modulo)
      if url_modulos[i] in elemento:
        print(url_modulos[i])
        archivo.write(elemento)
        archivo.write("\n")
        filtrados.append(elemento)


#for url in filtrados:
  #wget.download(url, out='RPM-PHP')

for url in lista:
  wget.download(url, out='RPM-PHP')
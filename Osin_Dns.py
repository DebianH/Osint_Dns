import subprocess, socket, os, re
from pyfiglet import Figlet
import requests
from bs4 import BeautifulSoup
import urllib.request 
import json
import dns.resolver



os.system('cls')

desk=Figlet(font='slant')
print (desk.renderText('Dns GH'))  #Banner :)


dom= input('Ingrese dominio: ')
print("Ip del servidor: ")
print(socket.gethostbyname(dom))


datos = socket.gethostbyaddr(dom)

iplist = datos[2]

for ip in iplist:
	respuesta = os.popen(f"ping {ip}").read()
	if "Received = 4" in respuesta:
		print(f"Servidor Activo {dom}")

	else:
		print("Servidor asignado NO permite Ping")



print("\n______Busqueda Domios en el mismo servidor______\n")


agent = {'User-Agent':'Firefox'}
consulta = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(dom),headers=agent)

parse=BeautifulSoup(consulta.text, 'html5lib')
analizar=parse.find(id="null")
analizar1=analizar.find(border="1")

for i in analizar1.find_all("tr"):
	print('[+] Sitios encontrados en el mismo servidor: ' + i.td.string)



print("\n______Busqueda Geolocalizacion______\n")
#Geolocalizacion de servidor

ip = "".join(iplist)    #convierte la lista en string para poder concatenar
url ="https://ipinfo.io/"+ip+"/json"
abrirURL=urllib.request.urlopen(url)
cargaURL=json.load(abrirURL)

for i in cargaURL:
	print(i+":"+cargaURL[i])

print("\n______Busqueda Subdominios______\n")

def DomainSec():
	file = open("base.txt")
	content = file.read()
	subdomains = content.splitlines()

	for subdomain in subdomains:
		url= f"http://{subdomain}.{dom}"
		try:
			requests.get(url)
		except requests.ConnectionError:
			pass
		else:
			print("[+] Dominio encontrado: ", url)

DomainSec()



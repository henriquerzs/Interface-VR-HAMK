#!/usr/bin/env python
 
import json
from watson_developer_cloud import VisualRecognitionV3
#from watson_developer_cloud.visual_recognition_v3 import VisualRecognitionV3
import cgi
print "Content-type: text/html"
print



# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key='8b916c3ab946fd1da094dd1a48cb8b3e9ac46a3f')

#URL da imagem a ser classificada
url_image='http://www.americareadsspanish.org/images/stories/amigos_espanol/angelina-jolie-2.jpg'


# Detectar Faces de uma imagem por URL
Resultados = VR.detect_faces(images_url=url_image)

#Mostra o resultado no formato json
ResultadoJson = json.dumps(Resultados, indent=2)

#formulario = cgi.FieldStorage()
#nome = formulario.getvalue("nome")
#url_image = formulario.getvalue("url")

nome="HENRIQUE"
url_image="URL QUALQUER"

print "<title>Test CGI</title>"
print "<p>Ola MUNDO!</p><br>"
substituir = (''' 
<p>%s</p><br>
<p>%s</p><br>
<p>%s</p>

''')

print substituir % (nome,url_image,ResultadoJson)
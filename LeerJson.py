import json
import re
from re import search


class LecturaJSon:
    def __init__(self, archivo):
        self.archivo = archivo

    def read(self):
        return json.loads(open(self.archivo).read())



leer = LecturaJSon("datos.json").read();
my_regexNombre = re.compile("(?P<nombre>[a-zA-Z]+)")
my_regexEdad = re.compile("(?P<edad>\d+)")
my_regexCorreo = re.compile("(?P<correo>[a-zA-Z]+@+[a-zA-Z].*)")

i = 0
while i < len(leer):

    print(my_regexNombre.search(leer[i]["nombre"]).group())
    print(my_regexEdad.search(str(leer[i]["edad"])).group())
    print(my_regexCorreo.search(leer[i]["correo"]).group())
    i += 1

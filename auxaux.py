# -*- coding: utf-8 -*-
def Reemplazo_utf8_To_ne(Texto):
    Texto = Texto.encode("utf8")
    lista = [['\\xc3\\xb17','ñ']]
    resultado = Texto.replace(lista[0][0], lista[0][1])

    return resultado

texto = 'hola ñe'
#texto = texto.encode('utf-8')
res =Reemplazo_utf8_To_ne(texto)

a = 'ñ'
d = a.encode("utf8")

b = a.encode("ascii")
#c = a.decode("utf-8")

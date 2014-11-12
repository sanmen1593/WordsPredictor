import numpy as np

class Predictor():
    def __init__(self):
        self.listaDiccionarios = []
        self.diccionarioPalabras = {}
        self.listaPalabras = []

    def delEspChar(self,texto):
        texto = texto.replace(':','')
        texto = texto.replace('?','')
        texto = texto.replace(';','')
        texto = texto.replace('-','')
        texto = texto.replace('_','')
        texto = texto.replace(')','')
        texto = texto.replace('(','')
        texto = texto.replace('!','')
        texto = texto.replace(',','')
        texto = texto.replace('"','')
        texto = texto.replace('\'','')
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        return texto

    def divParrafos(self):
        lista = []
        archi = open('dictionary.txt', 'r')
        linea = archi.readline()
        while linea != '':
            if not linea.startswith("#"):
                if(linea != "\n"):
                    linea = self.delEspChar(linea)
                    lista.append(linea)
            linea = archi.readline()
        archi.close()
        return lista

    def divPalabras(self):
        self.diccionarioPalabras = {}
        totalpalabras = 0
        lista = self.divParrafos()
        for i in range(len(lista)):
            palabra = str.split(lista[i],' ')
            for j in range(len(palabra)):
                if not palabra[j] in self.diccionarioPalabras:
                    if not palabra[j]=='':
                        self.listaPalabras.append(palabra[j])
                        self.diccionarioPalabras[palabra[j]] = self.listaPalabras.index(palabra[j])
                        self.listaDiccionarios.append({'total':0})
                        totalpalabras = totalpalabras+1
                        if j<len(palabra)-1:
                            self.compararPalabras(palabra[j],palabra[j+1],self.diccionarioPalabras[palabra[j]])

    def compararPalabras(self, palabraActual, palabraSiguiente, posPA):
        if(palabraActual == self.listaPalabras[posPA]):
            print(palabraActual+" "+palabraSiguiente)
            if(self.listaDiccionarios[posPA].has_key(palabraSiguiente)):
                self.listaDiccionarios[posPA][palabraSiguiente] = self.listaDiccionarios[posPA][palabraSiguiente]+1
                self.listaDiccionarios[posPA]['total'] = self.listaDiccionarios[posPA]['total']+1
            else:
                self.listaDiccionarios[posPA][palabraSiguiente] = 1
                self.listaDiccionarios[posPA]['total'] = self.listaDiccionarios[posPA]['total']+1

predictor = Predictor()
predictor.divPalabras()
print(predictor.diccionarioPalabras)
print('')
print(predictor.listaPalabras)
print(predictor.listaDiccionarios[0]['and'])

array = np.ones((2,len(predictor.listaPalabras)),float)
array = np.zeros_like(array)
print(array)
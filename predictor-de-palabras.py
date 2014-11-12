import numpy as np

class Predictor():
    # Declaramos las variables que utilizaremos:
    # 1. La lista de palabras
    # 2. Diccionario de palabras que sigue la forma 'palabra': posicion, donde la
    # posicion es la de esa palabra en la lista de palabras.
    # 3. Diccionario Palabras, donde guardaremos los diccionarios de las palabras
    # que vienen despues de la correspondiente palabra en cada posicion.
    def __init__(self):
        self.listaDiccionarios = []
        self.diccionarioPalabras = {}
        self.listaPalabras = []

    #Eliminamos del texto (todo el texto), los caracteres especiales que no nos interesan
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

    #Dividiemos el texto en parrajos segun los saltos de linea.
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

    #Aqui llama a divParrafos para dividir en parrafos, y luego con cada parrafo,
    #saca todas las palabras
    def divPalabras(self):
        self.diccionarioPalabras = {}
        totalpalabras = 0
        lista = self.divParrafos()
        for i in range(len(lista)):
            palabra = str.split(lista[i],' ')
            for j in range(len(palabra)):
                if not palabra[j] in self.diccionarioPalabras:
                    if not palabra[j]=='': #Si la 'palabra' no es vacia
                        self.listaPalabras.append(palabra[j]) #guarda en la lista de palabras
                        #Guardamos en el diccinario la palabra junto con su posicion:
                        self.diccionarioPalabras[palabra[j]] = self.listaPalabras.index(palabra[j])
                        #Creamos el diccionario con las palabras que vienen despues
                        self.listaDiccionarios.append({'total':0})
                        totalpalabras = totalpalabras+1 #Totaldepalabras
                        if j<len(palabra)-1:
                            #Comparamos la palabra actual con la siguiente para llenar el diccionario de frecuencias
                            self.compararPalabras(palabra[j],palabra[j+1],self.diccionarioPalabras[palabra[j]])

    def compararPalabras(self, palabraActual, palabraSiguiente, posPA):
        if(palabraActual == self.listaPalabras[posPA]):
            print(palabraActual+" "+palabraSiguiente)
            if(self.listaDiccionarios[posPA].has_key(palabraSiguiente)):
                #Si la palabra siguiente ya esta (antes ya estuvo despues de la palabra actual)
                #se le suma 1 a la frecuencia
                self.listaDiccionarios[posPA][palabraSiguiente] = self.listaDiccionarios[posPA][palabraSiguiente]+1
                self.listaDiccionarios[posPA]['total'] = self.listaDiccionarios[posPA]['total']+1
            else:
                #Si la palabra siguiente no esta, entonces se crea con el valor de uno.
                self.listaDiccionarios[posPA][palabraSiguiente] = 1
                self.listaDiccionarios[posPA]['total'] = self.listaDiccionarios[posPA]['total']+1
                #En ambos casos, sumamos 1 al total (para luego dividir y sacar la probabilidad)

predictor = Predictor()
predictor.divPalabras()
print(predictor.diccionarioPalabras)
print('')
print(predictor.listaPalabras)
print(predictor.listaDiccionarios[0]['and'])

#Creamos la matriz de probabilidades p
p = np.ones((2,len(predictor.listaPalabras)),float)
p = np.zeros_like(p)
print(p)

#Creamos el arreglo de probabilidades iniciales a
a = np.ones( (1,len(predictor.listaPalabras)),float)
a = np.zeros_like(a)
print(a)

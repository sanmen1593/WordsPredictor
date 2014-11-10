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
        texto = texto.replace('\n', '')
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
                        totalpalabras = totalpalabras+1
                        if j<len(palabra)-1:
                            self.compararPalabras(self.diccionarioPalabras[palabra[j]],palabra[j+1],self.diccionarioPalabras[palabra[j]])

    def compararPalabras(self, palabraActual, palabraSiguiente, posPA):
        print("---")

predictor = Predictor()
predictor.divPalabras()
print(predictor.diccionarioPalabras)
print(predictor.listaPalabras)
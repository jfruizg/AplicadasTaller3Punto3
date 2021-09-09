abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
listaAbecedario = list(abecedario)
matrizAbecedario = []
alphabet_list = list(abecedario)


for i in range(0, len(abecedario)):
    matrizAbecedario.append(i)

def algortimoRSA(mensaje, clave_e, clave_n):
    hola = ""
    result = ""
    for i in range(0,len(mensaje)):
        for j in range(0,len(matrizAbecedario)):
            """se busca elevar al cuadrado (primer paso)"""
            contadorMultiplo = matrizAbecedario[i] ** clave_e
            print(contadorMultiplo)
            """Se saca el modulo del resultado elevado (Segundo paso)"""
            modulo = contadorMultiplo % clave_n

            if(str(modulo) == mensaje):
                result = result + str(modulo)
                hola = hola + alphabet_list[matrizAbecedario[i]]
                return hola


def primeraLetra(mensaje):
    result = ""
    for i in range(0,3):
        result = result + mensaje[i] + " "


mensajeAlicia = "26 2 15 16 6 0 13"
mensaje = mensajeAlicia.split()
mensajeBenito = "22 8 10 9 18 0"

n_alicia = 33
e_alicia = 7

n_benito = 39
e_benito = 5

print(algortimoRSA(mensaje,e_alicia,n_alicia))











def aplicarNumerosAbecedario(abecedario):
    matriz = []
    for i in range(0, len(abecedario)):
        matriz.append(i)
    return matriz

def algortimoRSA(listaMensaje, clave_e, clave_n,matrizAbc,listaAbecedario):
    resultado_algoritmo = ""
    result = ""
    contador1= 0
    for i in range(0,len(listaMensaje)):
        for j in range(0,len(matrizAbc)):
            """se busca elevar a la clave e (primer paso)"""
            contador1 = matrizAbc[j] ** clave_e
            """Se saca el modulo del resultado elevado (Segundo paso)"""
            modulo = contador1 % clave_n

            if(str(modulo) == listaMensaje[i]):
                result = result + str(modulo)
                resultado_algoritmo = resultado_algoritmo + listaAbecedario[matrizAbc[j]]
    return resultado_algoritmo

def primeraLetra(mensaje):
    result = ""
    for i in range(0,3):
        result = result + mensaje[i]
    return result



if __name__ == '__main__':
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    listaAbecedario1 = list(abecedario)
    matrizNumero = aplicarNumerosAbecedario(abecedario)

    mensajeAlicia = "26 2 15 16 6 0 13".split()
    mensajeBenito = "22 8 10 9 18 0".split()

    clave_n_alicia = 33
    clave_e_alicia = 7

    clave_n_benito = 39
    clave_e_benito = 5

    resultadoAlicia = algortimoRSA(mensajeAlicia,clave_e_alicia,clave_n_alicia,matrizNumero,listaAbecedario1)
    resultadoBenito = algortimoRSA(mensajeBenito, clave_e_benito, clave_n_benito, matrizNumero, listaAbecedario1)

    print(resultadoAlicia)
    print(resultadoBenito)
    print(primeraLetra(resultadoAlicia))
    print(primeraLetra(resultadoBenito))

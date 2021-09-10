def numberAphabet(abc):
    array = []
    for i in range(0, len(abc)):
        array.append(i)
    return array

def algorithmRSA(messageList, password_e, password_n,abcArray,abcList):
    algorithm_result = ""
    result = ""
    cont= 0
    for i in range(0,len(messageList)):
        for j in range(0,len(abcArray)):
            """se busca elevar a la clave e (primer paso)"""
            cont = abcArray[j] ** password_e
            """Se saca el modulo del resultado elevado (Segundo paso)"""
            modulo = cont % password_n

            if(str(modulo) == messageList[i]):
                result = result + str(modulo)
                algorithm_result = algorithm_result + abcList[abcArray[j]]
    return algorithm_result

def threeLetter(menssge):
    result = ""
    for i in range(0,3):
        result = result + menssge[i]
    return result

if __name__ == '__main__':
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abcList = list(abc)
    numberArray = numberAphabet(abc)

    aliciaMessage = "26 2 15 16 6 0 13".split()
    benitoMessage = "22 8 10 9 18 0".split()

    password_n_alicia = 33
    password_e_alicia = 7

    password_n_benito = 39
    password_e_benito = 5

    aliciaResult = algorithmRSA(aliciaMessage,password_e_alicia,password_n_alicia,numberArray,abcList)
    benitoResult = algorithmRSA(benitoMessage, password_e_benito, password_n_benito, numberArray, abcList)

    print(aliciaResult)
    print(benitoResult)
    print(threeLetter(aliciaResult))
    print(threeLetter(benitoResult))

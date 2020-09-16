# Fazer ese desafio depois
def sockMerchant(ar):
    
    rigth = []
    left = []
    lose = []

    loop = len(ar)
    
    test = 0

    for element in ar:

        if(element % 2 == 0):
            rigth.appen'd(element)

        elif(element % 3 == 0):
            left.append(element)

    print(rigth)

    if len(rigth) % 2 == 1:
        
        rm = len(rigth)

        valueRight = rm / 2

        print(valueRight)

    else:
        rm = len(rigth) - 1
        lose.append(1)

        rigth.pop(1)

        print("Eu sou a cor 2 mas tive que escluir um pé que estava sem par", rigth)

if __name__ == '__main__':
    
    ar = [1,2,1,2,1,3,2,4,4,4,6]

    sum(ar)
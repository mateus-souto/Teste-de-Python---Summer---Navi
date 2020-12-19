import numpy as np
import math

vetor = []

for i in range (10):

    if (i % 2 == 0 ):
        valor = 3**i+7*(math.factorial(i))
    else:
        valor = 2**i+4*(math.log(i))

    vetor.append(valor)


print("A posição do maior elemento é",np.argmax(vetor))

print("A média dos elementos é",np.mean(vetor))

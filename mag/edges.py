import matplotlib.pyplot as plt
import numpy as np

tam = 100
erro = 0.001

a = np.zeros([tam, tam + 2])
b = np.copy(a)
kernel = np.array([
    [0, 0.25, 0],
    [0.25, 0, 0.25],
    [0, 0.25, 0]
])
# b = np.zeros([tam+2, tam])
c = 1

a[:, 0] = 10
a[:, tam + 1] = -10

while erro < c:
    for i in range(tam):
        for j in range(1, tam + 1):
            try:
                fator1 = a[i, j+1]
            except:
                fator1 = 0
            try:
                fator2 = a[i, j-1]
            except:
                fator2 = 0
            try:
                fator3 = a[i+1, j]
            except:
                fator3 = 0
            try:
                fator4 = a[i-1, j]
            except:
                fator4 = 0
            a[i,j] = (fator1 + fator2 + fator3 + fator4)/4

    c = np.max(np.abs(a-b))
    b = np.copy(a)

plt.matshow(a)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

tam = 100
erro = 0.001

offset_x = 1
offset_y = 1

a = np.zeros([tam, tam])
a[offset_y:tam-offset_y, offset_x] = 10
a[offset_y:tam-offset_y, tam - offset_x - 1] = -10

b = np.copy(a)
c = 1

kernel = np.array([
    [0, 0.25, 0],
    [0.25, 0, 0.25],
    [0, 0.25, 0]
])

while erro < c:
    for i in range(tam):
        for j in range(tam):
            if a[i, j] == 10 or a[i, j] == -10:
                continue

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

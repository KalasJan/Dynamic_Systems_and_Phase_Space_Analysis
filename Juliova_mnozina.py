# vykreslete Juliovy mnoziny - casti Mandelbrota


import numpy as num #numerika
import matplotlib.pyplot as plt

vyska, sirka = 800, 800 #rozliseni
min_x, max_x = -1.5, 1.5 #jsme v rovine abs(z)<=2
min_y, max_y = -1.5, 1.5 # nechceme celou rovinu, staci kousek
iter_max = 100 # max pocet iteraci

# mrizka v C
x = num.linspace(min_x, max_x, vyska)
y = num.linspace(min_y, max_y, sirka)
X, Y = num.meshgrid(x,y) 
z = X + Y*1j # tvar komplexniho cisla, musi byt 1j

# konstanta ci - pokaždé vyjde jiny tvar
c1 = -0.4 + 0.6j
c2 = -0.8 + 0.156j
c3 = -0.7269 + 0.1889j
konstanty = [c1, c2, c3] # hodnoty generovany AI

# vykresleni jednotlivych mnozin (podle konstanty ci)
fig, osy = plt.subplots(1, 3, figsize=(15, 5))

# generovani mnozin
for i, c in enumerate(konstanty):
    Z = z.copy()
    iterace = num.zeros(Z.shape, dtype=int)
    
    # mnozina samotna
    for k in range(iter_max):
        obraz = num.abs(Z) <= 2  # abs hodnota max 2
        Z[obraz] = Z[obraz] ** 2 + c  # vzorec s pevnou konstantou c
        iterace[obraz] = k
    
    # samotne mnoziny
    ax = osy[i]
    im = ax.imshow(iterace, extent=(min_x, max_x, min_y, max_y), cmap='plasma')
    ax.set_title(f'c = {c}')
    ax.set_xlabel('Reálná část')
    ax.set_ylabel('Imaginární část')
    
plt.suptitle('Juliovy množiny - 3 různé části Mandelbrotovy množiny')
plt.tight_layout()
plt.show()
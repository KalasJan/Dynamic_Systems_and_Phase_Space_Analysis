# nakreslete Mengerovu houbu (metoda Sierpinskeho trojuhelniku v krychli)

import matplotlib.pyplot as plt
import numpy as np

def menger(hloubka):
    n = 3**hloubka
    i, j, k = np.indices((n, n, n))
    kostka = np.ones((n, n, n), dtype=bool)
    # plna kostka
    
    # odstranovani prostredni casti
    for h in range(hloubka):
        # Zjistíme pozici uvnitř aktuálního 3x3x3 bloku (0, 1 nebo 2)
        ii = (i // 3**h) % 3
        jj = (j // 3**h) % 3
        kk = (k // 3**h) % 3

    # Mengerova podmínka: středy stěn a středy krychle mají alespoň dvě souřadnice rovné 1
        stredova_maska = (ii == 1) & (jj == 1) | (ii == 1) & (kk == 1) | (jj == 1) & (kk == 1)

    # Odstraníme tyto středy ze zbývající struktury
        kostka[stredova_maska] = False

    return kostka

# kvykresleni 1 kostky
hloubka1 = 2

data = menger(hloubka1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')

ax.voxels(data, facecolors='gray', edgecolor='k', linewidth=0.2)

plt.title(f'Mengerova kostka, do {hloubka1} iterace')

# ===================================================
# kostky vedle sebe (porovnani iteraci)

seznam_iteraci = [1, 2, 3]

fig2, osy = plt.subplots(1, 3, subplot_kw={'projection': '3d'}, figsize=(15, 5))

for idx, hloubka in enumerate(seznam_iteraci):
  data = menger(hloubka)

  axes = osy[idx]
  axes.voxels(data, facecolors='cyan', edgecolor='k', linewidth=0)
  axes.set_title(f'Iterace = {hloubka}')
  axes.axis('off')

fig2.suptitle('Mengerova kostka / houba - porovnání hloubek')
plt.tight_layout()

plt.show()
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

### Crée le plan 3D #########
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#################################################
### titre du plan 3D ########
ax.set_title('axes Lazarus')
## Afiché l'image  Background #####
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.grid(False)
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False


## plan des Axes invisibles
#ax._axis3don = False ##rendre le graph Invisible !!! Axes Plan !!!!! attention

###################################################



# chaines des listes pour les dns et axes X , Y , Z
types = ['dns_1', 'dns_2', 'dns_3', 'dns_4', 'dns_5']
X = [120, 50, 120, 175,200] # Longueur X de 0 a 200 max
Y = [100, 150, 150, 150,150]   # Largeur Y de 0 a 150 max
Z = [100, 100, 100, 100,100]   # Hauteur de 0 a 170 max


#ax.scatter(X,Y,Z, color='b',s=100) ## color point blue taille s=100


for i, type in enumerate(types):        # enumeration des données sur les points scatter en txt
     x = X[i]
     y = Y[i]
     z = Z[i]
     ax.scatter(x, y, z, marker="^", color='r', s=100)  #point violet taille 100
     ax.text(x+0.3, y+0.3, z+0.3, type, color="g", fontsize=9)      # text a +0.3 du point taille 9
     ax.plot(X,Y,Z, color='b')                 #ajout des connexions lignes en bleu



######### INFOS ########################
ax.set_xlabel("Longueur X")
ax.set_ylabel("Largeur Y")
ax.set_zlabel("Hauteur H")

plt.show()





############ 360 degrée ################
#for angle in range(0, 360):
    #ax.view_init(30, angle)
    #plt.draw()

    #plt.pause(.001)
    #plt.show()
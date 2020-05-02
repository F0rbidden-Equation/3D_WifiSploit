import subprocess
import pandas




import subprocess

out, err = subprocess.Popen(['nmcli -t -f ssid dev wifi'],shell=True, stdout=subprocess.PIPE).communicate()
out = out.decode('utf-8').splitlines()
print(out)
print("")

print(len(out)) ### compté
# numpy pour les x,y,z
N = (len(out))
 ###### Plan graphical ######
import numpy as np
import matplotlib.pyplot as plt



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

### Crée le plan 3D #########
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#################################################
### titre du plan 3D ########
ax.set_title('axes Lazarus')


## plan des Axes invisibles
#ax._axis3don = False ##rendre le graph Invisible !!! Axes Plan !!!!! attention

###################################################



# chaines des listes pour les dns et axes X , Y , Z
types = [out]
X = np.random.rand(N)
Y = np.random.rand(N)
Z = np.random.rand(N)


ax.scatter(X,Y,Z, color='r',s=100) ## color point blue taille s=100

for i, type in enumerate(types):

     x = X[i]
     y = Y[i]
     z = Z[i]
     ax.scatter(x, y, z, marker="^", color='g', s=600)  #point violet taille 100
     ax.text(x+0.3, y+0.3, z+0.3, out, fontsize=9)      # text a +0.3 du point taille 9
     #ax.plot(X,Y,Z, color='b')                 #ajout des connexions lignes en bleu



######### INFOS ########################
ax.set_xlabel("Longueur X")
ax.set_ylabel("Largeur Y")
ax.set_zlabel("Hauteur H")
plt.show()
## testé avec numpy c est mieux je pense!!
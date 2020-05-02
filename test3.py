import subprocess
import pandas


import mpl_toolkits.mplot3d.axes3d as p3

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

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(111, projection='3d')





#################################################
### titre du plan 3D ########
ax.set_title('axes Lazarus')


## plan des Axes invisibles
#ax._axis3don = False ##rendre le graph Invisible !!! Axes Plan !!!!! attention

###################################################
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.grid(False)
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False


# chaines des listes pour les dns et axes X , Y , Z
types = [out]
X = np.random.rand(N)
Y = np.random.rand(N)
Z = np.random.rand(N)


for i,type in enumerate(out):
    x = X[i]
    y = Y[i]
    z = Z[i]
    ax.scatter(x, y, z,color='r', s=15)  # point violet taille 100
    ax.text(x + 0.0, y + 0.0, z + 0.0, type, color='w', fontsize=7)


    #ax.legend(label=type)

    #ax.scatter(x, y, z, color='g', s=12)
    #ax.plot(X,Y,Z, color='m') #JAMMER !!!





plt.show()






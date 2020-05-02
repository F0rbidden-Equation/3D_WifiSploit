from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np
from pylab import *
import subprocess

out, err = subprocess.Popen(['nmcli -t -f ssid dev wifi'],shell=True, stdout=subprocess.PIPE).communicate()
out = out.decode('utf-8').splitlines()
print(out)
print("")

print(len(out)) ### compté
# numpy pour les x,y,z
N = (len(out))

# Create an empty list
My_list = []

# Value to begin and end with
start, end = 1, N

# Check if start value is smaller than end value
if start < end:
  # unpack the result
  My_list.extend(range(start, end))
  # Append the last value
  My_list.append(end)

# Create an empty list
My_list = []


m = rand(N,N)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(m)): # plot each point + it's index as text above
  x = m[i,0]
  y = m[i,1]
  z = m[i,2]
  label = i
  ax.scatter(x, y, z, color='b')
  ax.text(x, y, z, '%s' % (label), size=20, zorder=1, color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

for angle in range(0, 360):
  ax.view_init(30, angle)
  plt.draw()
  plt.pause(.001)
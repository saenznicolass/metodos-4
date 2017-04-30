# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


#tipo de graficas obtenidas de: 
#http://nbviewer.jupyter.org/github/barbagroup/CFDPython/blob/master/lessons/07_Step_5.ipynb


x = np.linspace(0,1,100)
y = np.linspace(0,1,100)




a = np.loadtxt("t0fC1.txt")
fig1 = plt.figure(dpi= 1000)
ax = fig1.gca(projection="3d")
X, Y = np.meshgrid(x,y)
a1 = ax.plot_surface(X,Y,a, cmap=cm.plasma)
cb = fig1.colorbar(a1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion fija, t = 0")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t0fC1.png")


b = np.loadtxt("t0fC2.txt")
fig2 = plt.figure(dpi= 1000)
ax = fig2.gca(projection="3d")
X, Y = np.meshgrid(x,y)
b1 = ax.plot_surface(X,Y,b, cmap=cm.plasma)
cb = fig2.colorbar(b1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion fija, t = 0")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t0fC2.png")

c = np.loadtxt("t100fC1.txt")
fig3 = plt.figure(dpi= 1000)
ax = fig3.gca(projection="3d")
X, Y = np.meshgrid(x,y)
c1 = ax.plot_surface(X,Y,c, cmap=cm.plasma)
cb = fig3.colorbar(c1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion fija, t = 100")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t100fC1.png")


d = np.loadtxt("t100fC2.txt")
fig4 = plt.figure(dpi= 1000)
ax = fig4.gca(projection="3d")
X, Y = np.meshgrid(x,y)
d1 = ax.plot_surface(X,Y,d, cmap=cm.plasma)
cb = fig4.colorbar(d1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion fija, t = 100")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])

plt.savefig("t100fC2.png")


e = np.loadtxt("t2500fC1.txt")
fig5 = plt.figure(dpi= 1000)
ax = fig5.gca(projection="3d")
X, Y = np.meshgrid(x,y)
e1 = ax.plot_surface(X,Y,e, cmap=cm.plasma)
cb = fig5.colorbar(e1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion fija, t = 2500")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t2500fC1.png")


f = np.loadtxt("t2500fC2.txt")
fig6 = plt.figure(dpi= 1000)
ax = fig6.gca(projection="3d")
X, Y = np.meshgrid(x,y)
f1 = ax.plot_surface(X,Y,f, cmap=cm.plasma)
cb = fig6.colorbar(f1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion fija, t = 2500")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t2500fC2.png")


g = np.loadtxt("t0pC1.txt")
fig7 = plt.figure(dpi= 1000)
ax = fig7.gca(projection="3d")
X, Y = np.meshgrid(x,y)
g1 = ax.plot_surface(X,Y,g, cmap=cm.plasma)
cb = fig7.colorbar(g1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion periodica, t = 0")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t0pC1.png")

h = np.loadtxt("t0pC2.txt")
fig8 = plt.figure(dpi= 1000)
ax = fig8.gca(projection="3d")
X, Y = np.meshgrid(x,y)
h1 = ax.plot_surface(X,Y,h, cmap=cm.plasma)
cb = fig8.colorbar(h1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion periodica, t = 0")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])

plt.savefig("t0pC2.png")

k = np.loadtxt("t100pC1.txt")
fig9 = plt.figure(dpi= 1000)
ax = fig9.gca(projection="3d")
X, Y = np.meshgrid(x,y)
k1 = ax.plot_surface(X,Y,k, cmap=cm.plasma)
cb = fig9.colorbar(k1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion periodica, t = 100")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t100pC1.png")

i = np.loadtxt("t100pC2.txt")
fig10 = plt.figure(dpi= 1000)
ax = fig10.gca(projection="3d")
X, Y = np.meshgrid(x,y)
i1 = ax.plot_surface(X,Y,i, cmap=cm.plasma)
cb = fig10.colorbar(i1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion periodica, t = 100")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t100pC2.png")

j = np.loadtxt("t2500pC1.txt")
fig11 = plt.figure(dpi= 1000)
ax = fig11.gca(projection="3d")
X, Y = np.meshgrid(x,y)
j1 = ax.plot_surface(X,Y,j, cmap=cm.plasma)
cb = fig11.colorbar(j1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 1, condicion periodica, t = 2500")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t2500pC1.png")

l = np.loadtxt("t2500pC2.txt")
fig12 = plt.figure(dpi= 1000)
ax = fig12.gca(projection="3d")
X, Y = np.meshgrid(x,y)
l1 = ax.plot_surface(X,Y,l, cmap=cm.plasma)
cb = fig12.colorbar(l1, pad =0.1 , shrink = 0.8)
ax.set_title("Caso 2, condicion periodica, t = 2500")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Temperatura [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
plt.savefig("t2500pC2.png")



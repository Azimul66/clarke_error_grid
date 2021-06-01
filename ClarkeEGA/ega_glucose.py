import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text
from matplotlib.patches import Circle, Wedge, Polygon, Path
from matplotlib.collections import PatchCollection

def ega_glucose(ref,est):
    fig, ax = plt.subplots()

    polygons = []

    A = [[0,0],[70,0],[70,56],[400,320],[400,400],[400/1.2,400],[175/3,70],[0,70]]
    Bl = [[70,84],[70,180],[290,400],[400/1.2,400]]
    Br = [[70,0],[70,56],[400,320],[400,180],[240,180],[240,70],[180,70],[130,0]]
    Cl =[[70,180],[290,400],[70,400]]
    Cr = [[130,0],[180,0],[180,70]]
    Dl=[[0,70],[175/3,70],[70,84],[70,180],[0,180]]
    Dr=[[240,180],[400,180],[400,70],[240,70]]
    El=[[0,180],[70,180],[70,400],[0,400]]
    Er=[[180,70],[400,70],[400,0],[180,0]]
    

    pA = Polygon(np.asarray(A),True)
    pBl = Polygon(np.asarray(Bl),True)
    pBr = Polygon(np.asarray(Br),True)
    pCl = Polygon(np.asarray(Cl),True)
    pCr = Polygon(np.asarray(Cr),True)
    pDl = Polygon(np.asarray(Dl),True)
    pDr = Polygon(np.asarray(Dr),True)
    pEl = Polygon(np.asarray(El),True)
    pEr = Polygon(np.asarray(Er),True)
    polygons.append(pA)
    polygons.append(pBl)
    polygons.append(pBr)
    polygons.append(pCl)
    polygons.append(pCr)
    polygons.append(pDl)
    polygons.append(pDr)
    polygons.append(pEl)
    polygons.append(pEr)


    p = PatchCollection(polygons)
    p.set_color(['#0BCA6A','#0AF675','#0AF675','#FEF584','#FEF584','#FFDFC5','#FFDFC5','#FFADAD','#FFADAD'])
    ax.add_collection(p)



    plt.plot([0,400],[0,400], '--', c='#06720D')


    x = ref
    y = est

    sA = []
    sB = []
    sC = []
    sD = []
    sE = []
    for i in range(len(y)):
        sA.append(int(pA.contains_point([x[i],y[i]]))*30)
        sB.append(int(pBr.contains_point([x[i],y[i]]) or pBl.contains_point([x[i],y[i]]))*30)
        sC.append(int(pCr.contains_point([x[i],y[i]]) or pCl.contains_point([x[i],y[i]]))*30)
        sD.append(int(pDr.contains_point([x[i],y[i]]) or pDl.contains_point([x[i],y[i]]))*30)
        sE.append(int(pEr.contains_point([x[i],y[i]]) or pEl.contains_point([x[i],y[i]]))*30)

    plt.scatter(x,y,s=sA,color='#077739')
    plt.scatter(x,y,s=sB,color='#EDAA0E')
    plt.scatter(x,y,s=sC,color=[0.886, 0.654, 0.133,1])
    plt.scatter(x,y,s=sD,color=[0.854,0.213,0.068,1])
    plt.scatter(x,y,s=sE,color=[0.854,0.213,0.068,1])
    

    lx = np.linspace(min(x), max(x), 100)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(lx,p(lx), c='#06720D')


    plt.text(350, 320, "A", fontsize=15)
    plt.text(320, 350, "A", fontsize=15)
    plt.text(370, 260, "B", fontsize=15)
    plt.text(280, 370, "B", fontsize=15)
    plt.text(160, 370, "C", fontsize=15)
    plt.text(160, 15, "C", fontsize=15)
    plt.text(30, 140, "D", fontsize=15)
    plt.text(370, 120, "D", fontsize=15)
    plt.text(30, 370, "E", fontsize=15)
    plt.text(370, 15, "E", fontsize=15)
    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400])
    plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400])
    plt.xlabel('Reference Concentration of Glucose (mg/dL)',fontsize=15)
    plt.ylabel('Estimated Concentration of Glucose (mg/dL)',fontsize=15)
    plt.show()
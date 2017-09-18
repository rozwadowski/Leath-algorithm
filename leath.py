#!/usr/bin/env python
# -*- coding: utf-8 -*-
# P. Rozwadowski
import math
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import scipy as scipy
from scipy import ndimage
import pylab
L = 500
p = 0.6

tab = np.ones((L,L), dtype=np.int8)*(-1)
tabtmp = np.ones((L,L), dtype=np.int8)

for i in range(L):
	tab[i][0] = -2
	tab[i][L-1] = -2
	tab[0][i] = -2
	tab[L-1][i] = -2
tab_rand = np.random.random( (L,L) )


i = (L/2,L/2)

stack = []
tab[i]= 1

#EN = 1



def rysuj():
	for i in range(L):
		for j in range(L):
			if tab[i][j]<=0:
				tabtmp[i][j]=0
			else:
				tabtmp[i][j]=1
	'''pylab.figure()
	pylab.pcolor(tabtmp)
	nStr=str(np.sum(tab == 1)-1)
	nStr=nStr.rjust(5,'0')
	pylab.savefig(nStr)
	'''
	fig=plt.figure()
	ax=fig.add_subplot(111)
	cax = ax.imshow(tabtmp, interpolation='nearest')
	cax.set_clim(vmin=0, vmax=1)
	nStr=str(np.sum(tab == 1)-1)
	nStr=nStr.rjust(6,'0')
	fig.savefig(nStr)
	plt.clf() 

rysuj()

while True:
	if i[0]>0: #gora
		if tab[i[0]-1][i[1]] <= -1:
			if (tab_rand[i[0]-1][i[1]]<p):
				tab[i[0]-1][i[1]] = 1
				stack.append((i[0]-1,i[1]))
				if np.sum(tab == 1)%500-1==0:
					rysuj()
					print np.sum(tab == 1)-1
			else:
				tab[i[0]-1][i[1]] = 0
	if i[1]>0:	#lewo
		if tab[i[0]][i[1]-1] <= -1:
			if (tab_rand[i[0]][i[1]-1]<p):
				tab[i[0]][i[1]-1] = 1
				stack.append((i[0],i[1]-1))
				if np.sum(tab == 1)%500-1==0:
					rysuj()
					print np.sum(tab == 1)-1
			else:
				tab[i[0]][i[1]-1] = 0
	if i[1]<L-1:	#prawo
		if tab[i[0]][i[1]+1] <= -1:
			if (tab_rand[i[0]][i[1]+1]<p):
				tab[i[0]][i[1]+1] = 1
				stack.append((i[0],i[1]+1))
				if np.sum(tab == 1)%500-1==0:
					rysuj()
					print np.sum(tab == 1)-1
			else:
				tab[i[0]][i[1]+1] = 0
	if i[0]<L-1:	#dol
		if tab[i[0]+1][i[1]] <= -1:
			if (tab_rand[i[0]+1][i[1]]<p):
				tab[i[0]+1][i[1]] = 1
				stack.append((i[0]+1,i[1]))
				if np.sum(tab == 1)%500-1==0:
					rysuj()
					print np.sum(tab == 1)-1
			else:
				tab[i[0]+1][i[1]] = 0
	#rysuj()
	#EN = EN + 1
	if len(stack)==0:
		break
	else:
		#if np.sum(tab == 1)%1000-1==0:
		#	rysuj()
		#	print np.sum(tab == 1)%1000-1
		i=stack.pop()

rysuj()
#print tab
print np.sum(tab == 1)


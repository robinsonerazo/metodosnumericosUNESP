#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Resolucao da questao 3 da prova 3 de 2014 do JBA
#  
#  Copyright 2014 Róbinson Erazo <robinson@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
 
#Importacao das bibliotecas cientificas 
#import pylab
import scipy as sp
import scipy.optimize as opt
#import matplotlib.pyplot as plt
#import mpl_toolkits.mplot3d.axes3d as p3d
#from matplotlib import cm

#FUNÇÕES
def F(x):
        n = 517
        
        som1 = 0.
        for i in sp.arange(n):
                j = i + 1
                som1 += (sp.floor( (x[i] - j) ))**2
        
        som2 = sum(x[:])**2
        
        
        return sp.absolute(som1 - som2)

def main():
        return 0


#PRINCIPAL

if __name__ == '__main__':
        main()

        n = 517
        x0 = 5 * sp.ones(n)

        #x_min = opt.fmin_powell(F, x0) # Fmin = 7.4e-08
        
        #x_min = opt.fmin_bfgs(F, x0) # Fmin = 23081242.36
        
        #x_min = opt.fmin(F, x0) # Fmin = 38070712.
        
        lim_inf = -300*sp.ones(n) 
        lim_sup = 300 * sp.ones(n) 
        
        ranges = zip(lim_inf,lim_sup)  
        
        #x_min = opt.brute(F, ranges , Ns = 20)
        
        #x_min = opt.anneal(F, x0) #Fmin = zilhoes
        
        #x_min = opt.leastsq(F, x0)

        
        
        print(x_min, F(x_min))
        
        #Código para escrever arquivo de saída
        file = open("robinson_P2_Q3.txt", "w")
        for i in range(1, n+1):
                j=i-1
                file.write(str(x_min[j]))
                file.write("\n")
        file.write("\n")
        file.write(str(F(x_min)))

        file.close()







#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Resolucao da questao 2 da prova 2 de 2014 do JBA
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
        n = 86
        som = 0.
        for i in sp.arange(n):
                j = i + 1
                som += 1 / ( 1 + (sp.cos(j*x[i]))**2 )
        return n - som

def main():
        return 0


#PRINCIPAL

if __name__ == '__main__':
        main()

        n = 86
        x0 = 2*sp.ones(n)

        #x_min = opt.fmin_powell(F, x0) # Fmin = 8.52e-14
        
        x_min = opt.fmin_bfgs(F, x0) # Fmin = 1.19e-11
        
        #x_min = opt.fmin(F, x0) # Fmin = 3.11
        
        #lim_inf = -300*sp.ones(n) 
        #lim_sup = 300*sp.ones(n) 
        #ranges =        
        #for i in ranges:
        #        ranges[i] = (lim_inf[i],lim_sup[i])  
        
        #x_min = opt.brute(F, ranges , Ns = 10)
        
        #x_min = opt.leastsq(F, x0)
        
        print(x_min, F(x_min))
        
        #Código para escrever arquivo de saída
        file = open("robinson_P2_Q2.txt", "w")
        for i in range(1, n+1):
                j=i-1
                file.write(str(x_min[j]))
                file.write("\n")
        file.write("\n")
        file.write(str(F(x_min)))

        file.close()







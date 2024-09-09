#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Resolucao da questao 1 da prova 3 de 2014 do JBA.
#  Assunto Integracao
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
 

# Bibliotecas científicas e para manipulação de arrays
import scipy.integrate as integ
import scipy as sp
import pylab as pl

def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
    main() 
    
    #Adaptive Gauss quadrature using QUADPACK 
    f = lambda x: 1/sp.sqrt(abs(sp.sin(x)))
    # ponto x=sp.pi tem comportamento extremo (tende ao inf) por isso eh eliminado
    # no argumento points.
    integral, abs_error = integ.quad(f, a = 0.0001, b = 4, epsabs=1.49e-8, epsrel=1.e-18, points=[sp.pi])
    print("Numerical Result =" , integral )
    print("Analytical Result =" , 0)
    print("Absolut Error =" , abs_error)
    
    # Integral de Simpson
    x1 = sp.array([0.0001,1,2,sp.pi-1e-80]) #sao os pontos para interpolar
    x2 = sp.array([sp.pi+1e-80,4])
    integral1 =  integ.simps(f(x1), x1, dx = 1.0)
    integral2 =  integ.simps(f(x2), x2, dx = 1.0)
    print("\n\nNumerical Result =" , integral1+integral2 )
    print("Analytical Result =" , 0 )
    
    #Código para escrever arquivo de saída
    file  = open('robinson_P3_Q1.txt', "w")
    file.write(str(integral))
    file.write("\n")
    file.write(str(abs_error))

    file.close()
        
    #Plotagem
    x = sp.linspace(0.0001, 4.0, num=5000)
    pl.plot(x, f(x))
    pl.xlabel('x')
    pl.ylabel('f(x)')
    pl.grid(True)
    pl.savefig("ode.png")
    pl.show()

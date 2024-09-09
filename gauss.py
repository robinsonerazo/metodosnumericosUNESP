#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gauss.py
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

import numpy as np
from backward_forward import solve_backward 

#FUNÇÕES
def solve_gauss(A,b):
        "Resolve pelo método de Gauss"
        n = len(A) #numero de equacoes no sistema linear
        x = np.zeros(n)  #inicializacao do vetor x =[0,0,0...]

        #Modificacao da matriz A para U
        for k in range(n-1):
                if A[k,k] != 0.0:
                        A[k:n,k] = A[k:n,k]/A[k,k]
                        for i in range(k+1,n):
                                A[i,k:n] = A[i,k:n] - A[i,k]*A[k,k:n]
                                b[i] = b[i] - A[i,k]*b[k]

        #Resolução da Ux = b pelo método backward-substitution
        x = solve_backward(A , b)
        
        return x	
			
def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
        main()
        A = np.array([  [2., 10., 7.],
                        [4., 1.5, 9.],
                        [6., 2., 1.0],
                        ])
				 
        b = np.array([1., 2., 7.])
        x = solve_gauss(A, b)
        print("My code= ",x)
        print("Correto= ",np.linalg.solve(A, b))
        if np.all( np.dot(A,x) == b ):
                print(":) Fechou!")
        else:
                print(":(")



















                
	
	



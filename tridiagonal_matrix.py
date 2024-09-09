#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tridiagonal_matrix.py
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
import scipy.linalg as la
from backward_forward import solve_backward 

#FUNÇÕES
def solve_tridiagonal(A,d):
        "Resolve pelo método de Gauss + backward-substitution"

       #numero de equacoes no sistema linear
        n = len(A) 

        # Extração dos valores das diagonais de [A] para vetores
        a = np.diagonal(A, offset=-1)
        b = np.diagonal(A, offset=0)
        c = np.diagonal(A, offset=1)

        #inicializacao do vetor x =[0,0,0...]
        x = np.zeros(n) 

        #Modificacao da matriz A para U
        for j in range(1,n):
                i = j-1
                b[i+1] = b[i+1]+(-a[i]/b[i])*c[i]
                d[i+1] = d[i+1]+(-a[i]/b[i])*d[i]

        x[n-1] = d[n-1]/b[n-1]
        for j in range(n-1,0,-1):
                i = j-1
                x[i] = (d[i] - c[i] * x[i+1]) / b[i] 
        
        return x	
			
def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
        main()
        A = np.array([  [2., 10., 0., 0.0, 0.],
                        [4., 1.5, 9., 0.0, 0.],
                        [0., 2., 1.0, 5.0, 0.],
                        [0., 0., 2.0, 5.0, 2.],
                        [0., 0., 0.0, 5.0, 2.],
                        ])
				 
        d = np.array([1., 2., 7., 7., 4.])
        x = solve_tridiagonal(A, d)
        print("My code= ",x)
        print("Correto= ",np.linalg.solve(A, d))


















                
	
	



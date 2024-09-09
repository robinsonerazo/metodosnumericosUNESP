#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  backward_forward.py
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


#FUNÇÕES

def solve_backward(A,b):
        "Resolve pelo método backward-substitution"

        n = len(A) #numero de equacoes no sistema linear
        x = np.zeros(n)  #inicializacao do vetor x =[0,0,0...] 
	
	#Primeira solucao
        x[n-1] = b[n-1] / A[n-1][n-1]
	
	#Solucoes seguintes
        for k in range(n-1,0,-1): #k in (n-1,n-2,...,1)
		
                sum_j_to_n = 0.0 # inic. da variavel que guarda o somatorio
                for j in range(k+1,n+1):
                        sum_j_to_n += A[k-1][j-1] * x[j-1]
                        
                x[k-1] = ( b[k-1] - sum_j_to_n ) / A[k-1][k-1]

        return x
	
	
	
def solve_forward(A,b):
        "Resolve pelo método forward-substitution"
        n = len(A) #numero de equacoes no sistema linear
        x = np.zeros(n)  #inicializacao do vetor x =[0,0,0...] 
	
	#Primeira solucao
        x[0] = b[0] / A[0][0]
	
	#Solucoes seguintes
        for k in range(2,n): #k in (2,3,...,n)
                x[k] = ( b[k] - sum(A[k][:]*x[:]) ) / A[k][k]

        return x

def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
        main()
        A = np.array([  [2., 0., 0., 0.],
                        [4., 1.5, 0., 0.],
                        [6., 2., 2., 0.],
                        [5.45, 4., 9.2, 10.]
                        ])
				 
        b = np.array([1., 2., 7., 10.])
        x = solve_forward(A, b)
        print("Numero de Condicionamento de A =", np.linalg.cond(A)) 
        print("My code= ",x )
        print("Correto= ",np.linalg.solve(A, b))
        if all( np.dot(A,x) == b ):
                print(":) Fechou!")
        else:
                print(":(")

        #Matriz de Hilbert Hn (mal condicionadas)
        #Qto mais alto o Nro de Cond, pior o condicionamento
        Hn = np.eye(4)
        bn = np.zeros(4) #Vetor de Hilbert que produz solucao exata 1`s

        for i in range( 1,len(Hn)+1 ):
                for j in range( 1,len(Hn)+1 ):
                        Hn[i-1][j-1] = 1. / (i+j-1)

                bn[i-1] = sum(Hn[i-1][:])
                 

        print("Matriz de Hilbert \n", Hn)
        print("Det(Hn) =", np.linalg.det(Hn))
        print("Numero de Condic. de Hn =", np.linalg.cond(Hn))
        xn = np.linalg.solve(Hn, bn)
        xn_exato = np.dot(bn, np.linalg.inv(Hn))
        print("Solucao exata= \n", xn_exato)
        print("Solucao x= \n", xn)
        if all( np.dot(Hn, xn) == bn ):
                print(":) Fechou!")
        else:
                print(":(")

                
        

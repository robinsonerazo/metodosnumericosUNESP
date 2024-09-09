#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  iteractive_gauss_seidel.py
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

def gauss_seidel(A,b,x,erro_abs):
        "Resolve pelo método iterativo de Gauss Seidel"

        imax = 30000 

        L = la.tril(A)
        U = A - L
        for i in range(imax):
                xk_1 = x
                x = np.dot( la.inv(L) , b - np.dot(U,x) )
                e_abs = np.linalg.norm(x - xk_1)
                norm_residuo = np.linalg.norm( np.dot(A,x) - b )
                print(str(i).zfill(3),x,e_abs,norm_residuo)

                if e_abs <= erro_abs:
                        return x
                elif i == imax:
                        print("Não convergiu com iteracoes =" ,i)
                        



	

def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
        main()
        A = np.array([[4.0, -2.0, 1.0],
                      [1.0, -3.0, 2.0],
                      [-1.0, 2.0, 6.0]])
        b = [1.0, 2.0, 3.0]
        x_0 = [1, 1, 1]
        erro_abs = 1e-5
        
        x = gauss_seidel(A, b, x_0, erro_abs)
        print("Numero de Condicionamento de A =", np.linalg.cond(A))
        print("Norma do residuo =", la.norm( np.dot(A,x) - b) )
        print("\nMy code= ",x )
        print("Correto= ",np.linalg.solve(A, b))
        

        #Matriz de Hilbert Hn (mal condicionadas)
        #Qto mais alto o Nro de Cond, pior o condicionamento
        n = 5
        Hn = la.hilbert(n) #Matriz de Hilbert
        bn = np.zeros(n) #Vetor de Hilbert que produz solucao exata 1`s
        x_0 = np.zeros(n) #Chute!
        for i in range( 1,len(Hn)+1 ):
                bn[i-1] = sum(Hn[i-1][:])
                 

        print("\n\n\nMatriz de Hilbert \n", Hn)
        print("Det(Hn) =", la.det(Hn))
        print("Numero de Condic. de Hn =", np.linalg.cond(Hn))
        erro_abs = 1e-3
        xn = gauss_seidel(Hn, bn, x_0, erro_abs)
        xn_exato = np.dot(bn, np.linalg.inv(Hn))
        print("Solucao exata= \n", xn_exato)
        print("Solucao x= \n", xn)


        #Código para escrever arquivo de saída
        n = 20000
        Hn = la.hilbert(n)
        file  = open('huge.csv', "w")
        for i in range(n):
                file.write("\n")
                for j in range(n):
                        file.write(str(Hn[i][j]))
                        file.write(",")
        file.close()

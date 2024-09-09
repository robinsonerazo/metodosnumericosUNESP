#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  code_Q1.py
#  
#  Copyright 2014 Róbinson Erazo <robinson.gtpe@gmail.com>
#  
#  Resolução da Questão 1.
#  
#  

# Bibliotecas científicas e para manipulação de arrays
import numpy as np
import scipy as sp
import scipy.linalg as la
from scipy.sparse.linalg.dsolve import spsolve
from scipy.sparse import csr_matrix
import csv

#FUNÇÕES

def gerar_matriz(n):
        "Gera a matriz A"

        A = np.zeros((n,n),float)  #inicializacao da matriz A =[0] 

	
        for i in range(1,n+1):
                for j in range(1,n+1):
                        if i==j:
                                A[i-1][j-1] = 10./(i*j)
                        elif i != j:
                                A[i-1][j-1] = 1./((i*i) + (2*j*j))
                
        return A


def gerar_vetor(n):
        "Gera a vetor b"

        b = np.zeros(n,float)  #inicializacao da matriz A =[0] 

	
        for i in range(1,n+1):
                b[i-1] = n/(i*(i+8))
                

        return b

	
	
	


def main():
	
	return 0

#PRINCIPAL

if __name__ == '__main__':
    main()
    n = 4007
    A = gerar_matriz(n)
    b = gerar_vetor(n)
    A_= np.dot(A,A.T)
    b_= np.dot(A.T,b)

    x = la.solve(A_,b_) #norm_residuo =  x
    #x = spsolve(csr_matrix(A),b)   #norm_residuo x c/ sp.sparse 
    v_residuo = np.dot(A_,x) - b_
    norm_residuo = la.norm(v_residuo, ord = 8)
    print('Vetor solucao = \n',x)
    print('\n\nDeterminante = \n',la.det(A_))
    print('\n\nNorma do residuo = \n',norm_residuo)
    print('\n\nNro de Condicionamento = \n',np.linalg.cond(A_))
    

    #Código para escrever arquivo de saída
    file  = open('robinson_P1_Q1.txt', "w")
    file.write(str(n))
    for i in range(1, n+1):
        j=i-1
        file.write("\n")
        file.write(str(i))
        file.write(" ")
        file.write(str(x[j]))
    file.write("\n")
    file.write(str(norm_residuo))

    file.close()

    
        

        

    



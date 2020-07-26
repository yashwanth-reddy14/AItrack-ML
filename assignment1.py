# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:52:02 2020

@author: aleti
"""


from scipy.optimize import linprog
objec=[-50,-120]
lhs_ceq = [[7000,2000],[10,30],[1,1]]
rhs_ceq = [700000,1200,110]
bounder=[(0,float('inf')),(0,float('inf'))]
optimize = linprog(c=objec,A_ub=lhs_ceq,b_ub=rhs_ceq,bounds=bounder,method="simplex")
optimize
# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from IPython.core.display import HTML
from IPython.display import Image
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# # *Circuitos Elétricos I - Semana 6*

# ### Problema 1
#   
# Para o circuito abaixo, tem-se que $v(t)=-1800te^{-20t}$ para $t\geq0$ e $i_1(0)=4\;A$ e $i_2(0)=-16\;A$
#
# a) Determine $i_1(t)$ e $i_2(t)$ para $t\geq0$.\
# b) Determine a energia fornecida à fonte de tensão no intervalo $0\leq t \leq\infty$.\
# c) Determine a energia inicial armazenada nos indutores.\
# d) Determine a energia final armazenada nos indutores.

Image("./figures/J8C1.png", width=500)

# +
import matplotlib.pyplot as plt
import numpy as np

tmax = 1
t = np.linspace(0, tmax, num = 1000)
v = 1800*t*np.exp(-20*t)

plt.plot(t, v)
plt.xlim(0, tmax)
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('v(t) [V]')
plt.show()

# +
# valores das indutâncias
L1 = 10
L2 = 30

# valores iniciais das correntes
i1_0 = 4
i2_0 = -16

# +
from sympy import *

# define as variáveis 
t, τ = symbols('t, τ')

# define v(τ)
v = -1800*τ*exp(-20*τ)

# correntes nos indutores em função da tensão aplicada aos terminais
i1 = -(1/L1)*integrate(v, (τ, 0, t)) + i1_0
i2 = -(1/L2)*integrate(v, (τ, 0, t)) + i2_0

print('Correntes nos indutores:')
print('i1(t) = ', i1 , ' A')
print('i2(t) = ', i2 , ' A')

# +
# LKC
i = i1 + i2

# define v(t)
v = -1800*t*exp(-20*t) 

# potência fornecida à fonte
p = v*i

# energia entrege à fonte
E = integrate(p, (t, 0, oo))
print('Energia entrege à fonte:')
print('E = %.2f J' %E)

# +
# calculando os valores de energia em t=0

E1_0 = (1/2)*L1*(i1.evalf(subs={t:0}))**2
E2_0 = (1/2)*L2*(i2.evalf(subs={t:0}))**2

print('Energia inicial armazenada nos indutores:')
print('E1(0) = %.2f J' %E1_0)
print('E2(0) = %.2f J' %E2_0)

# +
# calculando os valores de energia em t =oo

E1_inf = (1/2)*L1*(i1.evalf(subs={t:100}))**2
E2_inf = (1/2)*L2*(i2.evalf(subs={t:100}))**2

print('Energia final armazenada nos indutores:')
print('E1(oo) = %.2f J' %E1_inf)
print('E2(oo) = %.2f J' %E2_inf)

# +
# calculando a variação de energia nos indutores

ΔE = (E1_inf-E1_0) + (E2_inf-E2_0)

print('Variação da energia armazenada nos indutores:')
print('ΔE = %.2f J' %ΔE)
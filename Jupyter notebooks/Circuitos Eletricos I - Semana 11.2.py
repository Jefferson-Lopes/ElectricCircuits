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
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# # *Circuitos Elétricos I - Semana 11*

# ### A integral de Laplace
#
# Seja $f(t)$ uma função definida no intervalo $0\leq t \leq \infty$, com $t$ e $f(t)$ reais, então a função $F(s)$, definida pela integral de Laplace
#
# $$\large
# \begin{equation}
# F(s)=\mathcal{L}\{f(t)\}=\int_{0}^{\infty} f(t) e^{-s t} dt,\;\; s \in \mathbb{C},
# \end{equation}
# $$
#
# é conhecida como a transformada de Laplace de $f(t)$.
#
# Para informações sobre como utilizar o Sympy para o cálculo da transformada de Laplace:
#
# https://dynamics-and-control.readthedocs.io/en/latest/1_Dynamics/3_Linear_systems/Laplace%20transforms.html

# +
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy.polys.partfrac import apart


plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False

# Função para plot de funções do sympy
def symplot(F, intervalo, funLabel):
     
    if type(F) == list:
        indLabel = 0
        for f in F:
            f_num = np.zeros(intervalo.shape)
 
            for indT in range(0,intervalo.size):
                f_num[indT] = f.evalf(subs={t:intervalo[indT]})
            
            plt.plot(intervalo, f_num, label=funLabel[indLabel])
            plt.legend();
            plt.xlim([min(intervalo), max(intervalo)]);
            plt.xlabel('tempo [s]');
            indLabel += 1
    else:
        f_num = np.zeros(intervalo.shape)
 
        for indT in range(0,intervalo.size):
            f_num[indT] = F.evalf(subs={t:intervalo[indT]})
            
        plt.plot(intervalo, f_num, label=funLabel)
        plt.legend();
        plt.xlim([min(intervalo), max(intervalo)]);
        plt.xlabel('tempo [s]');            
    
    plt.grid();
    
# função para arredondamento de floats em expressões simbólicas
def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(sp.Number)})

# transformada de Laplace
def L(f,t,s):
    return sp.laplace_transform(f, t, s, noconds=True)

# transformada inversa de Laplace
def invL(F,s,t):
    return sp.re(sp.inverse_laplace_transform(F, s, t, noconds=True))

# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    coeff = expr.as_numer_denom()
    c0 = sp.poly(coeff[1].cancel()).coeffs()[0]
    
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def partFrac(expr, Ndigits):
    expr = expr.cancel()
    expr = apart(adjustCoeff(expr), s, full=True).doit()
    
    return sp.N(expr, Ndigits)

sp.init_printing()
# -

# #### Definindo algumas variáveis simbólicas de interesse

t, s  = sp.symbols('t, s')
a     = sp.symbols('a', real=True, positive=True)
omega = sp.symbols('omega', real=True)

# ## Gere sua tabela de transformadas

func = [1,
         t,
         sp.exp(-a*t),
         t*sp.exp(-a*t),
         t**2*sp.exp(-a*t),
         sp.sin(omega*t),
         sp.cos(omega*t),
         1 - sp.exp(-a*t),
         sp.exp(-a*t)*sp.sin(omega*t),
         sp.exp(-a*t)*sp.cos(omega*t),
         ]
func

Fs = [L(f,t,s) for f in func]
Fs

# ### Problema 1
#
# Não existe nenhuma energia armazenada no circuito da figura a seguir no momento em que a fonte de corrente é ligada.
#
# <img src="./figures/J14C1.png" width="500">
#
# a. Determine $I_a(s)$ e $I_b(s)$.\
# b. Determine $i_a(t)$ e $i_b(t)$.\
# c. Determine $V_a(s)$, $V_b(s)$ e $V_c(s)$.\
# d. Determine $v_a(t)$, $v_b(t)$ e $v_c(t)$.

# <img src="./figures/J14C2.png" width="500">

# a. Determinando $I_a(s)$ e $I_b(s)$:

# +
I2, I3, s = sp.symbols('I2, I3, s')

# define os sistema de equações
eq1 = sp.Eq((4 + s)*I2 - 2*I3, 4)             
eq2 = sp.Eq(-2*s*I2 + s*(4 + s)*I3, 8)  

# resolve o sistema
soluc = sp.solve([eq1, eq2],[I2, I3], dict=True)
soluc

I2 = [sol[I2] for sol in soluc]
I3 = [sol[I3] for sol in soluc]

I1 = 4/s
I2 = I2[0]
I3 = I3[0]

print('Correntes de malha no domínio de Laplace: \n')
print('I1 =',I1)
print('I2 =',I2)
print('I3 =',I3)
# -

# Calculando Ia
Ia = I1-I2
Ia = Ia.simplify()
Ia

# Calculando Ib
Ib = I2
Ib

# b. Determinando $i_a(t)$ e $i_b(t)$

Ia.apart()

# +
t = sp.symbols('t',real=True)

ia = invL(Ia,s,t)
ia
# -

Ib.apart()

ib = invL(Ib,s,t)
ib

# c. Determinando $V_a(s)$, $V_b(s)$ e $V_c(s)$.

# +
Va = (100/s)*I2
Vb = (100/s)*(I3-I2)
Vc = (100/s)*(I1-I3)

print('Va =',Va.cancel().simplify())
print('Vb =',Vb.cancel().simplify())
print('Vc =',Vc.cancel().simplify())
# -

Va.apart()

Vb.apart()

Vc.apart()

# d. Determinando $v_a(t)$, $v_b(t)$ e $v_c(t)$.

# +
va = ((-400/9)*sp.exp(-6*t) + (400/9) + (400/3)*t)*sp.Heaviside(t)

round_expr(va,2)

# +
vb = ((800/9)*sp.exp(-6*t) - (800/9) + (400/3)*t)*sp.Heaviside(t)

round_expr(vb,2)

# +
vc = va

round_expr(vc,2)
# -

# plota funções no domínio do tempo
intervalo = np.arange(-4, 10, 0.01)
symplot([va, vb, vc], intervalo, ['va(t)','vb(t)','vc(t)'])

# ### Problema 2
#
# Não existe nenhuma energia armazenada no circuito da figura a seguir no momento em que a fonte de tensão é conectada.
#
# <img src="./figures/J14C3.png" width="600">
#
# a. Determine $V_0(s)$.\
# b. Determine $v_0(t)$.

# <img src="./figures/J14C4.png" width="600">

# +
Ia, Ib, s = sp.symbols('Ia, Ib, s')

# define o sistema de equações
eq1 = sp.Eq(10*Ia + (s + 250/s)*Ib, 35/s)             
eq2 = sp.Eq(Ia - (1 + 0.4*s)*Ib, 0)

# resolve o sistema
soluc = sp.solve([eq1, eq2],[Ia, Ib], dict=True)
soluc

Ia = [sol[Ia] for sol in soluc]
Ib = [sol[Ib] for sol in soluc]

Ia = Ia[0]
Ib = Ib[0]
# -

print('Ia =')
Ia

print('Ib =')
Ib.simplify()

V0 = 35/s - 2*Ia
V0.simplify()

partFrac(V0, 2)

np.roots([1, 2, 50, 0])

# +
K    = sp.symbols('K')
σ, ω = sp.symbols('σ, ω', real=True)

j = sp.I

F = K/(s + σ + j*ω) + sp.conjugate(K)/(s + σ - j*ω)
F
# -

invL(F,s,t)

v0 = (35 + sp.exp(-t)*(-5.6*sp.cos(7*t)-1.2*sp.sin(7*t)))*sp.Heaviside(t)
v0

# plota funções no domínio do tempo
intervalo = np.arange(-4, 10, 0.01)
symplot(v0, intervalo, 'v0(t)')
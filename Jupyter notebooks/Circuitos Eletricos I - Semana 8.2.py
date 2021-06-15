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

# # *Circuitos Elétricos I - Semana 8*
#
# # Circuitos de segunda ordem

# ## Circuito RLC em paralelo
#
# <img src="./figures/J12C2.png" width="800">
#
# ### Aplicação das Leis de Kirchhoff 
#
# $$\begin{align}
#    i_R + i_L + i_C &= i_s\\
#    \frac{v}{R} + i_L + C\frac{d v}{d t} &= i_s\nonumber\\
#     \frac{1}{R}\left[L\frac{d i_L}{d t}\right] + i_L + C \frac{d}{d t}\left[L\frac{d i_L}{d t}\right]  &= i_s\nonumber\\
#     \frac{d^{2} i_L}{d t^{2}}+\frac{1}{RC} \frac{d i_L}{d t}+\frac{1}{L C} i_L &=\frac{i_s}{LC}
#    \end{align}
# $$
#
# com $\alpha = \frac{1}{2RC}$ e $\omega_0 = \frac{1}{\sqrt{LC}}$, temos
#
# $$ 
# \begin{equation}\label{EDO1} 
# \frac{d^{2} i_L}{d t^{2}}+2\alpha \frac{d i_L}{d t}+\omega_0^2 i_L=i_{\mathrm{s}}\omega_0^2 
# \end{equation} 
# $$
#
# A equação \ref{EDO1} é uma EDO de segunda ordem, linear e de coeficientes constantes.
#
# Equação característica:
#
# $$\begin{equation} s^2+2\alpha s + \omega_0^2=0 \end{equation} $$
#
# Raízes da equação característica:
#
# $$
# \begin{align}
# s_1 &=-\alpha +\sqrt{\alpha^2-\omega_0^2}\\
# s_2 &=-\alpha -\sqrt{\alpha^2-\omega_0^2}
# \end{align}
# $$

# ### Resposta total 
#
# A resposta transiente de circuitos RLC em paralelo, seja ela natural ($i_L(\infty)=0$) ou ao degrau ($i_L(\infty)=i_s$), pode ser classificada nas três casos seguintes. Em todos os casos, assume-se que o transiente teve início no instante $t_0$ (instante do chaveamento).
#
# #### Caso superamortecido ($\alpha>\omega_0\Rightarrow \text{raízes reais e distintas}$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} i_L(t) =A_{1} e^{s_{1} (t-t_0)}+A_{2} e^{s_{2} (t-t_0)}+i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=A_1 + A_2 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &=s_1A_1 + s_2A_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $A_1$ e $A_2$:
#
# $$
# \begin{align}
# A_{1} &=\frac{\frac{1}{L} v_C(t_0^+)-s_{2}\left[i_L(t_0^+)-i_L(\infty)\right]}{s_{1}-s_{2}} \\
# A_{2} &=\frac{-\frac{1}{L} v_C(t_0^+)+s_{1}\left[i_L(t_0^+)-i_L(\infty)\right]}{s_{1}-s_{2}}
# \end{align}
# $$

# #### Caso subamortecido ($ \alpha<\omega_0\Rightarrow\text{raízes complexas e conjugadas} $):
#
# Fazendo $\omega_d = \sqrt{\omega_0^2-\alpha^2}$ temos $s_1 = -\alpha +j\omega_d$ e $s_2 = -\alpha -j\omega_d$.
#
# Solução geral da EDO:
#
# $$\begin{equation} i_L(t) = e^{-\alpha(t-t_0)}\left\lbrace B_{1}\cos[\omega_d (t-t_0)] + B_{2}\sin[\omega_d (t-t_0)]  \right\rbrace + i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=B_1 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &= -\alpha B_1 +\omega_d B_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $B_1$ e $B_2$:
#
# $$
# \begin{align}
# B_{1} &=i_L(t_0^+)-i_L(\infty) \\
# B_{2} &=\frac{\frac{1}{L} v_C(t_0^+)+\alpha\left[i_L(t_0^+)-i_L(\infty)\right]}{\omega_d}
# \end{align}
# $$

# #### Caso criticamente amortecido ($\alpha=\omega_0\Rightarrow \text{raízes reais e idênticas } s_1=s_2=-\alpha$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} i_L(t) =D_{1} e^{-\alpha(t-t_0)}+D_{2}(t-t_0) e^{-\alpha(t-t_0)}+i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=D_1 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &=-\alpha D_1 + D_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $D_1$ e $D_2$:
#
# $$
# \begin{align}
# D_{1} &=i_L(t_0^+)-i_L(\infty) \\
# D_{2} &= \frac{1}{L} v_C(t_0^+)+\alpha\left[i_L(t_0^+)-i_L(\infty)\right]
# \end{align}
# $$

# ### Problema 1
#
# Para o circuito a seguir, as chaves $ch1$ e $ch2$ estiveram abertas por um longo intervalo de tempo. 
#
# <img src="./figures/J12C3.png" width="700">
#
#
# a. Considerando que apenas $ch1$ fecha em $t_0=0$s, determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.\
# b. Qual o máximo valor (absoluto) atingido pela tensão aplicada aos terminais do capacitor para $t\geq 0^+$? Em que instante ele ocorre?\
# c. Considerando que apenas $ch2$ fecha em $t_0=0$s, determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.
#
# Link para a simulação do circuito: https://tinyurl.com/yf8pj57t

# +
import numpy as np
import sympy as sp
from matplotlib import style

# função para arredondamento de floats em expressões simbólicas
def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(sp.Number)})


# -

# Resolução item (a):

# +
# Parâmetros do circuito:
R = 1.64
L = 6e-3
C = 0.5e-3

# calculando α e ω0
α  = 1/(2*R*C)
ω0 = 1/np.sqrt(L*C)

print('α = %.2f rad/s'%α)
print('ω0 = %.2f rad/s'%ω0)

# +
# informações obtidas pela análise do circuito
iL_inf = -4 # valor final da corrente no indutor
iL_t0 = 2   # valor inicial da corrente no indutor
vc_t0 = 0   # valor inicial da tensão no capcitor

t0 = 0 # instante do chaveamento

# +
# raízes da equação característica
s1 = -α + np.sqrt(α**2-ω0**2)
s2 = -α - np.sqrt(α**2-ω0**2)

# define variáveis da solução geral
t, A1, A2 = sp.symbols('t,A1,A2')

# expressão geral da resposta superamortecida
iL = A1*sp.exp(s1*(t-t0)) + A2*sp.exp(s2*(t-t0)) + iL_inf

print('iL(t) = ', round_expr(iL,2), ' A')

# +
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq(   A1 +    A2 + iL_inf, iL_t0)             
eq2 = sp.Eq(s1*A1 + s2*A2,        vc_t0/L)  

# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
A1 = np.array([sol[A1] for sol in soluc])
A2 = np.array([sol[A2] for sol in soluc])

A1 = A1[0]
A2 = A2[0]

print('Solução do sistema:\n\n A1 = %.2f A,\n A2 = %.2f A' %(round(A1,2), round(A2,2)))

# +
# expressão geral da resposta subamortecida
iL = A1*sp.exp(s1*(t-t0)) + A2*sp.exp(s2*(t-t0)) + iL_inf

print('iL(t) = ', round_expr(iL,2), ' A')

# +
# tensão aplicada sobre o capacitor (= tensão sobre o indutor)
vC = L*sp.diff(iL, t)

print('vC(t) = ', round_expr(vC, 2), ' V')
# -

# Resolução item (b):

style.use('seaborn-darkgrid')
p = sp.plot(iL, vC, (t,0,0.025), ylim = (-8,4), show=False, legend=True)
p[0].line_color = 'red'
p[1].line_color = 'blue'
p[0].label = 'iL(t)'
p[1].label = 'vC(t)'
p.show()

# +
# define a equação dvC/dt = 0
eq1 = sp.Eq(sp.diff(vC, t),0)   

# resolve a equação em t
ts = sp.solveset(eq1, t).args[0]

# calcula o valor de vC(t) para t = ts
vC_ts = vC.evalf(subs={t:ts})

print('ts = %.2e s'%ts)
print('vC(ts) = %.2f V'%vC_ts)
# -

# Resolução item (c):

# +
# Parâmetros do circuito:
R = 6
L = 6e-3
C = 0.5e-3

# calculando α e ω0
α  = 1/(2*R*C)
ω0 = 1/np.sqrt(L*C)

print('α = %.2f rad/s'%α)
print('ω0 = %.2f rad/s'%ω0)

# +
# informações obtidas pela análise do circuito
iL_inf = 0  # valor final da corrente no indutor
iL_t0 = 2   # valor inicial da corrente no indutor
vc_t0 = 0   # valor inicial da tensão no capcitor

t0 = 0 # instante do chaveamento

# +
# define a frequência de oscilação amortecida
ωd =np.sqrt(ω0**2-α**2)

# define variáveis da solução geral
t, B1, B2 = sp.symbols('t,B1,B2')

# expressão geral da resposta subamortecida
iL = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0)) + B2*sp.sin(ωd*(t-t0))) + iL_inf

print('iL(t) = ', round_expr(iL,2), ' A')

# +
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq(   B1 + iL_inf, iL_t0)             
eq2 = sp.Eq(-α*B1 + ωd*B2,  vc_t0/L)  

# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
B1 = np.array([sol[B1] for sol in soluc])
B2 = np.array([sol[B2] for sol in soluc])

B1 = B1[0]
B2 = B2[0]

print('Solução do sistema:\n\n B1 = %.2f A,\n B2 = %.2f A' %(round(B1,2), round(B2,2)))

# +
# expressão geral da resposta subamortecida
iL = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0))+B2*sp.sin(ωd*(t-t0))) + iL_inf

print('iL(t) = ', round_expr(iL,2), ' A')

# +
# tensão aplicada sobre o capacitor (= tensão sobre o indutor)
vC = L*sp.diff(iL, t)
vC = sp.simplify(vC)

print('vC(t) = ', round_expr(vC, 2), ' V')
# -

#style.use('seaborn-darkgrid')
p = sp.plot(iL, vC, (t,0,0.050), ylim = (-6,4), show=False, legend=True)
p[0].line_color = 'red'
p[1].line_color = 'blue'
p[0].label = 'iL(t)'
p[1].label = 'vC(t)'
p.show()

# ## Circuito RLC em série

# <img src="./figures/J12C1.png" width="800">
#
# ### Aplicação das Leis de Kirchhoff 
#
# $$\begin{align}
#    v_R + v_L + v_C &= v_s\\
#    R i + L\frac{d i}{dt}+v_C &= v_s\nonumber\\
#    R\left[C\frac{dv_C}{dt}\right] + L\frac{d}{dt}\left[C\frac{dv_C}{dt} \right] &= v_s\nonumber\\
#     \frac{d^{2} v_{\mathrm{C}}}{d t^{2}}+\frac{R}{L} \frac{d v_{\mathrm{C}}}{d t}+\frac{1}{L C}   v_{\mathrm{C}} &=\frac{v_{\mathrm{s}}}{LC}
#    \end{align} 
# $$
#
# com $ \alpha = \frac{R}{2L}$ e $\omega_0 = \frac{1}{\sqrt{LC}}$, temos
#
# $$ \begin{equation}\label{EDO2} \frac{d^{2} v_{\mathrm{C}}}{d t^{2}}+2\alpha \frac{d v_{\mathrm{C}}}{d t}+\omega_0^2 v_{\mathrm{C}}=v_{\mathrm{s}}\omega_0^2 \end{equation} $$
#
# A equação \ref{EDO2} é uma EDO de segunda ordem, linear e de coeficientes constantes.
#
# Equação característica:
#
# $$\begin{equation} s^2+2\alpha s + \omega_0^2=0 \end{equation}$$
#
# Raízes da equação característica:
#
# $$
# \begin{align}
# s_1 &=-\alpha +\sqrt{\alpha^2-\omega_0^2}\\
# s_2 &=-\alpha -\sqrt{\alpha^2-\omega_0^2}
# \end{align}
# $$

# ### Resposta total 
#
# A resposta transiente de circuitos RLC em série, seja ela natural ($v_C(\infty)=0$) ou ao degrau ($v_C(\infty)=v_s$), pode ser classificada nas três casos seguintes. Em todos os casos, assume-se que o transiente teve início no instante $t_0$ (instante do chaveamento).
#
# #### Caso superamortecido ($\alpha>\omega_0\Rightarrow \text{raízes reais e distintas}$):
#
# Solução geral da EDO:
#
# $$\begin{equation} v_{\mathrm{C}}(t) =A_{1} e^{s_{1} (t-t_0)}+A_{2} e^{s_{2} (t-t_0)}+v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=A_1 + A_2 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &=s_1A_1 + s_2A_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $A_1$ e $A_2$:
#
# $$
# \begin{align}
# A_{1} &=\frac{\frac{1}{C} i_{\mathrm{L}}(t_0^+)-s_{2}\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{s_{1}-s_{2}} \\
# A_{2} &=\frac{-\frac{1}{C} i_{\mathrm{L}}(t_0^+)+s_{1}\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{s_{1}-s_{2}}
# \end{align}
# $$

# #### Caso subamortecido ($\alpha<\omega_0\Rightarrow \text{raízes complexas e conjugadas}$):
#
# Fazendo $\omega_d = \sqrt{\omega_0^2-\alpha^2}$ temos $s_1 = -\alpha +j\omega_d$ e $s_2 = -\alpha -j\omega_d$.
#
# Solução geral da EDO:
#
# $$\begin{equation} v_{\mathrm{C}}(t) = e^{-\alpha(t-t_0)}\left\lbrace B_{1}\cos[\omega_d (t-t_0)] + B_{2}\sin[\omega_d (t-t_0)]  \right\rbrace + v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=B_1 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &= -\alpha B_1 +\omega_d B_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $B_1$ e $B_2$:
#
# $$
# \begin{align}
# B_{1} &=v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty) \\
# B_{2} &=\frac{\frac{1}{C} i_{\mathrm{L}}(t_0^+)+\alpha\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{\omega_d}
# \end{align}
# $$

# #### Caso criticamente amortecido ($\alpha=\omega_0\Rightarrow \text{raízes reais e idênticas } s_1=s_2=-\alpha$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} v_{\mathrm{C}}(t) =D_{1} e^{-\alpha(t-t_0)}+D_{2}(t-t_0) e^{-\alpha(t-t_0)}+v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=D_1 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &=-\alpha D_1 + D_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $D_1$ e $D_2$:
#
# $$
# \begin{align}
# D_{1} &=v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty) \\
# D_{2} &= \frac{1}{C} i_{\mathrm{L}}(t_0^+)+\alpha\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]
# \end{align}
# $$

# ### Problema 2
#
# No circuito da figura a seguir, a chave $ch1$ estive aberta por um longo intervalo de tempo antes de fechar, no instante $t_0=0$s.
#
# <img src="./figures/J12C4.png" width="500">
#
# a. Para qual valor de $R_x$ o circuito exibe uma resposta criticamente amortecida para $t\geq 0^+$?\
# b. Considerando que $R_x$ vale exatamente o valor calculado em (a), determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.\
# c. Considerando que $R_x$ vale um décimo do valor calculado em (a), determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.
#
# Link para a simulação deste circuito: https://tinyurl.com/yjgkkzhu

# Resolução item (a):

# +
# Parâmetros do circuito:
R =
L = 
C = 

# calculando α e ω0
α  = 
ω0 = 1/np.sqrt(L*C)

print('α = %.2f rad/s'%α)
print('ω0 = %.2f rad/s'%ω0)

# +
# informações obtidas pela análise do circuito
vC_inf =   # valor final da tensão sobre o capacitor
iL_t0 =    # valor inicial da corrente no indutor
vC_t0 =    # valor inicial da tensão sobre o capacitor

t0 = 0 # instante do chaveamento

# +
# raízes da equação característica
s1 = -α
s2 = -α

# define variáveis da solução geral
t, D1, D2 = sp.symbols('t, D1, D2')

# expressão geral da resposta 
vC = D1*sp.exp(s1*(t-t0)) + D2*(t-t0)*sp.exp(s2*(t-t0)) + vC_inf

print('vC(t) = ', round_expr(vC,2), ' V')

# +
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq()             
eq2 = sp.Eq()  

# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
D1 = np.array([sol[D1] for sol in soluc])
D2 = np.array([sol[D2] for sol in soluc])

D1 = D1[0]
D2 = D2[0]

print('Solução do sistema:\n\n D1 = %.2f V,\n D2 = %.2f V/s' %(round(A1,2), round(A2,2)))

# +
# expressão geral da resposta 
vC = D1*sp.exp(s1*(t-t0)) + D2*(t-t0)*sp.exp(s2*(t-t0)) + vC_inf

print('vC(t) = ', round_expr(vC,2), ' V')

# +
# corrente passando pelo indutor
iL = C*sp.diff(vC, t)

print('iL(t) = ', round_expr(iL, 2), ' A')
# -

#style.use('seaborn-darkgrid')
p = sp.plot(iL, vC, (t,0,0.050), ylim = (-6,4), show=False, legend=True)
p[0].line_color = 'red'
p[1].line_color = 'blue'
p[0].label = 'iL(t)'
p[1].label = 'vC(t)'
p.show()
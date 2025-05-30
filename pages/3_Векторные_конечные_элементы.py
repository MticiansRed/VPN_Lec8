import streamlit as st
from PIL import Image
 
menu = st.sidebar.radio('***',
    (
    "Функции непрерывного аргумента", 
    "Операторы векторного анализа", 
    "Уравнение Максвелла",
    "Конечно-элементная аппроксимация",  
    "Векторные элементы",        
    )
)
  
if menu == "Функции непрерывного аргумента":
    r"""
##### Функции непрерывного аргумента

**Скалярные функции**

$\varphi(x), \quad x \in \Omega$

$x = (x_1, x_2, x_3)$ - 3D точка 

**Векторные функции**

$\bm u(x), \quad  x \in \Omega$

$\bm u(x) = \{u_1(x), \ u_2(x), \ u_3(x)\}$ - компонентное представление вектора

**Тензорные функции**

$\cdots$

    """    
    
if menu == "Операторы векторного анализа":
    r"""
##### Операторы векторного анализа

Градиент скалярной функции $\varphi(x)$

$\begin{aligned}
\operatorname{grad} \varphi = \left \{
\frac {\partial \varphi} {\partial x_1}, \ \frac {\partial \varphi} {\partial x_2}, \ \frac {\partial \varphi} {\partial x_3} \right \}
\end{aligned}$

Дивергенция векторной функции $\bm u(x) = \{u_1(x), \ u_2(x), \ u_3(x)\}$

$\begin{aligned}
\operatorname{div} \bm u = 
\frac {\partial u_1} {\partial x_1} + \frac {\partial u_2} {\partial x_2} + \frac {\partial u_3} {\partial x_3} 
\end{aligned}$

Ротор векторной функции $\bm u(x) = \{u_1(x), \ u_2(x), \ u_3(x)\}$

$\begin{aligned}
\operatorname{rot} \bm u = \left \{
\frac {\partial u_3} {\partial x_2} - \frac {\partial u_2} {\partial x_3} , \ \frac {\partial u_1} {\partial x_3} - \frac {\partial u_3} {\partial x_1} , \ \frac {\partial u_2} {\partial x_1} - \frac {\partial u_1} {\partial x_2} \right \}
\end{aligned}$

    """

if menu == "Уравнение Максвелла":
    r"""
##### Уравнение Максвелла

**Однородная среда**

$\begin{aligned}
\frac {\partial \bm E} {\partial t} - \operatorname{rot} \bm H = 0 
\end{aligned}$

$\begin{aligned}
\frac {\partial \bm H} {\partial t} + \operatorname{rot} \bm E = 0 
\end{aligned}$

$\bm E$ - электрическое поле

$\bm H$ - магнитное поле

**Уравнение для электрического поля**

$\begin{aligned}
\frac {\partial^2 \bm E} {\partial t^2} - \operatorname{rot} \operatorname{rot} \bm E = 0 
\end{aligned}$

**Координатное представление**

$\cdots$

    """       
    
if menu == "Конечно-элементная аппроксимация":
    r"""
##### Конечно-элементная аппроксимация

**Векторные функции** 

$\bm u(x) = \{u_1(x), \ u_2(x), \ u_3(x)\}$ 

* Конечно-элементная аппроксимация отдельных комонент вектора (скалярных функций)

$\quad~~ \varphi_i(x) \approx u_i(x), \quad i = 1,2,3$

* Специальные конечные элементы

$\quad~$ Выделение нормальных и тангенциальный компонент вектора

    """       
    
    c1,c2 = st.columns([4,2])
    image = Image.open("pages/figs/13.png")
    c1.image(image) 
    
if menu == "Векторные элементы":
    r"""
##### Векторные элементы

**Линейные конечные элементы**

    """    
    
    c1,cc,c2 = st.columns([4,0.5,2])
    c1.write(r"""
    $~$
    
    Нормальные компоненты вектора
    
    (Brezzi–Douglas–Marini)    
    """)
    image = Image.open("pages/figs/14.png")
    c2.image(image) 
    
    c1,cc,c2 = st.columns([4,0.5,2])
    c1.write(r"""
    $~$
    
    Тангенциальные компоненты вектора
    
    (Nédélec)    
    """)
    image = Image.open("pages/figs/15.png")
    c2.image(image) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import streamlit as st
import numpy as np
import schemdraw
import schemdraw.elements as elm
from io import BytesIO
import matplotlib.pyplot as plt
import subprocess, sys, os
from io import BytesIO

def dibujar_circuito_original():
    with schemdraw.Drawing() as d:
        d += elm.SourceV().up().label("20V")
        d += elm.Resistor().right().label("R1=6Ω")
        d += elm.Dot(open=True).label("a")
        d += elm.Resistor().right().label("R2=4Ω")
        d += elm.Dot(open=True).label("b")
        d += elm.Line().down()
        d += elm.SourceV().down().label("12V")
        d += elm.Resistor().left().label("R3=2Ω")
        d += elm.Dot(open=True).label("c")
        d += elm.Line().up()

        buffer = BytesIO()
        d.save(buffer, 'circuito.png')  # ¡sin fmt!
        buffer.seek(0)
        return buffer

def dibujar_circuito_supermalla():
    with schemdraw.Drawing() as d:
        d += elm.SourceV().up().label("20V")
        d += elm.Resistor().right().label("R1=6Ω")
        d += elm.Dot(open=True).label("a")
        d += elm.Resistor().right().label("R2=4Ω")
        d += elm.Dot(open=True).label("b")

        buffer = BytesIO()
        d.save(buffer, 'supermalla.png')  # <-- aquí se corrige
        buffer.seek(0)
        return buffer

def main():
    st.title(" Análisis de Supermallas ")
    st.write("Visualización paso a paso del procedimiento con diagramas y cálculos.")

    st.header("1. Circuito original con mallas")
    st.image(dibujar_circuito_original(), caption="Circuito original con corrientes de malla")

    st.header("2. Circuito (Supermalla)")
    st.image(dibujar_circuito_supermalla(), caption="Circuito reducido con supermalla")

    # === LKC ===
    st.header("1) Aplicación de LKC en el nodo 'a'")
    st.write("""
    Aplico la **Ley de Corrientes de Kirchhoff (KCL)** en el nodo **a**:
    - Se suman corrientes que entran y salen del nodo.
    - Ecuaciones obtenidas:
    """)
    st.latex(r"I_1 = IF_1 + I_2")
    st.latex(r"I_1 - I_2 = IF_1")
    st.latex(r"I_1 - I_2 = 4 \quad (1)")

    # === LKV ===
    st.header("2) LKV en la Supermalla")
    st.write("Aplico la **Ley de Voltajes de Kirchhoff (KVL)** alrededor de la supermalla:")
    st.latex(r"I_1R_1 + I_1R_2 + I_2R_3 = 32")
    st.latex(r"10I_1 + 2I_2 = 32 \quad (2)")

    # === Sistema de ecuaciones ===
    st.header("3) Sistema de ecuaciones")
    st.write("De los pasos anteriores obtenemos el sistema:")
    st.latex(r"I_1 - I_2 = 4")
    st.latex(r"10I_1 + 2I_2 = 32")

    # === Método de Cramer ===
    st.header("4️)  Resolviendo con el Método de Cramer")

    # Matriz de coeficientes
    A = np.array([[1, -1], [10, 2]])
    b = np.array([4, 32])

    # Determinantes
    A1 = np.array([[4, -1], [32, 2]])
    A2 = np.array([[1, 4], [10, 32]])
    detA = round(np.linalg.det(A))
    detA1 = round(np.linalg.det(A1))
    detA2 = round(np.linalg.det(A2))

    I1 = detA1 / detA
    I2 = detA2 / detA

    # Mostrar matrices y determinantes usando LaTeX
    st.markdown("**Matriz de coeficientes A:**")
    st.latex(r"A = \begin{bmatrix} 1 & -1 \\ 10 & 2 \end{bmatrix}")
    st.latex(r"\Delta = " + str(detA))

    st.markdown("**Matriz A1 (columna de I1 reemplazada):**")
    st.latex(r"A_1 = \begin{bmatrix} 4 & -1 \\ 32 & 2 \end{bmatrix}")
    st.latex(r"\Delta_1 = " + str(detA1))

    st.markdown("**Matriz A2 (columna de I2 reemplazada):**")
    st.latex(r"A_2 = \begin{bmatrix} 1 & 4 \\ 10 & 32 \end{bmatrix}")
    st.latex(r"\Delta_2 = " + str(detA2))

    # Mostrar corrientes gráficamente como en la hoja usando fracciones
    st.markdown("**Cálculo de las corrientes usando Cramer:**")
    st.latex(rf"I_1 = \frac{{\Delta_1}}{{\Delta}} = \frac{{{detA1}}}{{{detA}}} \approx {round(I1,3)}\,\mathrm{{A}}")
    st.latex(rf"I_2 = \frac{{\Delta_2}}{{\Delta}} = \frac{{{detA2}}}{{{detA}}} \approx {round(I2,3)}\,\mathrm{{A}}")



    # === Tensiones ===
    st.header("5) Tensiones en Resistencias (Ley de Ohm)")
    R1, R2, R3 = 6, 4, 2
    VR1, VR2, VR3 = I1*R1, I1*R2, I2*R3

    st.write("Aplicamos V = I * R:")
    st.latex(r"V_{R1} = I_1 \cdot R_1 = " + f"{round(VR1,2)} V")
    st.latex(r"V_{R2} = I_1 \cdot R_2 = " + f"{round(VR2,2)} V")
    st.latex(r"V_{R3} = I_2 \cdot R_3 = " + f"{round(VR3,2)} V")

   

    # === Resumen final ===
    st.header("6) Resumen Final")
    st.write(f"""
    - I1 = {round(I1,3)} A  
    - I2 = {round(I2,3)} A  
    - VR1 = {round(VR1,2)} V  
    - VR2 = {round(VR2,2)} V  
    - VR3 = {round(VR3,2)} V  
    """)

    # === Conclusión ===
    st.header("7) Conclusión del análisis de supermallas")
    st.info("""
    El circuito fue resuelto aplicando:
    - La Ley de Corrientes de Kirchhoff (KCL) en el nodo 'a'
    - La Ley de Voltajes de Kirchhoff (KVL) en la supermalla
    - El método de Cramer para resolver el sistema de ecuaciones
    - La Ley de Ohm para calcular tensiones
    """)

    st.success(" Los resultados obtenidos permiten conocer corrientes y tensiones en cada resistencia.")


if __name__ == "__main__":
    main()
    

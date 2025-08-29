import numpy as np

def main():
    print("Análisis de Supermallas:")

    print("=======================================\n") 
    #=== CIRCUITO ORIGINAL === 
    print("Circuito original con corrientes de malla:\n")
    print(" (20V) ")
    print(" | ")
    print(" ( )---R1=6Ω---(a)---R2=4Ω---(b) ") 
    print(" | I1 → ↑ I3 ") 
    print(" | (a) ")
    print(" | ")
    print(" ( )---R3=2Ω---(c)---(12V) ") 
    print(" I2 → ") 
    print("\n") 
    
    # === CIRCUITO SUPERMALLA ===
    print("Circuito equivalente (Supermalla, fuente de corriente eliminada):\n")
    print(" (20V) ") 
    print(" | ")
    print(" ( )---R1=6Ω---(a)---R2=4Ω---(b) ")
    print(" | R3=2Ω---(12V) ")
    print(" | ")
    print(" ------------------------------- ") 
    print("\n")


    print("Quitamos la fuente de corriente entre las dos mallas (I1 e I2)")
    print("y la reemplazamos por un circuito abierto.\n")

    # === LKC ===
    print("=== 1) Aplicación de LKC en el nodo 'a' ===")
    print("Aplico LKC al nodo 'a' -> Se suman corrientes que entran y salen del nodo:")
    print("ΣI_entro = ΣI_sale -> Principio de conservación de carga\n")
    print("I1 = IF1 + I2  -> La corriente de la malla izquierda se reparte en IF1 y en I2")
    print("I1 - I2 = IF1  -> Se despeja IF1 en función de las otras corrientes")

    print("\nRestricciones de corriente:")
    print("I1 = IF1 + I2  -> Corriente de la malla izquierda se reparte")
    print("I1 - I2 = IF1  -> Se despeja IF1 en función de las corrientes")
    print("I1 - I2 = 4A   (1) -> Como IF1 = 4A, queda la primera ecuación \n")

    # === LKV Supermalla ===
    print("=== 2) LKV Análisis de la Supermalla ===")
    print("Σ = 0  -> Se aplica Ley de Voltajes de Kirchhoff en la supermalla")
    print("I1 - VR1 - VR2 - VR3 + I2 = 0  -> Sumatoria de voltajes alrededor de la supermalla")
    print("ΣI + I2 = VR1 + VR2 + VR3  -> Reordenando términos")
    print("I1*R1 + I1*R2 + I2*R3 = 32V  -> Sustituyendo caídas de voltaje por ley de Ohm")
    print("I1(R1 + R2) + I2*R3 = 32V  -> Se agrupan resistencias asociadas a I1")
    print("10*I1 + 2*I2 = 32V   (2)  -> Se sustituyen valores numéricos de resistencias y fuente\n")

    # === Sistema de ecuaciones ===
    print("=== 3) Sistema de ecuaciones ===")
    print("1) I1 - I2 = 4   -> Ecuación obtenida con KCL en el nodo 'a'")
    print("2) 10*I1 + 2*I2 = 32   -> Ecuación obtenida con KVL en la supermalla\n")
    print("-> Con estas dos ecuaciones ya podemos resolver el sistema\n")

    # === Método de Cramer ===
    print("=== 4) Resolviendo por el Método de Cramer ===\n")
    print("Aplicamos el método de determinantes para resolver el sistema de dos ecuaciones:")

    # Δ
    A = np.array([[1, -1],
                [10, 2]])
    b = np.array([4, 32])

    detA = round(np.linalg.det(A))

    print("\nMatriz A (coeficientes):")
    print(A)
    print("Det(A) = Δ =", detA, "-> Determinante de la matriz principal\n")

    # Δ1
    A1 = np.array([[4, -1],
                [32, 2]])
    detA1 = round(np.linalg.det(A1))
    print("Matriz A1 (reemplazando columna de I1 por resultados):")
    print(A1)
    print("Det(A1) =", detA1, "\n")

    # Δ2
    A2 = np.array([[1, 4],
                [10, 32]])
    detA2 = round(np.linalg.det(A2))
    print("Matriz A2 (reemplazando columna de I2 por resultados):")
    print(A2)
    print("Det(A2) =", detA2, "\n")

    print("Relaciones del método de Cramer:")
    print("Δ =", detA)
    print("Δ1 =", detA1)
    print("Δ2 =", detA2, "\n")

    I1 = detA1 / detA
    I2 = detA2 / detA

    print("Resultados de corrientes:")
    print("I1 = Δ1/Δ =", detA1, "/", detA, "=", round(I1, 3), "A  -> Corriente en la primera malla")
    print("I2 = Δ2/Δ =", detA2, "/", detA, "=", round(I2, 3), "A  -> Corriente en la segunda malla\n")

    # === Tensiones en resistencias ===
    print("=== 5) Tensiones en resistencias (Ley de Ohm) ===\n")
    print("Ahora aplicamos V = I * R para calcular las caídas de tensión en cada resistencia:")

    R1, R2, R3 = 6, 4, 2

    VR1 = I1 * R1
    VR2 = I1 * R2
    VR3 = I2 * R3

    print("VR1 = I1 * R1 =", round(I1, 3), "*", R1, "=", round(VR1, 2), "V  -> Tensión en R1")
    print("VR2 = I1 * R2 =", round(I1, 3), "*", R2, "=", round(VR2, 2), "V  -> Tensión en R2")
    print("VR3 = I2 * R3 =", round(I2, 3), "*", R3, "=", round(VR3, 2), "V  -> Tensión en R3")

    # === Verificación ===
    print("\n=== 6) Verificación de las ecuaciones originales ===\n")
    print("Sustituimos los valores de I1 e I2 en las ecuaciones para confirmar:")

    eq1 = round(I1 - I2, 3)
    eq2 = round(10*I1 + 2*I2, 3)

    print("Ecuación (1): I1 - I2 =", eq1, "≈ 4 ✅" if abs(eq1-4) < 1e-3 else "❌")
    print("Ecuación (2): 10*I1 + 2*I2 =", eq2, "≈ 32 ✅" if abs(eq2-32) < 1e-3 else "❌")

    # === Resumen final ===
    print("\n=== 7) Resumen Final ===")
    print("Corrientes obtenidas:")
    print(f"I1 = {round(I1,3)} A  -> corriente en la malla izquierda")
    print(f"I2 = {round(I2,3)} A  -> corriente en la malla derecha")
    print("\nTensiones en resistencias:")
    print(f"VR1 = {round(VR1,2)} V")
    print(f"VR2 = {round(VR2,2)} V")
    print(f"VR3 = {round(VR3,2)} V")

    # === Conclusión ===
    print("\n=== 8) Conclusión del análisis de supermallas ===")
    print("Se resolvió el circuito aplicando:")
    print("- La Ley de Corrientes de Kirchhoff (KCL) en el nodo 'a'")
    print("- La Ley de Voltajes de Kirchhoff (KVL) en la supermalla")
    print("- El método de Cramer para resolver el sistema de ecuaciones lineales")
    print("- La Ley de Ohm para calcular tensiones en resistencias")
    print("Con esto se determinaron las corrientes I1, I2 y las tensiones asociadas,")
    print("verificando que los resultados satisfacen las ecuaciones planteadas.\n")

    print("=======================================")
    print("       FIN DEL PROCEDIMIENTO ✅        ")
    print("=======================================")



if __name__ == "__main__":
    main()

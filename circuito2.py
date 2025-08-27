import numpy as np

def main():
    print("=======================================")
    print("        Análisis de Mallas              ")
    print("=======================================\n")

    # === CIRCUITO ORIGINAL ===
    print("Circuito original con corrientes de malla:\n")
    print("       (20V)                            ")
    print("        |                               ")
    print("       ( )---R1=6Ω---(a)---R2=4Ω---(b)  ")
    print("        |    I1 →           ↑ I3        ")
    print("        |                  (a)          ")
    print("        |                               ")
    print("       ( )---R3=2Ω---(c)---(12V)        ")
    print("             I2 →                       ")
    print("\n")

    # === CIRCUITO SUPERMALLA ===
    print("Circuito equivalente (Supermalla, fuente de corriente eliminada):\n")
    print("       (20V)                            ")
    print("        |                               ")
    print("       ( )---R1=6Ω---(a)---R2=4Ω---(b)  ")
    print("        |                 R3=2Ω---(12V) ")
    print("        |                               ")
    print("        ------------------------------- ")
    print("\n")

    print("Análisis de Supermallas:")
    print("Quitamos la fuente de corriente entre las dos mallas (I1 e I2)")
    print("y la reemplazamos por un circuito abierto.\n")

    # === LKC ===
    print("Aplico LKC al nodo 'a':")
    print("ΣI_entro = ΣI_sale\n")
    print("Restricciones de corriente:")
    print("I1 - I2 = 4A   (1)\n")

    # === LKV Supermalla ===
    print("LKV Análisis Supermalla Σ=0:")
    print("I1*R1 + I1*R2 + I2*R3 = 32V")
    print("10*I1 + 2*I2 = 32   (2)\n")

    # === Sistema de ecuaciones ===
    print("Sistema de ecuaciones:")
    print("1) I1 - I2 = 4")
    print("2) 10*I1 + 2*I2 = 32\n")

    # === Método de Cramer ===
    print("Resolviendo por el Método de Cramer:\n")
    
    # Δ
    A = np.array([[1, -1],
                  [10, 2]])
    b = np.array([4, 32])

    detA = round(np.linalg.det(A))

    print("Matriz A:")
    print(A)
    print("Det(A) =", detA, "\n")

    # Δ1
    A1 = np.array([[4, -1],
                   [32, 2]])
    detA1 = round(np.linalg.det(A1))
    print("Δ1")
    print(A1)
    print("Det(A1) =", detA1, "\n")
#------------------------------------------------#


    # Δ2
    A2 = np.array([[1, 4],
                   [10, 32]])
    detA2 = round(np.linalg.det(A2))
    print("Δ2")
    print(A2)
    print("Det(A2) =", detA2, "\n")
#------------------------------------------------#
    print("Δ =", detA)
    print("Δ1 =", detA1)
    print("Δ2 =", detA2, "\n")
   

    I1 = detA1 / detA
    I2 = detA2 / detA

    print("Resultados de corrientes:")
    print("I1 = Δ1/Δ =", detA1, "/", detA, "=", round(I1, 3), "A")
    print("I2 = Δ2/Δ =", detA2, "/", detA, "=", round(I2, 3), "A\n")

    # === Tensiones en resistencias ===
    print("Tensiones en resistencias (Ohm):\n")

    R1, R2, R3 = 6, 4, 2

    VR1 = I1 * R1
    VR2 = I1 * R2
    VR3 = I2 * R3

    print("VR1 = I1 * R1 =", round(I1, 3), "*", R1, "=", round(VR1, 2), "V")
    print("VR2 = I1 * R2 =", round(I1, 3), "*", R2, "=", round(VR2, 2), "V")
    print("VR3 = I2 * R3 =", round(I2, 3), "*", R3, "=", round(VR3, 2), "V")

    print("\n=======================================")
    print("        FIN DEL PROCEDIMIENTO           ")
    print("=======================================")

if __name__ == "__main__":
    main()

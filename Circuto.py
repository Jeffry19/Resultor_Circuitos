import numpy as np            # Para operaciones matemáticas y resolución de sistemas de ecuaciones
import matplotlib.pyplot as plt  # Para graficar el circuito
import networkx as nx         # Para crear y dibujar grafos que representan las mallas
import csv                    # Para guardar los resultados en un archivo CSV

# Función principal que resuelve las corrientes en un circuito por el método de mallas
def resolver_mallas():
    # Solicitar al usuario el número de mallas
    while True:
        try:
            n = int(input("Número de mallas: "))
            if n < 1:
                print("Debe haber al menos 1 malla.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    # Inicializar matriz de coeficientes A (para el sistema de ecuaciones)
    # y vector b (fuentes de voltaje)
    A = np.zeros((n, n))
    b = np.zeros(n)

    # Listas para almacenar resistencias de cada malla, fuentes y acoplamientos
    resistencias = []
    fuentes = []
    acoplamientos = {}

    # Pedir al usuario las resistencias de cada malla
    print("\n=== Definir resistencias en cada malla ===")
    for i in range(n):
        while True:
            try:
                R = float(input(f"Resistencia total de la malla {i+1} (Ω): "))
                if R < 0:
                    print("La resistencia no puede ser negativa.")
                    continue
                resistencias.append(R)
                A[i, i] = R  # diagonal de la matriz A
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

    # Pedir resistencias compartidas entre mallas (acoplamientos)
    print("\n=== Definir acoplamientos entre mallas (resistencias compartidas) ===")
    for i in range(n):
        for j in range(i+1, n):
            while True:
                try:
                    R_ij = float(input(f"Resistencia compartida entre malla {i+1} y {j+1} (0 si no hay): "))
                    if R_ij < 0:
                        print("La resistencia compartida no puede ser negativa.")
                        continue
                    if R_ij != 0:
                        # Ajustar matriz A según la teoría de mallas
                        A[i, i] += R_ij
                        A[j, j] += R_ij
                        A[i, j] -= R_ij
                        A[j, i] -= R_ij
                        acoplamientos[(i, j)] = R_ij  # Guardar acoplamiento para graficar
                    break
                except ValueError:
                    print("Ingrese un valor numérico válido.")

    # Pedir al usuario las fuentes de voltaje de cada malla
    print("\n=== Fuentes de voltaje ===")
    for i in range(n):
        while True:
            try:
                V = float(input(f"Suma de fuentes de voltaje en malla {i+1} (V): "))
                b[i] = V
                fuentes.append(V)
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

    # Resolver el sistema de ecuaciones A * I = b para encontrar corrientes
    try:
        corrientes = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: el sistema no tiene solución única.")
        return

    # Mostrar las corrientes calculadas
    print("\n=== Resultados ===")
    for i, I in enumerate(corrientes, start=1):
        print(f"Corriente I{i} = {I:.3f} A")

    # Guardar resultados en un archivo CSV con codificación UTF-8
    with open("resultados_mallas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Malla", "Resistencia (Ω)", "Fuente (V)", "Corriente (A)"])
        for i in range(n):
            writer.writerow([f"Malla {i+1}", resistencias[i], fuentes[i], corrientes[i]])
    print("\nResultados guardados en 'resultados_mallas.csv'")

    # Llamar a la función para dibujar el circuito
    dibujar_circuito(n, resistencias, fuentes, corrientes, acoplamientos)


# Función para dibujar el circuito usando un grafo
def dibujar_circuito(n, resistencias, fuentes, corrientes, acoplamientos=None):
    G = nx.DiGraph()  # Grafo dirigido para mostrar la dirección de la corriente

    # Crear nodos para cada malla
    for i in range(n):
        G.add_node(f"Malla {i+1}")
        G.nodes[f"Malla {i+1}"]["resistencia"] = resistencias[i]
        G.nodes[f"Malla {i+1}"]["fuente"] = fuentes[i]
        G.nodes[f"Malla {i+1}"]["corriente"] = corrientes[i]

    # Crear aristas para resistencias compartidas
    if acoplamientos:
        for (i, j), R_ij in acoplamientos.items():
            if R_ij != 0:
                # Dirección arbitraria de i a j
                G.add_edge(f"Malla {i+1}", f"Malla {j+1}", resistencia=R_ij)

    # Posición de los nodos en un círculo
    pos = nx.circular_layout(G)

    # Labels de nodos con resistencia, voltaje y corriente
    labels = {node: f"{node}\nR={data['resistencia']}Ω\nV={data['fuente']}V\nI={data['corriente']:.2f}A"
              for node, data in G.nodes(data=True)}

    # Dibujar nodos y labels
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color="lightblue", font_size=8)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)

    # Labels de aristas (resistencias compartidas)
    if acoplamientos:
        edge_labels = {(f"Malla {i+1}", f"Malla {j+1}"): f"R={R_ij}Ω"
                       for (i, j), R_ij in acoplamientos.items() if R_ij != 0}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Mostrar el gráfico
    plt.title("Esquema simplificado de mallas")
    plt.show()


# Ejecutar la función principal si se ejecuta directamente el script
if __name__ == "__main__":
    resolver_mallas()

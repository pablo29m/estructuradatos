import json

def main():
    f = open('archivo.json')
    estructura = json.load(f)
    f.close()
    sort = ordenar(estructura)
    print("Nodos:",estructura['P'])
    print("Aristas:",estructura['E']);
    if(sort==None):
            print("El grafo es ciclico")
    else:
        print("Sort Topologico:",sort)
def ordenar(estructura):
    nodos = estructura['P']
    aristas = estructura['E']
    cola=[]

    # Creo un  diccionario para guardar los grados de entrada de cada nodo
    grados= {}
    #Hago que cada nodo tenga grado 0 para inicializarlo
    for nodo in nodos:
        grados[nodo] = 0

    # Relleno el diccionario con los grados de entrada de cada nodo, para eso reviso las aristas
    for origen, destinos in aristas.items():
        for destino in destinos:
            grados[destino] = grados.get(destino, 0) + 1

    # Guardo en la cola solo aquellos nodos que tengan grado de entrada 0
    for nodo,grado in grados.items():
        if grado==0:
            cola.append(nodo)

    # Lista para guardar el orden topológico
    orden_topologico = []

    #Si hay al menos un nodo con grado de entrada 0 en la cola, entra al while
    while cola:
        nodo = cola.pop(0)
        orden_topologico.append(nodo)
        #Disminuye el grado de entrada de los vecinos a ese nodo
        for vecino in aristas.get(nodo, []):
            grados[vecino] -= 1
            #Si luego de disminuir, hay mas nodos con grado de entrada 0, lo guardo en la cola
            if grados[vecino] == 0:
                cola.append(vecino)

    # Verificar si hay ciclos en el grafo
    #Si difiere la cantidad de nodos es porque hay un ciclo. Tiene que ser igual
    if len(orden_topologico) != len(nodos):
        return None  # Hay un ciclo

    return orden_topologico


main()


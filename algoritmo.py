from arbol import Nodo

conexiones = {
    "Jiloyork": {"Celaya", "CDMX", "Queretaro"},
    "CDMX": {"Jiloyork"},
    "Sonora": {"Zacatecas", "Sinaloa"},
    "Guanajuato": {"Aguascalientes"},
    "Oaxaca": {"Queretaro"},
    "Sinaloa": {"Celaya", "Sonora", "Jiloyork"},
    "Queretaro": {"Monterrey", "Oaxaca"},
    "Celaya": {"Jiloyork", "Sinaloa"},
    "Zacatecas": {"Sonora", "Monterrey", "Queretaro"},
    "Monterrey": {"Zacatecas", "Sinaloa"},
    "Tamaulipas": {"Queretaro"},
    "Aguascalientes": {"Guanajuato"}
}

def buscar_Solucion_DFS_rec(nodo, solucion, visitados, limite):
    if nodo.get_datos() == solucion: return nodo
    if limite > 0:
        visitados.append(nodo.get_datos())
        lista_hijos = []
        for un_hijo in conexiones.get(nodo.get_datos(), []):
            hijo = Nodo(un_hijo)
            if hijo.get_datos() not in visitados:
                hijo.set_padre(nodo)
                lista_hijos.append(hijo)
        nodo.set_hijos(lista_hijos)
        for nodo_hijo in nodo.get_hijos():
            sol = buscar_Solucion_DFS_rec(nodo_hijo, solucion, visitados, limite - 1)
            if sol: return sol
    return None

def DFS_prof_iter(nodo_inicial, solucion):
    for limite in range(0, 100):
        sol = buscar_Solucion_DFS_rec(nodo_inicial, solucion, [], limite)
        if sol: return sol
    return None
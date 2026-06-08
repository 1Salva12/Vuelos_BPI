from flask import Flask, render_template, request
from arbol import Nodo
from algoritmo import DFS_prof_iter, conexiones

app = Flask(__name__)

@app.route('/')
def index():
    ciudades = sorted(list(conexiones.keys()))
    return render_template('index.html', ciudades=ciudades)

@app.route('/buscar', methods=['POST'])
def buscar():
    inicio = request.form.get('inicio')
    meta = request.form.get('meta')
    
    nodo_resultado = DFS_prof_iter(Nodo(inicio), meta)
    
    ruta = []
    if nodo_resultado:
        while nodo_resultado:
            ruta.append(nodo_resultado.get_datos())
            nodo_resultado = nodo_resultado.get_padre()
        ruta = ruta[::-1]
    
    ciudades = sorted(list(conexiones.keys()))
    return render_template('index.html', ciudades=ciudades, ruta=ruta, inicio=inicio, meta=meta)

if __name__ == '__main__':
    app.run(debug=True)
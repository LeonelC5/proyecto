from flask import Flask, render_template, request, jsonify
from animes import animes

app = Flask(__name__)

current_id = 5

def get_new_id():
    global current_id
    current_id = current_id + 1
    return current_id

@app.route("/")
def anime():
    return render_template("index.html")

@app.route('/anime')
def index():
    return animes

@app.route('/anime',methods=['POST'])
def agregar():
    data = request.get_json()
    data["id"] = get_new_id()
    animes.append(data)
    return {"message": f'el anime {data["titulo"]} se creó correctamente'} 


@app.route('/anime/<id>')
def get_anime_by_id(id):
    for anime in animes:
        if anime["id"] == int(id):
            return anime
    return {"message": f'no se encontró ningún anime con el id {id}'}

@app.route('/anime/<id>',methods=['DELETE'])
def borrar(id):
    for anime in animes:
        if anime["id"] == int(id):
            animes.remove(anime)
    return {"message": f'borrado exitosamente'}

@app.route('/anime/<id>',methods=['PUT'])
def editar(id):
    dato = request.get_json()
    dato["id"] = int(id)
    for i, anime in enumerate(animes):
        if anime["id"] == int(id):
            animes[i] = dato
            return dato
    return {"message": f'no se encontró el id'}

@app.route('/anime/<id>',methods=['PATCH'])
def update(id):
    dato = request.get_json()
    for anime in animes:
        if anime["id"] ==int(id):
            anime["titulo"] = dato["titulo"]
            return dato 
    return {"message": f'No se encontró el id'}

if __name__ == '__main__':
    app.run()
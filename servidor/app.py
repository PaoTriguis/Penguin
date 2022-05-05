# python -m flask run 'codigo para hacer funcionar en la terminal' 
from flask import Flask, render_template, url_for # Importamos las librerias a ser usadas
import requests

app = Flask(__name__) # Creamos el objeto app

@app.route("/") # Llamamos al metodo route y le pasamos el argumento de la url o slug que queremos que vaya
def inicio(): # Creamos la funcion inicio
    return render_template('inicio.html') # Retornamos la renderizacion de un doc html (mostrar en pantalla)

@app.route("/contacto") 
def contacto():
    API_KEY = "889bd3eb" #API key
    titulo = "Harry Potter"
    basic_call = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="+titulo
    datos= requests.get(basic_call)
    datos=datos.json()
    titulo_de_pelicula = datos['Title']
    director_de_pelicula = datos['Director']
    datos_filtrados = {'titulo' : titulo_de_pelicula , 'director' : director_de_pelicula}
    return render_template('contacto.html', datos = datos_filtrados)

if __name__ == "__main__":
    app.run(debug=True)
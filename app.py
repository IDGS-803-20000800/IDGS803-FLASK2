from flask import Flask, render_template, request
from collections import Counter
import forms

app = Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == "POST":
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("alumnos.html", form = alum_form)

@app.route("/", methods = ["GET", "POST"])
def cajasDinamicas():
    return render_template("cajas.html")

@app.route("/cajas_renderizadas", methods=["GET", "POST"])
def cajasRenderizadas():
    numCajas = request.form.get("txtNumCajas")
    numCajas = int(numCajas)
    return render_template("cajas_renderizadas.html", numCajas = numCajas)

@app.route("/resultado_cajas", methods=["GET", "POST"])
def resultadoCajas():
    maximo = 0
    minimo = 0
    promedio = 0
    lista = []
    duplicados = {}
    contador = 1
    totalCajas = request.form.get("txtTotalCajas")
    totalCajas = int(totalCajas)
    for num in range(totalCajas):
        lista.append(request.form.get("txtN{}".format(contador)))
        contador += 1
    maximo = max(lista)
    minimo = min(lista)
    for num in lista:
        promedio = promedio + int(num)
    promedio = promedio//len(lista)
    conteo=Counter(lista)
    for clave in conteo:  
        valor=conteo[clave]
        if valor != 1:
            duplicados[clave] = valor
    return render_template("resultado_cajas.html", lista = lista, maximo = maximo, minimo = minimo, promedio = promedio, duplicados = duplicados)

if __name__ == "__main__":
    app.run(debug = True)
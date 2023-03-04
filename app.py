from flask import Flask, render_template, request, make_response, flash
from collections import Counter
from flask_wtf.csrf import CSRFProtect
from googletrans import Translator
import forms

app = Flask(__name__)
app.config["SECRET_KEY"] = "Esta es la clave encriptada"
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrado(e):
    return render_template("404.html"), 404

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    reg_user = forms.LoginForm(request.form)
    datos = ""
    if request.method == "POST" and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos = user + "@" + password
        success_message = "Bienvenido {}".format(user)
        flash(success_message)
    response = make_response(render_template("cookies.html", form = reg_user))
    if len(datos) > 0:
        response.set_cookie("datos_user", datos)
    return response

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get("datos_user")
    nombres = valor_cookie.split("@")
    return render_template("saludo.html", nom = nombres[0])

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("alumnos.html", form = alum_form)

# Ejercicio 1
@app.route("/", methods = ["GET", "POST"])
def cajasDinamicas():
    cajas_form = forms.UserForm(request.form)
    return render_template("cajas.html", form = cajas_form)

@app.route("/cajas_renderizadas", methods=["GET", "POST"])
def cajasRenderizadas():
    cajas_form = forms.UserForm(request.form)
    numCajas = request.form.get("txtNumCajas")
    numCajas = int(numCajas)
    return render_template("cajas_renderizadas.html", numCajas = numCajas, form = cajas_form)

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

@app.route("/traductor", methods=["GET", "POST"])
def traductor():
    traductor_form = forms.UserForm(request.form)
    translator = Translator()
    diccionario = {}
    palabraEspanol = request.form.get("txtEspanol")
    palabraIngles = request.form.get("txtIngles")
    diccionario[palabraEspanol] = palabraIngles
    return render_template("traductor.html")

@app.route("/resistencia", methods=["GET", "POST"])
def resistencia():
    return render_template("resistencia.html")

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug = True)
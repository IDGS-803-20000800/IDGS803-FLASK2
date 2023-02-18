from flask import Flask, render_template, request
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
    num = request.form.get("txtNum")
    return render_template("cajas_renderizadas.html", num = num)

if __name__ == "__main__":
    app.run(debug = True)
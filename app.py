from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registros = []


@app.route("/")
def inicio():
    return render_template("index.html", registros=registros)


@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    fecha_nacimiento = request.form["fecha_nacimiento"]
    dia_semana = request.form["dia_semana"]

    # No permitir números en nombre
    if not nombre.replace(" ", "").isalpha():
        return "El nombre solo puede contener letras."

    # No permitir números en apellido
    if not apellido.replace(" ", "").isalpha():
        return "El apellido solo puede contener letras."

    nuevo_registro = {
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "dia_semana": dia_semana
    }

    registros.append(nuevo_registro)

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
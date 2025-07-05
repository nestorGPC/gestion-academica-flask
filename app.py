from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://adminuser:Root1234@gestion-academica-sql-server.database.windows.net:1433/gestion-academica-db?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Comentario para redeploy en Azure
# ------------------------------
# Modelo Estudiante
# ------------------------------
class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

class Carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    id_carrera = db.Column(db.Integer, nullable=False)

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)

class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, nullable=False)
    id_curso = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

# ------------------------------
# Crear base de datos
# ------------------------------
with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()

# ------------------------------
# Rutas Menú Principal
# ------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# ------------------------------
# Rutas Estudiantes
# ------------------------------
@app.route("/estudiantes")
def listar_estudiantes():
    estudiantes = Estudiante.query.all()
    return render_template("estudiantes.html", estudiantes=estudiantes)

@app.route("/estudiantes/agregar", methods=["POST"])
def agregar_estudiante():
    nombre = request.form["nombre"]
    carrera = request.form["carrera"]
    nuevo = Estudiante(nombre=nombre, carrera=carrera)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for("listar_estudiantes"))

@app.route("/estudiantes/editar/<int:id>")
def formulario_editar_estudiante(id):
    estudiante = Estudiante.query.get(id)
    return render_template("editar_estudiante.html", estudiante=estudiante)

@app.route("/estudiantes/editar/<int:id>", methods=["POST"])
def editar_estudiante(id):
    estudiante = Estudiante.query.get(id)
    estudiante.nombre = request.form["nombre"]
    estudiante.carrera = request.form["carrera"]
    db.session.commit()
    return redirect(url_for("listar_estudiantes"))

@app.route("/estudiantes/eliminar/<int:id>")
def eliminar_estudiante(id):
    estudiante = Estudiante.query.get(id)
    db.session.delete(estudiante)
    db.session.commit()
    return redirect(url_for("listar_estudiantes"))

# ------------------------------
# Rutas Carreras
# ------------------------------
@app.route("/carreras")
def listar_carreras():
    carreras = Carrera.query.all()
    return render_template("carreras.html", carreras=carreras)

@app.route("/carreras/agregar", methods=["POST"])
def agregar_carrera():
    nombre = request.form["nombre"]
    nueva = Carrera(nombre=nombre)
    db.session.add(nueva)
    db.session.commit()
    return redirect(url_for("listar_carreras"))

@app.route("/carreras/editar/<int:id>")
def formulario_editar_carrera(id):
    carrera = Carrera.query.get(id)
    return render_template("editar_carrera.html", carrera=carrera)

@app.route("/carreras/editar/<int:id>", methods=["POST"])
def editar_carrera(id):
    carrera = Carrera.query.get(id)
    carrera.nombre = request.form["nombre"]
    db.session.commit()
    return redirect(url_for("listar_carreras"))

@app.route("/carreras/eliminar/<int:id>")
def eliminar_carrera(id):
    carrera = Carrera.query.get(id)
    db.session.delete(carrera)
    db.session.commit()
    return redirect(url_for("listar_carreras"))

# ------------------------------
# Rutas Cursos
# ------------------------------
@app.route("/cursos")
def listar_cursos():
    cursos = Curso.query.all()
    return render_template("cursos.html", cursos=cursos)

@app.route("/cursos/agregar", methods=["POST"])
def agregar_curso():
    nombre = request.form["nombre"]
    id_carrera = request.form["id_carrera"]
    nuevo = Curso(nombre=nombre, id_carrera=id_carrera)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for("listar_cursos"))

@app.route("/cursos/editar/<int:id>")
def formulario_editar_curso(id):
    curso = Curso.query.get(id)
    return render_template("editar_curso.html", curso=curso)

@app.route("/cursos/editar/<int:id>", methods=["POST"])
def editar_curso(id):
    curso = Curso.query.get(id)
    curso.nombre = request.form["nombre"]
    curso.id_carrera = request.form["id_carrera"]
    db.session.commit()
    return redirect(url_for("listar_cursos"))

@app.route("/cursos/eliminar/<int:id>")
def eliminar_curso(id):
    curso = Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for("listar_cursos"))

# ------------------------------
# Rutas Profesores
# ------------------------------
@app.route("/profesores")
def listar_profesores():
    profesores = Profesor.query.all()
    return render_template("profesores.html", profesores=profesores)

@app.route("/profesores/agregar", methods=["POST"])
def agregar_profesor():
    nombre = request.form["nombre"]
    especialidad = request.form["especialidad"]
    nuevo = Profesor(nombre=nombre, especialidad=especialidad)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for("listar_profesores"))

@app.route("/profesores/editar/<int:id>")
def formulario_editar_profesor(id):
    profesor = Profesor.query.get(id)
    return render_template("editar_profesor.html", profesor=profesor)

@app.route("/profesores/editar/<int:id>", methods=["POST"])
def editar_profesor(id):
    profesor = Profesor.query.get(id)
    profesor.nombre = request.form["nombre"]
    profesor.especialidad = request.form["especialidad"]
    db.session.commit()
    return redirect(url_for("listar_profesores"))

@app.route("/profesores/eliminar/<int:id>")
def eliminar_profesor(id):
    profesor = Profesor.query.get(id)
    db.session.delete(profesor)
    db.session.commit()
    return redirect(url_for("listar_profesores"))

# ------------------------------
# Rutas Matrículas
# ------------------------------
@app.route("/matriculas")
def listar_matriculas():
    matriculas = Matricula.query.all()
    return render_template("matriculas.html", matriculas=matriculas)

@app.route("/matriculas/agregar", methods=["POST"])
def agregar_matricula():
    id_estudiante = request.form["id_estudiante"]
    id_curso = request.form["id_curso"]
    fecha = request.form["fecha"]
    nueva = Matricula(id_estudiante=id_estudiante, id_curso=id_curso, fecha=fecha)
    db.session.add(nueva)
    db.session.commit()
    return redirect(url_for("listar_matriculas"))

@app.route("/matriculas/editar/<int:id>")
def formulario_editar_matricula(id):
    matricula = Matricula.query.get(id)
    return render_template("editar_matricula.html", matricula=matricula)

@app.route("/matriculas/editar/<int:id>", methods=["POST"])
def editar_matricula(id):
    matricula = Matricula.query.get(id)
    matricula.id_estudiante = request.form["id_estudiante"]
    matricula.id_curso = request.form["id_curso"]
    matricula.fecha = request.form["fecha"]
    db.session.commit()
    return redirect(url_for("listar_matriculas"))

@app.route("/matriculas/eliminar/<int:id>")
def eliminar_matricula(id):
    matricula = Matricula.query.get(id)
    db.session.delete(matricula)
    db.session.commit()
    return redirect(url_for("listar_matriculas"))

# ------------------------------
# Ejecutar app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)

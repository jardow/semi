from flask import Flask, render_template, request
from fun.funciones import existe_archivo,leer_usuario,escribir_usuario

app = Flask(__name__)

@app.route('/')
def inicio() -> 'html':
    return render_template('index.html')

@app.route('/login')
def login() -> 'html':
    return render_template('login.html')


@app.route('/mostrar', methods=['POST','GET'])
def agrega() -> 'html':
 #   nombre = request.form['nombre']
    usuarioE = request.form['usuarioE']
    if (existe_archivo(usuarioE + ".user")):
        (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = leer_usuario(usuarioE)
        user=leer_usuario(usuarioE)
        return render_template('mostrar.html',
                               nom=nombre,
                               ed=edad,
                               est="" + str(estatura_m) + " m y " + str(estatura_cm) + " centímetros",
                               sex=sexo,
                               pa=pais,
                               num_amigos=amigos,
                               esta=estado,
                               mur=muro)
    else:
     return render_template('crear.html')

@app.route('/crear', methods=['POST'])
def ingresar() -> 'html':
    nombre = request.form['nom']
    global Nom
    Nom = nombre
    anio = int(request.form['an'])
    an = 2019-anio-1
    estatura = float(request.form['est'])
    metros = int(estatura)
    centimetros = int((estatura - metros) * 100)
    sexo = request.form['sex']
    pais = request.form['pa']
    amigos = request.form['ami'].split(",")
    global amig
    amig= request.form['ami'].split(",")
    estado = request.form['esta']
    muro=[]
    escribir_usuario(nombre,an,metros,centimetros,sexo,pais,amigos,estado,muro)
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = leer_usuario(Nom)
    return render_template('perfil.html',
                           titulo='ENIGMA II',
                           nom=nombre,
                           ed=edad,
                           est="" + str(estatura_m) + " m y " + str(estatura_cm) + " centímetros",
                           sex=sexo,
                           pa=pais,
                           num_amigos=amigos,
                           esta=estado,
                           mur=muro)
app.run()

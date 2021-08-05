from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# importamos la libreriaa de Flask
# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# creamos una ruta a raiz
app = Flask(__name__, static_url_path='/static')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12315948006'
app.config['MYSQL_DB'] = 'guerrero'
mysql = MySQL(app)
app.secret_key = 'mysecretkey'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/qsomos")
def quienessomos():
    return render_template("quienessomos.html")


# estamos crando un metodo de ruteo para el template html_rejilla.html.
@app.route("/grid_html")
def rejilla_html():
    return render_template("html_rejilla.html")


# estamos crando un metodo de ruteo para el template registro.
@app.route("/registro")
def registro_html():
    return render_template("registroxd.html")
@app.route("/updatedtos")
def updatedtos_html():
    return render_template("update.html")

@app.route("/guardar_datos", methods=['POST'])
def guardar_datos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        numerodetelefono = request.form['numerodetelefono']
        correo = request.form['correo']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO datos (nombre, descripcion, numerodetelefono, correo) VALUES (%s,%s,%s,%s)",
                   (nombre, descripcion, numerodetelefono, correo))
        mysql.connection.commit()
        cur.close()



    return redirect("/consultar_datos")

@app.route("/consultar_datos")
def consultar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datos')
    date = cur.fetchall()
    print(date)
    cur.close()
    return render_template("datos.html", date=date)



@app.route('/edit/<id>')
def get_datos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datos WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editar.html', date=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        numerodetelefono = request.form['numerodetelefono']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE datos
            SET nombre = %s,
                descripcion = %s,
                numerodetelefono = %s,
                correo = %s
            WHERE id = %s
        """, (nombre, descripcion, numerodetelefono, correo, id))
        mysql.connection.commit()
        return redirect(url_for('consultar'))


@app.route('/delete/<string:id>', methods = ['GET','POST'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM datos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    return redirect("/consultar_datos")






@app.route("/sugerencias")
def sugerenicas_html():

    return render_template("Sugerencias.html")
@app.route("/guardar_sugerencias", methods=['POST'])
def guardar_sugerencias():
    if request.method == 'POST':
        nombre2 = request.form['nombre2']
        sugerencias = request.form['sugerencias']
        numerodetelefono2 = request.form['numerodetelefono2']
        correo2 = request.form['correo2']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sugerenciasg (nombre, sugerencias, telefono, correo) VALUES (%s,%s,%s,%s)",
                   (nombre2, sugerencias, numerodetelefono2, correo2))
        mysql.connection.commit()
        cur.close()
    return redirect("/consultar_sugerencias")

@app.route("/consultar_sugerencias")
def consultar_sugerencias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sugerenciasg')
    sug = cur.fetchall()
    print(sug)
    cur.close()
    return render_template("sugerenciasg.html", sug=sug)
@app.route('/editar/<id>')
def editar_datos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sugerenciasg WHERE id = %s', (id))
    sug = cur.fetchall()
    cur.close()
    print(sug[0])
    return render_template('editars.html', sug=sug[0])


@app.route('/actualizar/<id>', methods=['POST'])
def actualizar_sugerencia(id):
    if request.method == 'POST':
        nombre2 = request.form['nombre2']
        sugerenicas = request.form['sugerenicas']
        numerodetelefono2 = request.form['numerodetelefono2']
        correo2 = request.form['correo2']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE sugerenciasg
            SET nombre = %s,
                sugerencias = %s,
                telefono = %s,
                correo = %s
            WHERE id = %s
        """, (nombre2, sugerenicas, numerodetelefono2, correo2, id))
        mysql.connection.commit()
        return redirect(url_for('consultar_sugerencias'))
@app.route('/eliminar/<string:id>', methods = ['GET','POST'])
def eliminar_sugerencias(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM sugerenciasg WHERE id = {0}'.format(id))
    mysql.connection.commit()
    return redirect("/consultar_sugerencias")

@app.route("/quehacemos")
def quehacemos_html():
    return render_template("quehacemos.html")


# creamos una condicional para tener un archivo
if __name__ == '__main__':
    app.run(port=3000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

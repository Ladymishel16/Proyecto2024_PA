from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'duki'
app.config['MYSQL_DB'] = 'Heladeria'

mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_Categorias', methods=['POST'])
def add_Categorias():
    if request.method == 'POST':
        categoria_nombre = request.form['categoria_nombre']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Categorias (categoria_nombre) VALUES (%s)', (categoria_nombre,))
        mysql.connection.commit()
        flash('Categoria agregada correctamente')
        return redirect(url_for('Index'))
    
@app.route('/add_Productos', methods=['POST'])
def add_Productos():
    if request.method == 'POST':
        producto_nombre = request.form['producto_nombre']
        producto_precio = request.form['producto_precio']
        producto_descripcion = request.form['producto_descripcion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Productos (producto_nombre,producto_precio,producto_descripcion) VALUES (%s,%s,%s)', (producto_nombre,producto_precio,producto_descripcion))
        mysql.connection.commit()
        flash('Producto agregado correctamente')
        return redirect(url_for('Index'))
    
@app.route('/add_Clientes', methods=['POST'])
def add_Cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Clientes (nombre, correo,telefono,direccion) VALUES (%s,%s,%s,%s)', (nombre,correo,telefono,direccion))
        mysql.connection.commit()
        flash('Cliente agregado correctamente')
        return redirect(url_for('Index'))
    
@app.route('/add_Pedidos', methods=['POST'])
def add_Pedidos():
    if request.method == 'POST':
        fecha_pedido = request.form['fecha_pedido']
        precio_total = request.form['precio_total']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Pedidos (fecha_pedidos,precio_total) VALUES (%s,%s)', (fecha_pedido,precio_total))
        mysql.connection.commit()
        flash('Pedido agregado correctamente')
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

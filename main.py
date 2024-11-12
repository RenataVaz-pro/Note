from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from flask import jsonify
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('notas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    conn.close()
    return render_template('index.html', notas=notas)

@app.route('/adicionar', methods=['POST'])
def adicionar_nota(): 
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notas (titulo, descricao) VALUES (?, ?)", (titulo, descricao))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/editar/<int:nota_id>', methods=['POST'])
def editar_nota(nota_id):
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, nota_id))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/salvar/<int:nota_id>', methods=['POST'])
def salvar_nota(nota_id):
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, nota_id))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/deletar/<int:nota_id>', methods=['POST'])
@app.route('/deletar/<int:nota_id>', methods=['POST'])
def deletar_nota(nota_id):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notas WHERE id = ?", (nota_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "nota_id": nota_id})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
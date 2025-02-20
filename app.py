from flask import Flask, render_template
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)


@app.route('/')
def index():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',  # Nota que 'passwd' debe ser 'password' en pymysql
        database='db'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students;')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
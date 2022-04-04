import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="shop"
)

cursor = mydb.cursor()

@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        name = request.form.get('name')
        price = int(request.form.get('price'))
        print(name)
        print(price)
        if price and name:
            sql = ('INSERT INTO products (name, price) Values (%s, %s)')

            val = (name, price)

            cursor.execute(sql, val)

            cursor.execute("SELECT * FROM products")
            for item in cursor.fetchall():
                print(item)
    except: pass

    mydb.commit()

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)









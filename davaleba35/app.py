from flask import Flask, render_template, request, redirect, url_for
from model import db, Car

app = Flask(__name__)

HOST = "localhost"
PORT = 5432
DATABASE = "flask_db"
USER = "postgres"
PASSWORD = "nat2nat"

app.secret_key = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    all_data = Car.query.all()
    return render_template('index.html', cars=all_data)


@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car = Car(manufacturer, model, instock, price)

        db.session.add(car)
        db.session.commit()

        return redirect(url_for('index'))


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)

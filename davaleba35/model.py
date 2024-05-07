#Files-ში ატვირთული გაქვთ 3 html ფაილი: base.html, header.html და index.html, დაწერეთ ჩანაწერის განახლების ლოგიკა

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(50))
    model = db.Column(db.String(50))
    instock = db.Column(db.String(5))
    price = db.Column(db.Double)

    def __init__(self, manufacturer, model, instock, price):
        self.manufacturer = manufacturer
        self.model = model
        self.instock = instock
        self.price = price


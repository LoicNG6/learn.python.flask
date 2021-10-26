from Api1 import Car
from waitress import serve
from sqlalchemy.sql.expression import false, within_group
from  flask import Flask, jsonify, request, wrappers

app = Flask(__name__)

@app.route('/api2/car/create', methods=['POST'])
def create_book():
    payload = request.form
    car = Car(payload["brand"], payload["model"], payload["power"])
    
    if (car.isCreated == True) :
        return jsonify (
            status = car.isCreated,
            brand = car.brand,
            model = car.model,
            power = car.power,
        )
    else :
        return jsonify(status = False)
    
if __name__ == '__main__' :
    app.run(debug=True)
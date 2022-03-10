from flask import Flask, jsonify, request


app = Flask(__name__)

buses = [
            { 
            "number_plate": "NAX 123",
            "manufacturer": "Toyata",
            "model": "Hiace",
            "year": "2009",
            "capacity": 18
            },
            {
            "number_plate": "LX Z19",
            "manufacturer": "Ford",
            "model": "FordX",
            "year": "2010",
            "capacity": 45
            },
            {
            "number_plate": "1-MFV-389",
            "manufacturer": "Suzuki",
            "model": "Intruder",
            "year": "2011",
            "capacity": 1
            },
            {
            "number_plate": "1-BEZ-475",
            "manufacturer": "Seat",
            "model": "Ibiza",
            "year": "2010",
            "capacity": 5
            }
        ]

@app.route('/buses')
def get_buses():
    return jsonify(buses)

@app.route('/buses/<int:index>')
def get_bus(index):
    bus = buses[index]
    return jsonify(bus)

@app.route('/buses', methods=['POST'])
def add_bus():
    bus = request.get_json()
    buses.append(bus)
    return bus
    #return {'id': len(buses)}, 200

@app.route('/buses/<int:index>', methods=['PUT'])
def update_bus(index):
    bus_to_update = request.get_json()
    buses[index] = bus_to_update
    return jsonify(buses[index])

@app.route('/buses/<int:index>', methods=['DELETE'])
def delete_bus(index):
    deleted = buses.pop(index)
    return jsonify(deleted), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)
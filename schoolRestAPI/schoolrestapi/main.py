from flask import Flask, jsonify, request

app = Flask(__name__)

opleidingen = {
                1:{"opleiding" : "JUD",
                    "vakken" : [1,2],
                    "studenten" : [1,2]
                    },
                2:{"opleiding": "Full stack",
                    "vakken" : [3,4],
                    "studenten" : [3,4]
                    },
                3:{"opleiding": "Engels",
                "vakken" : [5,6],
                "studenten" : [5,6]
                    }
                }

vakken = {
            1:"python101",
            2:"",
            3:"",
            4:"",
            5:"",
            6:""
        }

studenten = {
                1:"Jens"
}


@app.route('/opleidingen')
def get_opleidingen():
    return jsonify(opleidingen)

@app.route('/opleidingen/int:id>')
def get_opleiding(id):
    opleiding = opleidingen[id]
    return jsonify(opleiding)

@app.route('/opleidingen', methods=['POST'])
def add_opleiding():
    opleiding = request.get_json() #request.get_json(force=True) indien het niet werkt
    opleidingen.append(opleiding)
    return opleiding

@app.route('/opleidingen/<int:id>', methods=['PUT'])
def update_opleiding(id):
    opleiding_to_update = request.get_json()
    opleidingen[id] = opleiding_to_update
    return jsonify(opleidingen[id])

@app.route('/opleidingen/<int:id>', methods=['DELETE'])
def delete_opleiding(id):
    deleted = opleidingen.pop(id)
    return jsonify(deleted), 200

@app.route('/opleidingen/<int:id>/studenten')
def get_studenten_in_opleiding(id):
    pass

@app.route('/opleidingen/<int:id>/vakken')
def get_vakken_in_opleiding(id):
    pass

@app.route('/vakken')
def get_vakken():
    pass

@app.route('/vakken/<int:id>')
def get_vak():
    pass

@app.route('/vakken', methods=['POST'])
def add_vak():
    pass

@app.route('/vakken/<int:id>', methods=['PUT'])
def update_vak():
    pass

@app.route('/vakken/<int:id>', methods=['DELETE'])
def delete_vak():
    pass

@app.route('/vakken/<int:id>/studenten')
def get_studenten_met_vak():
    pass

@app.route('/vakken/<int:id>/opleidingen')
def get_opleidingen_met_vak():
    pass

@app.route('/studenten')
def get_studenten():
    pass

@app.route('/studenten/<int:id>')
def get_student():
    pass

@app.route('/studenten', methods=['POST'])
def add_student():
    pass

@app.route('/studenten/<int:id>', methods=['PUT'])
def update_student():
    pass

@app.route('/studenten/<int:id>', methods=['DELETE'])
def delete_student():
    pass

@app.route('/studenten/<int:id>/resultaten')
def get_resultaten_van_student():
    pass





if __name__ == "__main__":
    app.run(debug=True, port=8080)
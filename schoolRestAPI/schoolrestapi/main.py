from flask import Flask, jsonify, request

app = Flask(__name__)

opleidingen = {
                1:{"opleiding" : "JUD",
                    "vakken" : [1,2],
                    "studenten" : [1,2,6]
                    },
                2:{"opleiding": ".Net",
                    "vakken" : [3,4],
                    "studenten" : [1,3,4,6]
                    },
                3:{"opleiding": "Tolk",
                "vakken" : [5,6],
                "studenten" : [5,6]
                    }
                }

vakken = {
            1:{"naam" : "python101",
                "max" : 30
            },
            2:{"naam" : "Development & troubleshooting",
                "max" : 70
            },
            3:{"naam" : ".Net 101",
                "max" : 40
            },
            4:{"naam" : "C#",
                "max" : 60
            },
            5:{"naam" : "Engels",
                "max" : 80
            },
            6:{"naam" : "Spaans",
                "max" : 20
            }
        }

studenten = {
                1:{"voornaam" : "Jens",
                    "achternaam" : "Coomans",
                    "resultaten" : {
                        1 : 27,
                        2 : 20,
                        3 : 30,
                        4 : 50
                    }
                },
                2:{"voornaam" : "Dario",
                    "achternaam" : "Van Hasselt",
                    "resultaten" : {
                        1 : 21,
                        2 : 17
                    }
                },
                3:{"voornaam" : "Glenn",
                    "achternaam" : "Silkens",
                    "resultaten" : {
                        3 : 40,
                        4 : 50
                    }
                },
                4:{"voornaam" : "Willem",
                    "achternaam" : "Cajot",
                    "resultaten" : {
                        3 : 35,
                        4 : 55
                    }
                },
                5:{"voornaam" : "Seppe",
                    "achternaam" : "Van Gestel",
                    "resultaten" : {
                        5 : 65,
                        6 : 20
                    }
                },
                6:{"voornaam" : "Bert",
                    "achternaam" : "Vriens",
                    "resultaten" : {
                        1 : 30,
                        2 : 70,
                        3 : 40,
                        4 : 60,
                        5 : 80,
                        6 : 20
                    }
                }
}


@app.route('/opleidingen', methods=['GET'])
def get_opleidingen():
    limitedList = []
    limit = request.args.get('limit')
    if limit != None and len(limit) > 0:
        limit = int(limit)
        for i in range(limit):
            limitedList.append(opleidingen[i+1])
        return jsonify(limitedList)
    return jsonify(opleidingen)

@app.route('/opleidingen/<int:id>', methods=['GET'])
def get_opleiding(id):
    if opleidingen.get(id) == None:
        return "page not found", 404
    opleiding = opleidingen[id]
    return jsonify(opleiding)

@app.route('/opleidingen', methods=['POST'])
def add_opleiding():
    opleiding = request.get_json() #request.get_json(force=True) indien het niet werkt
    newId = max(opleidingen) + 1
    opleidingen[newId] = opleiding
    return jsonify(opleidingen[newId])

@app.route('/opleidingen/<int:id>', methods=['PUT'])
def update_opleiding(id):
    if opleidingen.get(id) == None:
        return "page not found", 404
    opleiding_to_update = request.get_json()
    opleidingen[id] = opleiding_to_update
    return jsonify(opleidingen[id])

@app.route('/opleidingen/<int:id>', methods=['DELETE'])
def delete_opleiding(id):
    if opleidingen.get(id) == None:
        return "page not found", 404
    deleted = opleidingen.pop(id)
    return jsonify(deleted)

@app.route('/opleidingen/<int:id>/studenten', methods=['GET'])
def get_studenten_in_opleiding(id):
    if opleidingen.get(id) == None:
        return "page not found", 404
    studentenInOpleiding = []
    for studentId in opleidingen[id]["studenten"]:
        student = studenten[studentId]
        studentenInOpleiding.append((student["voornaam"], student["achternaam"]))
    return jsonify(opleidingen[id]["opleiding"],studentenInOpleiding)

@app.route('/opleidingen/<int:id>/vakken', methods=['GET'])
def get_vakken_in_opleiding(id):
    if opleidingen.get(id) == None:
        return "page not found", 404
    vakkenInOpleiding = []
    for vakId in opleidingen[id]["vakken"]:
        vak = vakken[vakId]
        vakkenInOpleiding.append(vak)
    return jsonify(opleidingen[id]["opleiding"],vakkenInOpleiding)



@app.route('/vakken', methods=['GET'])
def get_vakken():
    return jsonify(vakken)

@app.route('/vakken/<int:id>', methods=['GET'])
def get_vak(id):
    if vakken.get(id) == None:
        return "page not found", 404
    vak = vakken[id]
    return jsonify(vak)

@app.route('/vakken', methods=['POST'])
def add_vak():
    vak = request.get_json()
    newId = max(vakken) + 1
    vakken[newId] = vak
    return jsonify(vakken[newId])

@app.route('/vakken/<int:id>', methods=['PUT'])
def update_vak(id):
    if vakken.get(id) == None:
        return "page not found", 404
    vak_to_update = request.get_json()
    vakken[id] = vak_to_update
    return jsonify(vakken[id])

@app.route('/vakken/<int:id>', methods=['DELETE'])
def delete_vak(id):
    if vakken.get(id) == None:
        return "page not found", 404
    deleted = vakken.pop(id)
    return jsonify(deleted)

@app.route('/vakken/<int:id>/studenten', methods=['GET'])
def get_studenten_met_vak(id):
    if vakken.get(id) == None:
        return "page not found", 404
    studentenVanVak = []
    for opleidingId in opleidingen:
        if id in opleidingen[opleidingId]["vakken"]:
            for studentId in opleidingen[opleidingId]["studenten"]:
                studentenVanVak.append((studenten[studentId]["voornaam"], studenten[studentId]["achternaam"]))
    return jsonify(vakken[id]["naam"],studentenVanVak)

@app.route('/vakken/<int:id>/opleidingen', methods=['GET'])
def get_opleidingen_met_vak(id):
    if vakken.get(id) == None:
        return "page not found", 404
    opleidingenVanVak = []
    for opleidingId in opleidingen:
        if id in opleidingen[opleidingId]["vakken"]:
            opleidingenVanVak.append(opleidingen[opleidingId]["opleiding"])
    return jsonify(vakken[id]["naam"],opleidingenVanVak)



@app.route('/studenten', methods=['GET'])
def get_studenten():
    return jsonify(studenten)

@app.route('/studenten/<int:id>', methods=['GET'])
def get_student(id):
    if studenten.get(id) == None:
        return "page not found", 404
    return jsonify(studenten[id])

@app.route('/studenten', methods=['POST'])
def add_student():
    student = request.get_json()
    newId = max(studenten) + 1
    studenten[newId] = student
    return jsonify(studenten[newId])

@app.route('/studenten/<int:id>', methods=['PUT'])
def update_student(id):
    if studenten.get(id) == None:
        return "page not found", 404
    student_to_update = request.get_json()
    studenten[id] = student_to_update
    return jsonify(studenten[id])

@app.route('/studenten/<int:id>', methods=['DELETE'])
def delete_student(id):
    if studenten.get(id) == None:
        return "page not found", 404
    deleted = studenten.pop(id)
    return jsonify(deleted)

@app.route('/studenten/<int:id>/resultaten', methods=['GET'])
def get_resultaten_van_student(id):
    if studenten.get(id) == None:
        return "page not found", 404
    puntenVanStudent = []
    resultaten = studenten[id]["resultaten"]
    for vakId in resultaten:
        vakNaam = vakken[vakId]["naam"]
        vakMax = vakken[vakId]["max"]
        score = resultaten[vakId]
        puntenVanStudent.append(f"Punten voor {vakNaam}: {score}/{vakMax}.")
    return jsonify(puntenVanStudent)





if __name__ == "__main__":
    app.run(debug=True, port=8080)
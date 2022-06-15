from flask import Flask, jsonify, request

api = Flask(__name__)


@api.route("/")
def Hello():
    return " Hello Frends "


data = [
    {
        'id': 1,
        'Contact': "1234567890",
        'Name': 'Keed',
        'done': False,
    },
    {
        'id': 2,
        'Contact': "7896541230",
        'Name': 'Anime_Stan',
        'done': False,
    },
    {
        'id': 3,
        'Contact': "5803946112",
        'Name': 'Prooo_Krish',
        'done': False,
    },
    {
        'id': 4,
        'Contact': "4836826560",
        'Name': 'Gae',
        'done': False,
    },
    {
        'id': 5,
        'Contact': "1699071292",
        'Name': 'BTSphan',
        'done': False,
    },
    {
        'id': 6,
        'Contact': "3759044145",
        'Name': 'Idiot',
        'done': False,
    },
    {
        'id': 7,
        'Contact': "3137053088",
        'Name': 'Komedy',
        'done': False,
    },
    {
        'id': 8,
        'Contact': "4734910459",
        'Name': 'Exxdee',
        'done': False,
    },
    {
        'id': 9,
        'Contact': "5641246269",
        'Name': 'Lmao',
        'done': False,
    },
    {
        'id': 10,
        'Contact': "8070636788",
        'Name': 'Ded',
        'done': False,
    },
]


@api.route("/add-data", methods=["POST"])
def AddTask():
    if not request.json:
        return jsonify({
            "status": "ERROR",
            "message": "Ok. But what should I add ?"
        }, 400)

    task = {
        'id': data[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json['Contact'],
        'done': request.json[False],
    }

    data.append(task)

    return jsonify({
        "status": "SUCCESS",
        "message": "Task Added!!!"
    })


@api.route("/get-data")
def GetTask():
    return jsonify({
        "data": data
    })


if __name__ == "__main__":
    api.run()

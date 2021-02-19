import flask
from flask import request, jsonify

app = flask.Flask(__name__)
@app.route("/foodscan/<tags>/")
def foodScan(tags):

  foods = {'orange': 'Vitamin C - 53%, Carbohydrates - 12%, Protein - 0.9%',
            'apple' : 'Carbohydrates - 14%, Protein - 0.3%' ,
            'bread' : 'Carbohydrates - 49%, Protein - 9%,' ,
            'cheese' : 'Carbohydrates - 1.3%, Protein = 25%, Fat = 33%,'}

  for food in foods:
    try:
      return jsonify(f"{food}: {foodScan[food]}")
    except:
      pass
app.run()
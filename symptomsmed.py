import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/getremedy/<symptomEntered>")
def giveRemedy(symptomEntered=None):
    sympmeds = {'cough': 'grating ginger and drinking the juice.', 'fever': 'staying in a bath with lukewarm water and rest' ,'sneeze': 'Have citrus fruits like oranges or lemons' , 'cold': 'to drink the juice from carom leaves.'}
    for symptom, remedy in sympmeds.items():
    
        if symptomEntered.lower() == symptom:
            answer = 'You have a ' + symptomEntered + '. You should try ' + remedy
            return jsonify(answer)
        else:
            answer = "We do not have that symptom in ourdatabase. We will try to add more. Or you have spelt the symptom wrong"
            return jsonify(answer)

app.run()

'''symptomEntered = input('Please enter the symptom you are having (eg. cough): ')
sympmeds = {'cough': 'grating ginger and drinking the juice.', 'fever': 'staying in a bath with lukewarm water and rest' ,'sneeze': 'Have citrus fruits like oranges or lemons' , 'cold': 'to drink the juice from carom leaves.' , ''}

for symptom, remedy in sympmeds.items():
    
    if symptomEntered.lower() == symptom:
        print('You have a ' + symptomEntered + '. You should try ' + remedy)
    else:
        print("We do not have that symptom in our database. We will try to add more. Or you have spelt the symptom wrong")'''


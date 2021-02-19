import flask

import smtplib

from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my app</h1>"
    
@app.route("/getvaccine/<age>") #age will be retreived from the database
def vaccine(age=None):
    age = int(age)
    if age == 1:
        #console.log('age=12')
        vaccines = ["Hepatitus A - Costs:Rs.1400 - Due:now - Valid till: 12 months from now."]
        #the input will be in thunkable
        emailRecieve ='akshitagoel2009@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                    
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your first shot of the Chickenpox vaccine are due in 3 months, the third dose of Polio due sometime around now.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
        return jsonify(vaccines)
    
    elif age == 2:
        vaccines = ["Diptheria - 4 shots - Due:now - Valid till:6 months from now (all) - Costs:Rs.800."]
        #"You had to have the second dose of Hepatitus B", months-2, "months ago. It costs 175 rs.")
        #print("You had to have the Diphtheria/DTaP")
         #the input will be in thunkable
        emailRecieve ='akshitagoel2009@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                  
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your four shots of Diptheria are due in 6 months, one shot of HepA is due sometime now and Influenza this year.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
        return jsonify(vaccines) 
    
    elif age == 3:
        vaccines = ["IPV - 3 doses - Due:now - Valid till:12 months from now (all) - Costs:200"]
        #the input will be in thunkable
        emailRecieve ='akshitagoel2009@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                  
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your four shots of Diptheria are due in 6 months, one shot of HepA is due sometime now.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
        return jsonify(vaccines)

    else:
        vaccines = 'Age did not match.'
        return jsonify(vaccines)


@app.route("/getnutri/<age>")
def nutrition(age=None):
    age = int(age)
    if age in range(0, 4):
        content1='Children from ages 0 to 3 need to eat around 33% carbohydrates, 13% protein, 5% fats, 15% dairy, 33%  fruits and veggies per day.'
        return jsonify(content1)
        #ask=input("Type 'y' if you want to know the foods you can use should be eating to help follow these protocals")


    elif age in range(4, 7):
        content2 = 'Children from ages 4 to 6 need to eat around 30% carbohydrates, 20% protein, 10% fats, 20% dairy, 30% fruits and veggies.'
        return jsonify(content2)
        #ask=input("Type 'y' if you want to know the foods you can use should be eating to help follow these protocals")

    elif age in range(7, 11):
        content3 = 'Children from ages 6 to 10 need to eat around 25% carbohydrates, 30% protein, 5% fats, 10% dairy, 30% fruits and veggies.'
        return jsonify(content3)
        #ask=input("Type 'y' if you want  to know the foods you can use should be eating to help follow these protocals")
        

    elif age in range(11, 16) :
        content4 = 'Children from ages 10 to 15 need to eat around 30% carbohydrates, 14% protein, 10% fats, 14% dairy, 20% fruits and veggies.'
        return jsonify(content4)
        #ask=input("Type 'y' if you want to know the foods you can use should be eating to help follow these protocals")
        
        
    elif age in range(16, 1000001):
        content5 = 'The age entered does not fall into our age group of children.'
        return jsonify(content5)

    else:
        content6 = 'Try again.'
        return jsonify(content6)


@app.route('/examplesoffoods/<wants>')
def foods(wants):
  if wants == 'y':
    x=["Carbohydrates - Rice, Chapati, Nuts, Potatoes , Proteins - Lentils, Meat, Egg, Fish", "Fats - Oil, butter", " Dairy - Milk, Curd/Yogurt, Cheese", " Fruits - Apples, Bananas, Lemons/Oranges", "Vegetables - Kale, Cucumber, Spinach"]
    return jsonify(x)
  else:
    y="Have a nice day"
    return jsonify(y)

if __name__ == "__main__":
    app.run()
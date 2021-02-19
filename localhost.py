import flask
import smtplib
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route("/getvaccine/<age>") #age will be retreived from the database
def vaccine(age=None):
    vaccines = ["You had to have the first dose vaccine Hepatitus B. It costs 175 rs."]
    return jsonify(vaccines)
    if age == 12:
        #the input will be in thunkable
        emailRecieve ='dhyan.k.murthy@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                    
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your first shot of the Chickenpox vaccine are due in 3 months, the third dose of Polio due sometime around now.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
    
    elif age == 24:
        vaccines = ["You had to have the first dose vaccine Hepatitus B. It costs 175 rs."]
        return jsonify(vaccines) 
        #"You had to have the second dose of Hepatitus B", months-2, "months ago. It costs 175 rs.")
        #print("You had to have the Diphtheria/DTaP")
         #the input will be in thunkable
        emailRecieve ='dhyan.k.murthy@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                  
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your four shots of Diptheria are due in 6 months, one shot of HepA is due sometime now and Influenza this year.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()

    
    elif age == 32:
        #the input will be in thunkable
        emailRecieve ='akshitagoel2009@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                  
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your four shots of Diptheria are due in 6 months, one shot of HepA is due sometime now.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
    
   
    
app.run()
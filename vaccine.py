import flask
import smtplib
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route("/getvaccine/<age>") #age will be retreived from the database
def vaccine(age):
    age = int(age)
    if age == 12:
        #the input will be in thunkable
        emailRecieve ='akshitagoel2009@gmail.com'
        #emailRecieve will be the retrieved from the databases
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
                    
        s.login("noreply123.InTheZone@gmail.com", "random123!") 
        message = (f"Your first shot of the Chickenpox vaccine are due in 3 months, the third dose of Polio due sometime around now.")
        s.sendmail("noreply123.InTheZone@gmail.com", emailRecieve, message) 
        s.quit()
        vaccines = "You had to have the first dose vaccine Hepatitus A. It costs Rs.175."
        return jsonify(vaccines)
    
    elif age == 24:
        vaccines = "You had to have the first dose vaccine Hepatitus B. It costs Rs.140"

         
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
    
    elif age == 36:
        vaccines = "You had to have the first dose vaccine Diptheria. It costs Rs.300."
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
   
    
app.run()





'''#going to make it connected with the main code
print('Hepatitus B: Rs.175')
print('Diptheria/Tetnus/Pertissus (whooping cough) : Rs.800')
print('Haemophilus Influenza Type B : Rs.2200')
print('IPV (Polio): Rs.700')
print('PCV13 (Pneumococcal Conjucate): Rs.700')
print('RV (Rotavirus - fluid): Rs.1500/Rs.700 (different doses)')
print('MMR (Measles, Mumps, Rubella): Rs.500')
print('Varicells (chickenpox): Rs.1900')
print('Hepatitus A: Rs.1400')
print('HPV (Human papilloma virus): Rs.3200')
print('MCV4 (Meningococcal Conjucate): Rs.')
print('Influenza (seasonal flu): ')

age = int(input('Enter your age: '))
months=age*12
if age in range(0,2) == True:
    print("You had to have the first dose vaccine Hepatitus B" ,age, ". It costs 175 rs.")
    print("You had to have the second dose of Hepatitus B", months-2, "months ago. It costs 175 rs.")
    print("You had to have the Diphtheria/DTaP")


#1st dose	2nd dose (age 1–2 months)	—	3rd dose (age 6–18 months)	—	—	—
#RV	—	1st dose	2nd dose	3rd dose (in some cases)	—	—	—
#DTaP	—	1st dose	2nd dose	3rd dose	—	4th dose	5th dose
#Hib	—	1st dose	2nd dose	3rd dose (in some cases)	Booster dose (age 12–15 months)	—	—
#PCV	—	1st dose	2nd dose	3rd dose	4th dose (age 12–15 months)	—	—
#IPV	—	1st dose	2nd dose	3rd dose (age 6–18 months)	—	—	4th dose
#Influenza	—	—	—	Yearly vaccination (seasonally as appropriate)	Yearly vaccination (seasonally as appropriate)	Yearly vaccination (seasonally as appropriate)	Yearly vaccination (seasonally as appropriate)
#MMR	—	—	—	—	1st dose (age 12–15 months)	—	2nd dose
#Varicella	—	—	—	—	1st dose (age 12–15 months)	—	2nd dose
#HepA	—	—	—	—	2 dose series (age 12–24 months)'''
import random
import pymongo

count = 0
#username
#email
#dob
#userid
client = pymongo.MongoClient("mongodb+srv://akshaj:akshaj@database.uariz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
mydb = client['TisbHax']
acctable= mydb['USers']


if opt == 'signup':
    username=input("Enter your username. must be more than 4 characters and less than 13 characters")
    if len(username)>4 and len(username)<13:
      print('Username is fine!')
    else:
      print('Username does not meet the character limit expectations. Please try again!')

    mo = input('What month were you born in? ')
    ye = input('What year were you born in? ')
    da = input('What day were you born in? ')
    if len(mo)<2:
      mo = '0'+mo
    if len(ye)<4:
      print('Invalid year of birth!')
    if len(da)<2:
      da = '0'+da

    da += '-'
    mo+='-'

    dob = da+mo+ye
    print(dob,"is your birthdate")
    email=input("Enter your gmail.")

    while True:
        userid=random.randint(1000,9999)
        userid = str(userid)

        user_dict = {'_id': userid}

        for x in acctable.find(user_dict):
          if x != {}:
              count+=1
        
        if count == 0:
            final_dict = {'dob': dob, 'email': email, 'username': username}
            final_dict.update(user_dict)
            insert = acctable.insert_one(final_dict)
            print('User succesfully added')
            break
        
elif opt == 'login':
    
    username_input = input('What is your username? ')
    id_input = input('What is your user id? ')
    
    dict_login = {'username': username_input, '_id': id_input}
    
    for x in acctable.find(dict_login):
          if x != {}:
              count+=1
    
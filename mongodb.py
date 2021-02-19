import random
import pymongo
#username
#email
#dob
#userid
client = pymongo.MongoClient("mongodb+srv://akshaj:akshaj@database.uariz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
mydb = client['TisbHax']
acctable= mydb['USers']
print(' d')
print(client)

username=input("Enter your username. must be more than 4 characters and less than 13 characters")
if len(username)>4 and len(username)<13:
  print('Username is fine!')
else:
  print('Username does not meet the character limit expectations. Please try again!')

mo = input('What month were you born in? ')
ye = input('What year were you born in? ')
da = input('What day were you born in? ')
if len(mo)<2:
  mo = '0'+mo + "/"
if len(ye)<4:
  print('Invalid year of birth!')
if len(da)<2:
  da = '0'+da + "-"

dob = da+mo+ye
print(dob,"is your birthdate")
email=input("Enter your gmail.")
userid=random.randint(1000,9999)

for x in acctable.find():
  print(x)
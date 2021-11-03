from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)

    name = infos['name']

    #Open the user .csv file and add new line with user's infos
    with open("users.csv", "a") as users:
        userwriter = csv.writer(users)
        userwriter.writerow([name])
    
    print("User Added !")
    return True
from os import remove
from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"involved",
        "message":"New Expense - Involved People (split each name by a comma): ",
    },
]

def remove_duplicates(array):
    return list(dict.fromkeys(array))

def new_expense(*args):
    infos = prompt(expense_questions)

    amount = infos['amount']
    label = infos['label']
    spender = infos['spender']
    involved = infos['involved']

    #Check if amount is a number or not
    if not amount.isdigit():
        print('Error: "{0}" is not a number!'.format(amount))
        return False

    users = open("users.csv", "r")
    users_list = users.read().lower()

    #Remove every spaces in involved people list and check if they are in user list
    involved = involved.replace(" ", "")
    involved_list = involved.split(',')
    for user in involved_list:
        if not user.lower() in users_list:
            print('Error: User "{0}" Not Found!'.format(user))
            return False
    
    #Check if spender is in user list, add him to involved people and remove duplicated users
    if not spender.lower() in users_list: 
        print('Error: User "{0}" Not Found!'.format(spender))
        return False
    involved_list.append(spender)
    involved_list = remove_duplicates(involved_list)

    #Open the expense .csv file and add new line with expense's infos
    with open("expense_report.csv", "a") as text_file:
        print(f"{amount},{label},{spender},{involved_list}", file=text_file)
        
    print("Expense Added !")
    return True



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

]



def new_expense(*args):
    infos = prompt(expense_questions)

    amount = infos['amount']
    label = infos['label']
    spender = infos['spender']

    if not amount.isdigit():
        print('Error: "{0}" is not a number!'.format(amount))
        return False
  
    file = open("users.csv", "r")
    readfile = file.read()
    
    if spender in readfile: 
        #Open the expense .csv file and add new line with expense's infos
        with open("expense_report.csv", "a") as text_file:
            print(f"{amount},{label},{spender}", file=text_file)
            print("Expense Added !")
            return True
    else: 
        print('Error: User "{0}" Not Found!'.format(spender))
        return False



from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import user_questions,add_user
from status import show_status

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    chosen_option = option['main_options']
    
    if chosen_option == "New Expense":
        new_expense()
    elif chosen_option == "Show Status":
        show_status()
    elif chosen_option == "New User":
        add_user()

    ask_option()

def main():
    ask_option()

main()
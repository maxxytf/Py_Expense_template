import csv
import ast

def show_status():
    #status is a list of (user_that_owes_money, [(spender, money_owed_to_spender), ...])
    status = []

    with open('expense_report.csv', newline='') as expense_report:
        #Skip first line and then read the file
        next(expense_report)
        expenses = csv.reader(expense_report, delimiter=';', quotechar='|')

        for row in expenses:
            spender = row[2]
            involved_list = ast.literal_eval(row[3])
            owed_amount = int(row[0])/len(involved_list)

            for user in involved_list:
                if user == spender:
                    continue
                i = 0
                while i < len(status):
                    element = status[i]
                    if element[0] == user:
                        j = 0
                        while j < len(element[1]):
                            if element[1][j] == spender:
                                element[1][j] += owed_amount
                                break
                            j += 1
                        if j == len(element[1]):
                            element[1].append((spender, owed_amount))
                        break
                    i += 1
                if i == len(status):
                    status.append((user, [(spender, owed_amount)]))
                
        users = open("users.csv", "r")
        users_list = users.read().split()

        for user in users_list:
            str = "{0} owes ".format(user)
            i = 0
            while i < len(status):
                element = status[i]
                involved_user = element[0]
                if involved_user == user:
                    owe_list = element[1]
                    j = 0
                    while j < len(owe_list):
                        owe = owe_list[j]
                        if (j == len(owe_list) - 1):
                            str += "{0}€ to {1}".format(owe[1], owe[0])
                        else:
                            str += "{0}€ to {1},".format(owe[1], owe[0])
                        j += 1
                    print(str)
                    break
                i += 1
            if i == len(status):
                str += "nothing"
                print(str)

    return True
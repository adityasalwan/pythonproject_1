#start_chat fuction starts and its defintion

def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    while(show_menu):
        menu_choices = print("what option do you want to choose ? \n 1. Add status \n 2. Close application \n ")
        result = int(input(menu_choices))

        #validating user's input

        if(result == 1):
            #logic here
            pass
        elif(result == 2):
            show_menu = False
        else :
            print("wrong input of choice.please try again")

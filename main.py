#import statement
from spy_detail import spy_name, spy_salutation, spy_age, spy_rating

print("Let's Get Started")
question = print("Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N) : ")
existing = input(question)
#validating users input
if (existing == "y" or existing == "Y") :
    #logic
    pass
elif (existing == "n" or existing == "N") :
    #new user code
    spy_name = input("Provide your name here : ")
    # check wether some name is input or not
    if len(spy_name) > 0:
        # code if condition is true
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_salutation = input("what should we call you? : ")
        # concatination of spy_name and spy_salutation
        spy_name = (spy_salutation + " " + spy_name)
        print("Welcome " + spy_name + " Glad to have you back with us")
        print("Alright " + spy_name + " i'll like to know little bit more about you ")
    else:
        print("Invalid name")

else :
    print("Wrong choice, Please try again")




def user_name():
    is_exist = False
    while not is_exist:
        choice = input("enter your name ")
        if choice.split():
            is_exist = True
            return choice

def how_many_rounds():
    is_valid = False
    while not is_valid:
        round_choice = input("please chose how many rounds ")
        if not round_choice.isdigit():
            print("its must to be a positive nome ")
            continue 

        round_choice = int(round_choice)
        if round_choice < 1 or round_choice > 10:
            print("number must be between 1-10")
            continue

        is_valid = True
        return round_choice

from all_function import start_game,display_game_history,display_game_statistics
from menu import menu
import input_user
from json_function import save_game,load_game_history,path


def main():
    is_exist = False
    while not is_exist:
        menu()
        user_option = input("please enter option (1-4) ")

        if user_option =="1":
            start_game()
            continue
        if user_option =="2":
            display_game_history(load_game_history(path))
            continue
        if user_option == "3":
            display_game_statistics(load_game_history(path))
            continue
        if user_option =="4":
            print("bye bye")
            break
        print("invalid choice please try again") 

if __name__ == "__main__":
    main()
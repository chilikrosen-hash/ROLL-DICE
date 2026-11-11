import json
path = "./game_history.json"

def load_game_history(path):
    try:
        with open (path,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_game(game):
    try:
        list_ = load_game_history(path)
        list_.append(game)
        with open (path,"w",encoding="utf-8") as file:
            json.dump(list_,file, indent=2)
    except Exception as e:
        print(e)


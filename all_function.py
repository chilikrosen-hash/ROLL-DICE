import random
from input_user import user_name,how_many_rounds
from json_function import save_game,load_game_history,path

def roll_dice():
    return random.randrange(1,7)



def play_round():    
    result_round = {} 
    result_round["round"] = 0
    player = roll_dice()
    computer = roll_dice()
    result_round["player_dice"] = player
    result_round["computer_dice"] = computer
   
    return result_round  
def calculate_winner(player_score,computer_score):
    if player_score > computer_score:
        return "player"
    elif computer_score > player_score:
        return "computer"
    elif computer_score == player_score:
        return "draw"   

def start_game():
    count = 0
    computer_points = 0
    player_points = 0
    game = {
        "player_name":user_name(),
        "rounds": how_many_rounds(),
        "computer_score":0,
        "player_score":0
        ,"winner":None
        ,"results":[]
    }
    for i in range(game["rounds"]):
        count+=1
        rounds = play_round()
        rounds["round"]=count
        if rounds["player_dice"] > rounds["computer_dice"]:  
            rounds["winner"] = game["player_name"]
            player_points+=1
        elif rounds["computer_dice"] > rounds["player_dice"]: 
            rounds["winner"] = "computer"
            computer_points+=1
        if rounds["player_dice"] == rounds["computer_dice"]:
            rounds["winner"] = "nobody"
        game["results"].append(rounds)
    winner = calculate_winner(player_points,computer_points)
    if winner == "player":
        game["winner"] = game["player_name"]
    elif winner == "computer":
        game["winner"] = "computer"
    else:
        game["winner"] = "nobody"
    game["computer_score"] = computer_points
    game["player_score"] = player_points
    display_game_result(game)
    save_game(game)


def display_game_result(game):
    print(f"""
        Player name: {game['player_name']}
        Number of rounds: {game["rounds"]}
        """)
    for res in game["results"]:
        print(f"""
        ---------- ROUND {res["round"]} ----------

        {game["player_name"]}: {res["player_dice"]} 
        computer: {res["computer_dice"]} 
        {res['winner']} wins this round 
        

    """)
    print(f"""
    ================================
              GAME OVER 
    ================================

    {game["player_name"]}: {game["player_score"]}
    computer: {game["computer_score"]}
    
    "WINNER: {game['winner']}

    Game saved successfully
    """)


def display_game_history(history):
    for game in history:
        print(f"""
        Name: {game['player_name']}
        number of rounds: {game['rounds']}
        player result: {game['player_score']}
        computer result: {game['computer_score']}
        winner: {game['winner']}
        """)



def display_game_statistics(history):
    num_of_games = len(history)
    player_win = 0
    computer_win = 0
    draw = 0
    for i in history:
        if i["winner"] != "nobody" and i["winner"] != "computer":
            player_win+=1
        if i["winner"] == "computer":
            computer_win+=1
        if i["winner"] == "nobody":
            draw+=1
    try:
        percent__player = 100/num_of_games * player_win

    except ZeroDivisionError:
        print("dont have games yet")
        return
    print(
    f""" 
    number of games: {num_of_games}
    player wins: {player_win}
    computer wins: {computer_win}
    draw: {draw}
    players percent of win: {percent__player}%
    
    
    """    )







    


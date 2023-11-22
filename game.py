"""
move_data={
    "game_id":<uniq id>
}
"""

import random
import time
def game():
    game_id=time.time()
    while True:
        ask_player_for_move()

data={
    "game_id":""
    "move_id""",
    "symbol":"",
    "duration":,
    "move":"",
    "is_winner":,
}

move_id=1
#10 games
for x in range(10):
    #for each game, let's randomly set the number of moves between 5,9
    num_of_moves=random.randit(5,9)
    game_id=time.time()
    move_id = 0
    for move in range(num_of_moves):
        data={}
        move_id += 1
        duration=random(1,30)
        data['game_id']=game_id
        data['move_id']=move_id
        data['move_start_time']=time.time()
        data['move_end_time']=data['move_start_time']+duration
        data['duration']=duration
        data['move']=random.randit(0,9)
        if move_id == num_of_moves:
            data['is_winner']=True
        else:
            data['is_winner']=False    
        game_data.append(data)        
        

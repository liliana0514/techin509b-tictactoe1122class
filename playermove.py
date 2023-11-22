import time


def dict_to_csv(data):
    """
    Input:
        data -> a dictionary
    Output:
        csv_str -> a valid csv row. i.e. 1,ian,uw
    """
    return ",".join([str(x) for x in data.values()])
  
def write_text(text, filename):
    """
    write the text into a file
    
    Input:
        text -> string
        filename -> The name of the file we want to write
    Output:
        None
    """
    
    # Open a file
    # file open modes: w -> write, r -> read, a -> append
    with open(filename, 'a') as f:
        f.write(text + "\n") #\n -> newline
        

def ask_player_move(symbol):
    """
    Input:
        move -> integer between 0 and 8
    Output:
        True if move success False is move is invalid
    """
    move_data = {}
    # time.time() -> current time in seconds
    move_start_time = time.time()
    move = input("Please enter a move, valid move is between 0 and 8: ")
    move_done_time = time.time()

    move_data['symbol'] = symbol
    move_data['move'] = move
    move_data['duration_seconds'] = move_done_time - move_start_time

    print(move_data)
    ## FIX ME
    csv_str = dict_to_csv()
    write_text(csv_str)

ask_player_move('X')

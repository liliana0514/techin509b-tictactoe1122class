
#symbol,move_count,move,time_spent
#x,1,1,2,60
#o,2,0,1,6

play = [
    {
        "symbol":"x",
        "move_count":1,
        "move":"1,2",
        "time_spent":60,
    },
    {
        "symbol":"o",
        "move_count":2,
        "move":"0,1",
        "time_spent":6
    },
]

def dict_to_csv(data):
    """
        INPUT:
            data -> a dictionary
        OUTPUT:
            csv_str -> a valid csv row. i.e. 1,liliana,uw
    """
    #print(data.values())
    return ",".join([str(x) for x in data.values()])

def write_text(text, filename):
    #file open mode: w-write, r-read, a-append
    with open(filename, "w") as f:
        f.write(text)

csv_str = dict_to_csv({"name":"liliana", "score":"111"})
print(csv_str)
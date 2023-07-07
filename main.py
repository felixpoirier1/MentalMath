import random
import time
import datetime

def main(operation:int=-1, time_allowed:int=60*8, decimals=True):
    starttime = time.time()
    operations = [(lambda x,y : x+y, "+"), (lambda x,y: x-y, "-"), (lambda x,y: x*y, "*"), (lambda x,y: x/y, "/")]
    operations = operations[operation] if operation != -1 else operations
    score = 0
    iterations = 0

    while(time.time() < starttime+time_allowed):
        iterations += 1
        op = operations[random.randint(0, len(operations)-1)]

        if op[1] in ["+", "-"]:
            x = random.randint(-4999, 4999) + (random.randint(0, 99)/100 if decimals else 0)

            y = random.randint(-4999, 4999) + (random.randint(0,99)/100 if decimals else 0)

        elif op[1] == "*":
            x = random.randint(-99, 99) + (random.randint(0, 9)/10 if decimals else 0)
            y = random.randint(-49, 49) + (random.randint(0, 9)/10if decimals else 0)
        
        else:
            y = random.randint(-49, 49)*10
            x = y * random.randint(-10,10)
        
        print(f"{starttime+time_allowed - time.time()} seconds remaining, press 'x' if you want to stop playing")
        print("\t", x, " ", op[1], " ", y, " = ")

        resp = input("\t\t")
        try:
            resp = float(resp) 
            if resp == op[0](x,y):
                score += 1
            else:
                score -= 1
        except:
            if resp == 'x':
                exit()
            score -= 1
    
    resp = {
            "score" : score,
            "questions_asked" : iterations,
            "seconds_elapsed" : time.time() - starttime,
            "date" : datetime.datetime.now()
    }
    
    return resp

if __name__== "__main__":
    print("Welcome to the mental math program, please select your options")
    
    op = input("Which operations? (0= +, 1= -, 2 = *, 3 = /) or press enter if you want all : ")
    
    if op.strip() in ["0", "1", "2", "3"]:
        op = int(op)

    else: op = -1
    
    time_to_play = input("How many minutes? (by default 8 minutes) : ")

    if time_to_play != "":
        time_to_play = float(time_to_play)*60
    else: time_to_play = 8*60

    decimals = input("Do you want decimals? (by default yes) (yes/no) : ")

    if decimals == "no":
        decimals = False
    else: 
        decimals = True

    result = main(op, time_to_play, decimals)
    
    print(result)



 



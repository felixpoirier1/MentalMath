import random
import time
import datetime
import os

def main(operation:int=-1, time_allowed:int=60*8, decimals:bool=True):
    starttime = time.time()
    operations = [(lambda x,y : x+y, "+"), (lambda x,y: x-y, "-"), (lambda x,y: x*y, "*"), (lambda x,y: x/y, "/")]
    operations = [operations[operation]] if operation != -1 else operations
    score = 0
    iterations = 0

    while(time.time() < starttime+time_allowed):
        it_time = time.time()
        iterations += 1
        op = operations[random.randint(0, len(operations)-1)]

        if op[1] == "+" or op[1] == "-":
            x = random.randint(-4999, 4999) + (random.randint(0, 99)/100 if decimals else 0)

            y = random.randint(-4999, 4999) + (random.randint(0,99)/100 if decimals else 0)

        elif op[1] == "*":
            x = random.randint(-9, 9) + (random.randint(0, 9)/10 if decimals else 0)
            y = random.randint(-24, 24)*2 
        
        else:
            y = random.randint(-49, 49)*10
            ans = random.randint(-10,10)
            ans = 1 if ans == 0 else ans
            y = 1 if y == 0 else y
            x = y * ans
    
        print(f"{round(starttime+time_allowed - time.time(),0)} seconds remaining, press 'x' if you want to stop playing")
        print("\t", x, " ", op[1], " ", y, " = ")

        resp = input("\t\t")
        try:
            resp = float(resp) 
            if resp == round(op[0](x,y),2):
                score += 1
                print("\u001b[32mCORRECT\u001b[0m, ANSWERED IN ", round(time.time() - it_time,2), " SECONDS")
            else:
                score -= 1
                print("\u001b[31mWRONG\u001b[0m, CORRECT ANSWER WAS ", round(op[0](x,y), 2))
        except:
            if resp == 'x':
                break
            score -= 1
            print("\u001b[31mWRONG\u001b[0m, CORRECT ANSWER WAS ", round(op[0](x,y), 2))
    
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
        
    ans = input("press 's' to save results into csv file : ")

    if ans == "s":
        if "results.csv" not in os.listdir():
            with open("results.csv", "w") as head:
                head.write("date,score,questions_asked,seconds_elapsed\n")
        with open("results.csv", "a") as res:
            res.write(f"{result['date']},{result['score']},{result['questions_asked']},{result['seconds_elapsed']}\n")
    



 



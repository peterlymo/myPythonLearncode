start = "start"
help = "help"
stop = "stop"
quit = "quit"
isStart = False
isStop = False

engine = ""
while engine.lower() != quit :
    engine = input(">")
    if engine == start:
        if isStart :
            print("car already started")
        else :
            isStart = True
            print("Car started .. Ready to go")
            
    
    elif engine == stop :
        if isStop:
            print("car already stopped")
        
        else :
            isStop =  True
            print("Car Stopped")
            isStart = False
    
    elif engine == help :
         print("""start = to start car
stop = to stop car
help = to get info
quit = to quit game""")

    elif engine == quit :
        break

    else :
        print("cant Understand")
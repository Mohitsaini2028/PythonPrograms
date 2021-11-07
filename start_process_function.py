#First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an p equal to "Yes", it should return "Start Process" Alternatively, elif p is equal to "No", then the function should return "Start Process Aborted". Finally, if start_process gets anything other than those inputs, the function should return "Sorry for the input".

def start_process(p): 
    if p == "Yes":
        print("Start Process")
    elif p == "No":
        print("Start Process Aborted")
    else:
        print("Sorry for the input")
    


start_process("Yes")
start_process("No")
start_process("Anything")

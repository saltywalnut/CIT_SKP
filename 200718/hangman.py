answer = []
input = []

def typeAnswer():
    mode= "typing"
    answer = []
    index = 0
    while mode == "typing":
        letter = input("Type letter: ")
        if answer != '':
            mode = "finished"
        else :
            answer[index] = letter
            index = index + 1
    return answer


answer = typeAnswer()

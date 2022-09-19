def greetings(say_it):
    say_it = say_it.strip().lower()

    if "hello" in say_it:
        print ('$0')
    elif say_it[0] == 'h' :
        print ('$20')
    else :
        print ('$100')

answer = input("Type Greetings and then Enter \n")

greetings(answer)
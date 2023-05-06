msg = '''
start -- start the engine
stop -- stop the engine
quit -- quit the game
help -- show this help message
'''

while True:
    response = input('> ').upper()
    if response == "QUIT":
        break
    elif response == "START":
        print('The Engine has started')
    elif response == "STOP":
        print('The Engine has stopped')
    elif response == "HELP":
        print(msg)
    else:
        print('I did not understand that!')


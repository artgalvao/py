import key_checker
while True:
    try:
        if key_checker.is_pressed('q'):
            print('You Pressed A Key!')
            break 
    except:
        break 
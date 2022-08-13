print('HELLO')
yourname = input('print your name')
secondname = input('print your lastname')
age = input('print your age')
question = input('do you now who are me?')
if question.lower == 'yes':
    print('YOU ARE RUSSIAN SPY')
elif yourname[0] == 'A' or yourname[0] == 'L' or yourname[0] == 'O':
        print('YOU ARE ITALIANO MAFIA')
elif secondname[0] == 'A' or secondname[0] == 'U':
        print('YOU ARE A DOCTOR')
elif int(age) < 18:
            print('YOU ARE CIVILIAN')
else:
        print('I DONT KNOW WHO ARE YOU')


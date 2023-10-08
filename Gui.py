def start_game():
    count = 0
    print('Набирание 5 очков!')
    for i in range(5):
        count += 1
    if count >= 5:
        return True
        print('Победа')
    else:
        return False


print(start_game())

def PasswordsDisplay(x):
    if x == '':
        return False
    else:
        with open(x, "r") as file:
            text = file.read()
            file.close()
        return text

print(PasswordsDisplay('user.txt'))
print(PasswordsDisplay(''))
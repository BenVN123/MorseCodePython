import time
import winsound

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()

def encrypt():
    phrase = input(f"\nPlease enter the phrase you would like to turn to morse code: ")
    print('\nEncrypted morse code (unknown characters as "*"): ')
    
    for char in phrase:
        if char.upper() in morse:
            for i in morse[char.upper()]:
                if i == '-':
                    print('-', flush=True, end='')
                    winsound.Beep(500, 220)
                elif i == ".":
                    print('.', flush=True, end='')
                    winsound.Beep(500, 80)
            print(' ', end='', flush=True)
            sleep(0.2)
        elif char == " ":
            print('/', end=' ', flush=True)
            sleep(0.1)
        else:
            print('*', end=' ', flush=True)

def decrypt():
    key_list = list(morse.keys())
    val_list = list(morse.values())
    phrase = input(f"\nPlease enter the morse code you would like to turn to letters (space inbetween letters, ' / ' inbetween words): ").split(" ")
    output = ""

    for char in phrase:
        if char in val_list:
            output += key_list[val_list.index(char)].lower()
        elif char == "/":
            output += " "
        else:
            print(f"\n'{char}' is not included in our morse chart. Please try again without that character.")
            decrypt()

    print(f"\nDecrypted morse code: {output}")


while True:
    choice = input(f"\n[1] Encrypt to morse code\n[2] Decrypt morse code\n\nEnter the number of the program you want to use: ")

    try:
        if choice == "1":
            encrypt()
            break
        elif choice == "2":
            decrypt()
            break
        else:
            print("\nSomething went wrong, please try again.")
    except Exception:
        print("\nSomething went wrong, please try again.")
from generator.generator import *
from generator.utils import *

def main():
    response = True
    while response:
        passwd = generate_passwd(int(ask_for_passwd_length()))
        if ask_for_save():
            print("La contraseña es: " + passwd)
            save_passwd(passwd)
        else:
            print("La contraseña es: " + passwd)
        response = ask_for_regenerate()
            
    

if __name__ == "__main__":
    main()
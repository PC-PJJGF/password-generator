
def ask_for_passwd_length():
    while True:
        passwd_length = input("De que tamaño quieres que sea la contraseña? (mínimo 8 caracteres): ")

        try:
            if (int)(passwd_length) < 8:
                raise ValueError
            else:
                return passwd_length
        except ValueError:
            print("Por favor, introduce un número de caracteres mínimo de 8.")

def ask_for_save():
    while True:
        save = input("Quieres guardar la contraseña? (s/n): ")

        if save == "s" or save == "S":
            return True
        elif save == "n" or save == "N":
            return False

def save_passwd(passwd):
    try:
        with open("data/passwords.txt", "a") as f:
            f.write(passwd + "\n")
    except Exception as e:
        raise e
    
def ask_for_regenerate():
    while True:
        regenerate = input("Quieres generar otra contraseña? (s/n): ")

        if regenerate == "s" or regenerate == "S":
            return True
        elif regenerate == "n" or regenerate == "N":
            return False
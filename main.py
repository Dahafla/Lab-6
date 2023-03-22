
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def encoder(password): #encoder done by Al Fahad
    encodepass = ""
    for num in password:
        digit = str((int(num) + 3))
        encodepass += digit
    return encodepass

def decoder(password):  # decoder done by JP
    decodedpass = ""
    for num in password:
        digit = str((int(num) - 3))
        decodedpass += digit
    return decodedpass



def main():

    while True:
        menu()
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encoder(password)
            print("Your password has been encoded and stored\n")

        if option == "2":
            decoder_pass = decoder(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoder_pass}\n")

        if option == "3":
            break



if __name__ == "__main__":
    main()

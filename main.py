
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def encoder(password):
    encodepass = ""
    for num in password:
        digit = str((int(num) + 3))
        encodepass += digit
    return encodepass





def main():

    while True:
        menu()
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encoder(password)
            print(encoded_pass)
            print("Your password has been encoded and stored\n")

        if option == "2":
            pass
        if option == "3":
            break



if __name__ == "__main__":
    main()





if __name__ == '__main__':
    main()

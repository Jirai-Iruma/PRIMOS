def NUMBER_RESULT():
    while True:
        try:
            NUMBER = int(input("select a number: "))
            if NUMBER <= 1:
                print(f"{NUMBER} is not a prime")
            for i in range (2,NUMBER):
                if NUMBER % i == 0:
                    print(f"{NUMBER} is not a prime")
                    break
            else:
                    print(f"{NUMBER} is a prime")
            break
        except ValueError:
            print("Invalid Responce")


NUMBER_RESULT()


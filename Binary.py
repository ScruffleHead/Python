while True:
    ten = input("Would you like to turn binary to decimal, or the other way around? Type 0 for binary to decimal and 1 for decimal to binary: ")
    if ten == "1" or ten == "0":
        break
    else:
        print("That's not 1 or 0!")

############################################################

binumbers = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
output = []

if ten == "1":
    while True:
        inpt = input("Input the integer you would like to convert to binary. Nothing above 1,023 please: ")
        try:
            inpt = int(inpt)
        except:
            print("Not an integer.")
            continue
        else:
            inpt = int(inpt)
        if inpt > 0 and inpt <= 1023:
            break
        else:
            print("Must be between 1 and 1,023.")
    for i in range(0, 10):
        if inpt >= binumbers[i]:
            output.append("1")
            inpt = inpt - binumbers[i]
        else:
            output.append("0")
    print("█" * 10)
    print(*output, sep="")
    print("█" * 10)
else:
    while True:
        inpt = input("Input the binary number you'd like to convert to decimal. Nothing above 10 digits please: ")
        if len(inpt) < 1 or len(inpt) > 10:
            print("Either too many digits or none at all; I can't be bothered to figure it out.")
        else:
            break
    inpt = list(inpt)
    output = 0
    for i in range(0, len(inpt)):
        if inpt[i] == "1":
            output = output + binumbers[i + (10 - len(inpt))]
        elif inpt[i] == "0":
            pass
        else:
            print("Input isn't binary.")
            quit()
    print("█" * len(str(output)))
    print(output)
    print("█" * len(str(output)))

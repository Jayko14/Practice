while True:
    x = input('Please type out a sentence ')
    y = x.split(" ")
    z = " ".join(reversed(y))
    print(z)

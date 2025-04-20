MINIMUM_HEIGHT: int = 50  # minimum height required to ride

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Required line to run main
if __name__ == '__main__':
    main()











# MINIMUM_HEIGHT: int = 50  # minimum height required to ride

# def main():
#     height = float(input("How tall are you? "))
#     if height >= MINIMUM_HEIGHT:
#         print("You're tall enough to ride!")
#     else:
#         print("You're not tall enough to ride, but maybe next year!")

# # Required line to run main
# if __name__ == '__main__':
#     main()

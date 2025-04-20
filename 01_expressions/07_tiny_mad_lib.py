SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "  # adjective, noun, verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter and print the result
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This provided line is required at the end of a Python file to call the main() function.
if __name__ == '__main__':
    main()

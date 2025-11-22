import sys


# Read from file
def readFile(filename):
    word_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            w = line.strip()
            word_list.append(w)
    
    return word_list


# Main function
def main():
    # Check if user provided a password as argument
    if len(sys.argv) > 1:
        word_to_test = sys.argv[1]
    else:
        print("Run the program like this:\n\tpython3", sys.argv[0], "<word>")
        sys.exit()
    
    # Read all weak password variants
    weak_passwords = readFile("all_passwords.txt")
    
    # Check if the password exists in the list
    if word_to_test in weak_passwords:
        print(f"❌ WARNING! '{word_to_test}' is NOT a secure password!")
        print("This password is easy to guess. Choose another.")
    else:
        print(f"✓ '{word_to_test}' seems to be an OK password!")
        print("It does not appear in the list of common password variants.")


main()

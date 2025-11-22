# Task 2: Convert to uppercase
def capitalLetter(letter):
    # Dictionary with lowercase → uppercase
    alphabet = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z', 'å': 'Å', 'ä': 'Ä', 'ö': 'Ö'
    }
    
    # If letter exists in dictionary, return uppercase version
    if letter in alphabet:
        return alphabet[letter]
    else:
        return letter


# Task 3: List with one uppercase letter
def uppercaseList(word):
    result = []
    
    # Go through each position in the word
    for i in range(len(word)):
        # Create new word with uppercase letter at position i
        new_word = word[:i] + capitalLetter(word[i]) + word[i+1:]
        result.append(new_word)
    
    return result


# Task 4: List with two uppercase letters
def doubleUppercaseList(word):
    result = []
    
    # Go through all combinations of two positions
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            # Create word with uppercase letters at positions i and j
            new_word = ""
            for k in range(len(word)):
                if k == i or k == j:
                    new_word = new_word + capitalLetter(word[k])
                else:
                    new_word = new_word + word[k]
            result.append(new_word)
    
    return result


# Task 5: Insert special characters
def insertSpecialChars(word):
    result = []
    
    # List of special characters and digits
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
    
    # For each special character
    for ch in chars:
        # Insert at every possible position
        for i in range(len(word) + 1):
            new_word = word[:i] + ch + word[i:]
            result.append(new_word)
    
    return result


# Task 6: Combine all variations
def createMasterList(word):
    result = []
    
    # 1. Add original word
    result.append(word)
    
    # 2. Add special-char variants
    result = result + insertSpecialChars(word)
    
    # 3. Add variants with one uppercase letter
    one_upper = uppercaseList(word)
    result = result + one_upper
    
    # 4. Add variants with one uppercase + special chars
    for variant in one_upper:
        result = result + insertSpecialChars(variant)
    
    # 5. Add variants with two uppercase letters
    two_upper = doubleUppercaseList(word)
    result = result + two_upper
    
    # 6. Add variants with two uppercase + special chars
    for variant in two_upper:
        result = result + insertSpecialChars(variant)
    
    return result


# Task 7: Read from file
def readFile(filename):
    word_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            w = line.strip()
            word_list.append(w)
    
    return word_list


# Task 8: Save to file
def saveToFile(filename, password_list):
    with open(filename, 'w') as file:
        for password in password_list:
            file.write("%s\n" % password)


# Main function
def main():
    # Test task 2
    print("Test task 2:")
    letter_test = capitalLetter('a')
    print(letter_test)
    
    # Test task 3
    print("\nTest task 3:")
    v3 = uppercaseList("admin")
    print(v3)
    
    # Test task 4
    print("\nTest task 4:")
    v4 = doubleUppercaseList("admin")
    print(v4)
    
    # Test task 5
    print("\nTest task 5 (with only 2, 3 and +):")
    v5 = insertSpecialChars("och")
    print(v5)
    
    # Test task 6
    print("\nTest task 6 (with fyra):")
    v6 = createMasterList("fyra")
    v6.sort()
    print(v6)
    
    # Task 7 and 8: Read from file and save all variations
    print("\nCreating password file...")
    words_from_file = readFile("passwords.txt")
    
    all_passwords = []
    for w in words_from_file:
        all_passwords = all_passwords + createMasterList(w)
    
    saveToFile("all_passwords.txt", all_passwords)
    print(f"Done! Total {len(all_passwords)} password variations saved in all_passwords.txt")


main()

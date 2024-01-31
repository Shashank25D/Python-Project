# Define the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Open the file for reading
with open("Answer.txt", "r") as myfile:
    # Initialize the counters
    vcount = 0
    ccount = 0

    # Read the file one character at a time
    ch = myfile.read(1)
    while ch:
        # Ignore spaces, newlines, and other non-alphabetic characters
        if ch.isalpha():
            # Convert to lowercase for easier comparison
            ch = ch.lower()

            # Check if the character is a vowel or a consonant
            if ch in vowels:
                vcount += 1
            else:
                ccount += 1

        # Read the next character
        ch = myfile.read(1)

# Print the results
print("Vowels in the file:", vcount)
print("Consonants in the file:", ccount)
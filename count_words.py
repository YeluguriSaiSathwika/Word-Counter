def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    A word is defined as a sequence of characters separated by spaces.
    This implementation iterates over the string to count words directly.
    """
    count = 0
    in_word = False

    for char in text:
        if char.isspace():
            in_word = False
        elif not in_word:
            count += 1
            in_word = True

    return count

# Prompt the user to enter a sentence or paragraph
user_input = input("Please enter a sentence or paragraph: ")

# Error handling for empty input
if not user_input.strip():
    print("Error: No input provided. Please enter some text.")

# Call the count_words function to get the number of words
word_count = count_words(user_input)

# Display the word count to the user
print(f"The number of words in the entered text is: {word_count}")



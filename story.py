with open("story.txt", "r") as f:
    story = f.read()
# a set is a data structure which will only unique elements
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"


# when you run the loop for i, char in enumerate(story):, it iterates through each character in the story string, and for each character, it assigns the index to i and the character itself to char. This allows you to access both the index and the character of each iteration within the loop.
for i, char in enumerate(story):
    # so we find that angel beacket and we just find the beginning og the word so let's mark that by indicating it to our variable
    if char == target_start:
        start_of_word = i

        # here we just said if we find the ending angel bracket and we have the start of angel bracket
    if char == target_end and start_of_word != -1:
        # so we take that entire word and add that to our words list
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

# here it will creat a dictionary that has all words associated with all of the values
for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
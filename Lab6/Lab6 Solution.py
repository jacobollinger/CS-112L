# Lab6: Design software to calculate continued fractions for a real number and for a rational number.
# By Jacob Bollinger and Keaton Wood

# Constants
VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
SENTENCE_TERMINATORS = ['.', ':', ';', '?', '!']

# Counts the number of words in a file
def countWords (words) :
    count = len(words)
    return count

# Counts the number of syllables in a word
def countSyllables(word) :
    count = 0
    index = 0
    while (index < len(word)) :
        if word[index] in VOWELS and word[index - 1] not in VOWELS :
            index = index + 1
            count = count + 1
        else : 
            index = index + 1
    if index == len(word) and word[index - 1] in VOWELS and word[index - 2] not in VOWELS :
        count = count - 1
    if count == 0 : 
        count = 1
    return count

# Counts the number of sentences in the file
def countSentences(word) :
    count = 0
    if word[len(word) - 1] in SENTENCE_TERMINATORS :
        count = count + 1
    return count

# Reads the file and calls the other functions
def processFile(file) :
    total_words = 0
    total_syllables = 0
    total_sentences = 0
    readscore = 0
    text = open(file)
    for line in text :
        line = line.strip()
        words = line.split()
        total_words = total_words + countWords(words)
        index = 0
        while (index < len(words)) :
            total_syllables = total_syllables + countSyllables(words[index])
            total_sentences = total_sentences + countSentences(words[index])
            index = index + 1
    readscore = readability(total_words, total_syllables, total_sentences)
    # Sets the grade level for each ease score
    if readscore > 90.0 :
        score = '5th grade'
    elif readscore > 80.0 : 
        score = '6th grade'
    elif readscore > 70.0 : 
        score = '7th grade'
    elif readscore > 60.0 : 
        score = '8th & 9th grade'
    elif readscore > 50.0 : 
        score = '10th to 12th grade'
    elif readscore > 30.0 : 
        score = 'college'
    else :
        score = 'college graduate'
    output = ('Flesch reading ease:', readscore, ' Grade level:', score, ' Number of Syllables:', total_syllables, ' Number of Words:', total_words, ' Number of Sentences:', total_sentences)
    return output

# Uses the variables to calculate the readability
def readability(words, syllables, sentences) :
    ease = round(206.835 - 84.6 * syllables / words - 1.015 * words / sentences, 1)
    return ease

# Outputs
print('Name of Text: Of Mice And Men', processFile('/Users/hackerman/Documents/VSCode/CS-112/Lab6/ofmiceandmen.txt'))
print("Name of Text: The Bird's Christmas Carol", processFile('/Users/hackerman/Documents/VSCode/CS-112/Lab6/thebirdschristmascarol.txt'))
print('Name of Text: AN INQUIRY INTO THE NATURE AND CAUSES OF THE WEALTH OF NATIONS', processFile('/Users/hackerman/Documents/VSCode/CS-112/Lab6/smithinquiry.txt'))

## TESTED FILES
# Name of Text: Of Mice And Men
# Flesch reading ease: 89.4
# Grade level: 6th grade
# Size in kilobytes: 160
# Number of Syllables: 37131
# Number of Words: 29731
# Number of Sentences: 2563

# Name of Text: The Bird's Christmas Carol
# Flesch reading ease: 74.6
# Grade level: 7th grade
# Size in kilobytes: 70
# Number of Syllables: 15611
# Number of Words: 11861
# Number of Sentences: 577

# Name of Text: AN INQUIRY INTO THE NATURE AND CAUSES OF THE WEALTH OF NATIONS
# Flesch reading ease: 50.9
# Grade level: 10th to 12th grade
# Size in kilobytes: 3,300
# Number of Syllables: 575512
# Number of Words: 380804
# Number of Sentences: 13756


# We learned how to use lists and how to count the amount of syllables in a text document.
# We learned how to read a file and learned how and why to split the text into word lists.
# We got more practice using if statements, for loops, and while loops.
# We learned how readability is computed and what it is used for.

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        file = f.readlines()
        wordsCount = []
        for sentences in file:
            sentence = sentences.split()
            for words in sentence:
                if words[len(words) - 1] in all_letters:
                    wordsCount.append(words)
                else:
                    nice_letter = words.replace(words[len(words) - 1] , '')
                    wordsCount.append(nice_letter)
    return wordsCount


def count_words():
    my_dict = {}
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    for words in text:
        if words in my_dict:
            my_dict[words] += 1
        else:
            my_dict[words] = 0
            my_dict[words] += 1
            return my_dict

    print(count_words())
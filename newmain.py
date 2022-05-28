# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt") as f:
        filename = f.readline()
        f.close()
        return filename
 
   

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    for word in text:
        split_text = word.split()
    count_words = {}
    for i in split_text():
        if i in count_words():
            count_words[i] += 1
        else:
            count_words[i] = 1
print(count_words())

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    g = open("story.txt", "r")
    Training = g.read()
    g.close()
    return(Training)

kaf = read_file_content('filename')
print(kaf)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    words = text.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
        
            count[word] = 1
    return(count)
print(count_words())    


    #return {"as": 10, "would": 20}
import sys 

#find some text
#attempt creating make chain function. 


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #create an empty dictionary
    dict_of_markov = {} 

    #take input text and put it in a list
    list_of_words = corpus.split()

    #split the string a dictionary of bigrams and their frequency value pair
    #create a for loop to loop over our list of words
    for i in range(len(list_of_words)-2):
        # add the word and the next word to the dictionary as a tuple (for the key)
        #in order to do that, we set the wordth item in the dictionary to that key
        
        #you can set a variable to two things (tuple!!)
        # we want the KEY in the dictionary to be the tuple
        # THEN we want the value to be the next word after the tuple
        key_tuple = (list_of_words[i], list_of_words[i+ 1])

        #if its in the dictionary then add it to the value (list)
        if dict_of_markov.get(key_tuple):
            #then add the word after it to the value list
            dict_of_markov[key_tuple].append(list_of_words[i + 2])
            # set the value to list_of_words[i + 2]
        else:
            #add that shit to the dictionary
        # if not in the dictionary add to the dictionary
            dict_of_markov[key_tuple] = [list_of_words[i + 2]]
        # use the tuple (list[i], list[i + 1]) as a key in the dictionary
        # add the next item in the list [i + 2] as the value (make a list of values)
    #return the dictionary of markov chains we just made with our awesome brains

    return dict_of_markov

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    #unpacking the arguments
    script, filename = sys.argv

    #open a file
    opened_file = open(filename, 'r')

    #read a file
    input_text = opened_file.read()

    #close a file
    opened_file.close()

    chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    print chain_dict

if __name__ == "__main__":
    main()
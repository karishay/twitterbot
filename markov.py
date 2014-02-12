import sys, random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #create an empty dictionary
    dict_of_markov = {} 

    #take input text and put it in a list
    list_of_words = corpus.split()

    #create a for loop to loop over our list of words
    for i in range(len(list_of_words)-3):

         #create a variable that holds the values of adjacent words
        key_tuple = (list_of_words[i], list_of_words[i+ 1], list_of_words[i + 2])

        #if the key_tuple is in the dictionary then:
        if dict_of_markov.get(key_tuple):
            #append the word after the tuple of words to the value pair
            dict_of_markov[key_tuple].append(list_of_words[i + 3])
        else:
            # if the key_tuple is not there, add that shit to the dictionary
            # and set the value equal to the word following the tuple
            dict_of_markov[key_tuple] = [list_of_words[i + 3]]
    #return the dictionary of markov chains we just made with our awesome brains
    return dict_of_markov

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
   
    #find the value of that index in the list, and the item next to it (this is the first random tuple to begin our random sentance)
    tuple_variable = random.choice(chains.keys())

    #returns the matching value (a list of possible third words)
    list_of_third_words = chains.get(tuple_variable)
    
    #generated a random number
    second_rando_number = random.choice(range(len(list_of_third_words)))

    #find the thing at list[random_index]
    third_word = list_of_third_words[second_rando_number]

    # add the two strings together
    sentence = tuple_variable[0] + " " + tuple_variable[1] + " " + tuple_variable[2]+ " " +third_word

    return sentence

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
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
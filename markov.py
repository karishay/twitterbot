import sys 

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #create an empty dictionary
    dict_of_markov = {} 

    #take input text and put it in a list
    list_of_words = corpus.split()

    #create a for loop to loop over our list of words
    for i in range(len(list_of_words)-2):

         #create a variable that holds the values of adjacent words
        key_tuple = (list_of_words[i], list_of_words[i+ 1])

        #if the key_tuple is in the dictionary then:
        if dict_of_markov.get(key_tuple):
            #append the word after the tuple of words to the value pair
            dict_of_markov[key_tuple].append(list_of_words[i + 2])
        else:
            # if the key_tuple is not there, add that shit to the dictionary
            # and set the value equal to the word following the tuple
            dict_of_markov[key_tuple] = [list_of_words[i + 2]]
    #return the dictionary of markov chains we just made with our awesome brains
    return dict_of_markov

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # we need the dictionary we made
    # return a string of random text made from the chains in the dictionary we created
    # make a string of three words
    # try using random.choice
    # maybe use the random number to access a list using their index
        #but we really want the tuple, so that index(the random number) and the one next to it
    
    #make a list
    #generate a random number 
    #find the value of that index in the list, and the item next to it (this is the first random tuple to begin our random sentance)
    #find the matching tuple in the dictionary
    #use the dictionary to find a random third word after the tuple
    #use random choice to generate another random number
    #find the thing at index[random]
    # add the two strings together
    # print that shit, yo


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
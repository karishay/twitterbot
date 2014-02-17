import sys, random, os 
#unpacking the arguments
script, filename = sys.argv

#open a file
opened_file = open(filename, 'r')
#opened_file = open(filename, mode='r', encoding="utf-8")

#read a file
input_text = opened_file.read()

#close a file
opened_file.close()

def make_chains(corpus, chain_size):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #create an empty dictionary
    dict_of_markov = {} 

    #take input text and put it in a list
    list_of_words = corpus.split()

    # create an empty dict
    cleaned_list = []
    # for each item in the range of the length of the list
    for i in range(len(list_of_words)):
        # the word variable will be each item in sequence in the list
        word = list_of_words[i]
        # save the word stripped of quotations to a variable
        stripped_word = word.replace('\xe2', '').replace('\x80', '')
        stripped_word = stripped_word.replace('\x99', "'")
        stripped_word = stripped_word.replace('\x9d', '')
        stripped_word = stripped_word.replace('\x9c', '')
        stripped_word = stripped_word.replace('\xa6', '')        
        stripped_word = stripped_word.strip('"\'')
        cleaned_list.append(stripped_word)
    #god dammit unicode and hex characters!

    #for each item in the cleaned list:
    for i in range(len(cleaned_list) - chain_size):
         
        key = tuple(cleaned_list[i:i+chain_size])
  
        #if the key is in the dictionary then:
        if dict_of_markov.get(key):
            #append the word after the tuple of words to the value pair
            dict_of_markov[key].append(cleaned_list[i + chain_size])
        else:
            # if the key is not there, add that shit to the dictionary
            # and set the value equal to the word following the tuple

            dict_of_markov[key] = [cleaned_list[i + chain_size]]
    #return the dictionary of markov chains we just made with our awesome brains
    return dict_of_markov

print make_chains(input_text, 3)
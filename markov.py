import sys, random, os 
#you took out the twitter module 

def make_chains(corpus, chain_size):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #create an empty dictionary
    dict_of_markov = {} 

    #take input text and put it in a list
    list_of_words = corpus.split()

    for i in range(len(list_of_words) - chain_size):
         
        key = tuple(list_of_words[0:chain_size])
        print key
        #if the key is in the dictionary then:
        #if dict_of_markov.get(key):
            #append the word after the tuple of words to the value pair
        #    dict_of_markov[key].append(list_of_words[i + chain_size])
        #else:
            # if the key is not there, add that shit to the dictionary
            # and set the value equal to the word following the tuple

         #   dict_of_markov[key] = [list_of_words[i + chain_size]]
    #return the dictionary of markov chains we just made with our awesome brains
    return dict_of_markov


def choose_first_tuple(dict_of_markov):
    #randomly generate a tuple from the list
    random_first_tuple = random.choice(dict_of_markov.keys())
    #if the first letter of the first word does not start with a capital
    first_letter = ord(random_first_tuple[0][0]) 
    if first_letter > 91:
        #replace it with another random tuple
        random_first_tuple = random.choice(dict_of_markov.keys())
    #otherwise return that tuple
    else:
        print random_first_tuple

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


    # add a step that resets the tuple to thenew value of the third word and the second tuple item
    #then repeat
    return sentence

#TODO do this shit yo
def add_ending(sentence):
    pass

#mix two authors as a single source
#TODO modify the program to allow any number of words to use as keys
#TODO modify it to start with a capital and end with a punctuation

#create a function that gives twitter access to twit our tweets
def tweet_text(some_text):
    #creating the keys to get into Psalms of Cartman Twitter account:
    twitter_consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    twitter_consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    twitter_token_key = os.environ.get("TWITTER_TOKEN_KEY")
    twitter_token_secret = os.environ.get("TWITTER_TOKEN_SECRET")

    #send the keys to the twitter API so we can actually use it. (I think?)
    api = twitter.Api(consumer_key = twitter_consumer_key , consumer_secret = twitter_consumer_secret, access_token_key = twitter_token_key , access_token_secret = twitter_token_secret )

    #now post our random generate message to twitter!
    status = api.PostUpdate(some_text)
    print status.text

def main():
    #unpacking the arguments
    script, filename = sys.argv

    #open a file
    opened_file = open(filename, 'r')

    #read a file
    input_text = opened_file.read()

    #close a fileic
    opened_file.close()

    #call the functions
    chain_dict = make_chains(input_text, 6)
    choose_first_tuple(chain_dict)
    #random_text = make_text(chain_dict) + " " + make_text(chain_dict)
    #tweet_text(random_text)

if __name__ == "__main__":
    main()




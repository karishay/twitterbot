import sys, random, twitter, os 

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

    #close a file
    opened_file.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict) + " " + make_text(chain_dict)
    tweet_text(random_text)

if __name__ == "__main__":
    main()
import sys, random, os, twitter, auth 
#you took out the twitter module, put it back in later


#This works when isolated and tested
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

#This works when isolated and tested
def choose_first_tuple(dict_of_markov):
    #create a list of keys
    list_of_key = dict_of_markov.keys()
    #create a random number
    rand_num = random.choice(range(len(list_of_key)))
    #look for that random key in the list
    random_first_key = list_of_key[rand_num]
  
    #is that letter capital?
    first_letter = ord(random_first_key[0][0])
    #maybe do a while loop?
    while not first_letter < 91:
        rand_num = random.choice(range(len(list_of_key)))
        random_first_key = list_of_key[rand_num]
        first_letter = ord(random_first_key[0][0])
    else:
        return random_first_key

def make_text(current_tuple, dict_of_markov):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    #make an empty list (this will become the sentence)
    list_sentence = [current_tuple[0]]
    character_count = 0
    rand_num = random.choice(range(len(dict_of_markov.get(current_tuple))))
    #while the sum of characters in the list < 140:
    while character_count < 50:
        # increase the character count by the count of letters in the word 
        sentence = " ".join(list_sentence)
        character_count = len(sentence)
        #add the current tuple to the list
        list_sentence.append(current_tuple[1])
        # create a current tuple that is the second of the previous tuple + a random word from the value
        current_tuple = (current_tuple[1], dict_of_markov.get(current_tuple)[rand_num])
        if ord(current_tuple[1][-1]) == 63 or ord(current_tuple[1][-1]) == 46 or ord(current_tuple[1][-1]) == 33:
            list_sentence.append(current_tuple[1])
            break
        
        
    return " ".join(list_sentence)

#create a function that gives twitter access to twit our tweets
def tweet_text(some_text):
    #creating the keys to get into Psalms of Cartman Twitter account:
    twitter_consumer_key = auth.TWITTER_CONSUMER_KEY
    twitter_consumer_secret = auth.TWITTER_CONSUMER_SECRET
    twitter_token_key = auth.TWITTER_TOKEN_KEY
    twitter_token_secret = auth.TWITTER_TOKEN_SECRET

    #send the keys to the twitter API so we can actually use it. (I think?)
    api = twitter.Api(consumer_key = twitter_consumer_key , consumer_secret = twitter_consumer_secret, access_token_key = twitter_token_key , access_token_secret = twitter_token_secret )

    #now post our random generate message to twitter!
    print some_text
    post_to_twitter = raw_input('Y/N?')

    if post_to_twitter == 'Y' or post_to_twitter =='y':
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
    chain_dict = make_chains(input_text, 2)
    first_tuple = choose_first_tuple(chain_dict)
    sentence = make_text(first_tuple, chain_dict)
    tweet_text(sentence)
    #random_text = make_text(chain_dict) + " " + make_text(chain_dict)

if __name__ == "__main__":
    main()




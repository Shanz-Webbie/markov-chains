"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as the_file:
        text_string = the_file.read()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()


    zipped_words = list(zip(words, words[1:]))


    chains = {}
    

    """iterating over each word in zipped words
        subtract 1 position from zipped words
        bigram variable is a given index of zipped words
        getting the following word by adding one to the previous index
        adding the result to a dictionary of a list
        append to the list one by one"""

    for index in range(len(zipped_words)-1):
        bigram = zipped_words[index]
        following_word = zipped_words[index+1][1]
        if bigram in chains:
            chains[bigram].append(following_word)
        else:
            chains[bigram] = [following_word]

    return chains


def make_text(chains):
    """Return text from chains."""
    
    words = []
    
    link = choice(list(chains.keys()))
    # if link[1].startswith().isupper():
    #     print(link[1].startswith().isupper())



    # link = list(link)
    punctuation = ['!', '#', '$','%','&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@','[',']', '^', '_','`'', '|', '~', '"']
    words.extend(link)
    if not link[1].endswith(punctuation):        
        while chains.get(link):
            # if link[1].isupper():
            #         # print(link[1].isupper()) # returns bool True
            #         link 
            # if link.endswith(punctuation):
            #     break
            try:
                # print(chains[link])
                new_word = (choice(chains[link]))
                print(new_word)
                words.append(new_word)
                link = (link[1], new_word)
                if new_word.endswith(punctuation):
                    break

                
                print(words)
            except:
                print("Out of options!")
                raise ValueError
            else:
                continue       
    return ' '.join(words)


input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)

import sys

OPPURTUNITIES_FILENAME = "oppurtunities.csv"

# extracts and returns a list of keywords from a pdf file
def find_keywords(filename):
    # load list of allowed_keywords
    allowed_keywords = [] # get_allowed_keywords
    # load and read pdf
    # go through every word and check if it is in allowed_keywords list
    # if it is add it to the list of keywords to return
    # example return:
    return ['Artificial Intelligence']

def get_allowed_keywords():
    # read the oppurtunities file get an unique set of all the keywords in all
    # of the rows
    # first part of function code
    pass

if __name__ == "__main__":
    filename = sys.argv[1]
    keywords = find_keywords(filename)
    print(keywords)

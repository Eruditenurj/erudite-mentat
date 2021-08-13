import sys

# extracts and returns a list of keywords from a pdf file
def find_keywords(filename):
    # load list of allowed_keywords
    allowed_keywords = []
    # load and read pdf
    # go through every word and check if it is in allowed_keywords list
    # if it is add it to the list of keywords to return
    # example return:
    return ['Artificial Intelligence']

if __name__ == "__main__":
    filename = sys.argv[1]
    keywords = find_keywords(filename)
    print(keywords)

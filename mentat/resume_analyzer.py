import sys
import csv

OPPURTUNITIES_FILENAME = "oppurtunities.csv"



# extracts and returns a list of keywords from a pdf file
def find_keywords(filename):
   
	list_keywords = []
	
	# load list of allowed_keywords
	allowed_keywords = get_allowed_keywords() # get_allowed_keywords
	
   # load and read pdf
	pdffile = open(filename, 'r')
	
	all_words = pdffile.read()
	
    # go through every word and check if it is in allowed_keywords list
    # if it is add it to the list of keywords to return
	
	for word in all_words:
		for keyword in allowed_keywords:
			if word == keyword:
				list_keywords.append(word)
    # example return:
	return list_keywords

def get_allowed_keywords():
    # read the oppurtunities file get an unique set of all the keywords in all
    # of the rows
	
	unique_keywords = []

	with open ('opportunities.csv') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',',quotechar='"')
		for row in csv_reader:
			count = 0
			temporary_keywords=[row[15]]
			for x in temporary_keywords:
				for y in unique_keywords:
					if x == y:
						continue
				unique_keywords.append(x)
			count = count + 1
		
	return unique_keywords

if __name__ == "__main__":
    filename = sys.argv[1]
    keywords = find_keywords(filename)
    print(keywords)

import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("/Users/nikhiljain/Documents/GitHub/erudite-mentat/mentat/opportunities.csv")
print(df)


# calculates which opportunities most aligns with the given keywords
# returns a list of opportunities
keywords = ['Chemistry', 'Biochemistry', 'Industry', 'Industrial Career', 'Organic', 'Inorganic', 'Analytical', 'Computational', 'Physical']
def get_recommended_opportunities(keywords):
    # example return:
    return [
        {
            "institution": "Brigham Young University",
            "site_name": "REU Site: Physics Research at Brigham Young University",
            "site_url": "http://reu.byu.edu/home",
            "contact_name": "Jean-Francois van Huele",
            "contact_email": "reu@byu.edu",
            "keywords": ["astronomy","astrophsyics"]
        },
        {
            "institution": "Brigham Young University",
            "site_name": "REU Site: Physics Research at Brigham Young University",
            "site_url": "http://reu.byu.edu/home",
            "contact_name": "Jean-Francois van Huele",
            "contact_email": "reu@byu.edu",
            "keywords": ["astronomy","astrophsyics"]
        }
    ]

if __name__ == "__main__":
    #keywords = sys.argv[1:]
    keywords = ['Chemistry', 'Biochemistry', 'Industry', 'Industrial Career', 'Organic', 'Inorganic', 'Analytical', 'Computational', 'Physical']
    oppurtunities = get_recommended_opportunities(keywords)
    print(oppurtunities)

import sys

# calculates which opportunities most aligns with the given keywords
# returns a list of opportunities
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
    keywords = sys.argv[1:]
    oppurtunities = get_recommended_opportunities(keywords)
    print(oppurtunities)

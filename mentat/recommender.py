import sys
import resume_analyzer

# calculates which opportunities most aligns with the given keywords
# returns a list of opportunities
def get_recommended_opportunities(keywords):
    allowed_keywords = resume_analyzer.get_allowed_keywords()
    # make count-vectorizer for resume

    # make count-vectorizer for all opportunites
    # opportunities = resume_analyzer.get_opportunities()
    
    # compute cosine similarity between resume and opportunities

    # return the 5 opportunities with the most cosine similarity

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
    opportunities = get_recommended_opportunities(keywords)
    print(opportunities)

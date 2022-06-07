from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer 
ps = PorterStemmer()

def clean_text(uncleaned):
    '''
    Cleans text in several steps. 1) Removes punctuation and common (stop) words. 2) Takes the stem of the word.

    Parameters
    ----------
    uncleaned : str
        Text to be cleaned.

    Returns
    -------
    cleaned : list
        List of words after cleaning
    '''
    
    try:
        stopwds = set(stopwords.words('english') + list(string.punctuation))
        uncleaned_2 = [i for i in word_tokenize(uncleaned.lower()) if i not in stopwds] # make lower and remove stopwords
        cleaned = []
        for word in uncleaned_2:
            if len(word) == 1:                  # Remove single characters such as '-'
                continue
            if "'" in [word[0], word[-1]]:      # remove things like 's as they're words of their own
                continue
            else:
                cleaned.append(ps.stem(word))   # stem the words
        cleaned = list(dict.fromkeys(cleaned)) # remove duplicated
        return cleaned
    except:
        print(f"A string was axcpected but a {type(uncleaned)} was given")


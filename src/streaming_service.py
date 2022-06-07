from show import Show
from inv_index import InvertedIndex
from cleaner import clean_text
from collections import Counter
from itertools import repeat, chain
from collections import OrderedDict

class StreamingService:
    '''
    StreamingService represents streaming service that stores and provides different TV and movie shows
    '''
    
    def __init__(self, name, show_data):
        '''
        Parameters
        ----------
        name : str
            name of the streaming service
        show_data : pandas DataFrame
            each row contains the information about title, type, year added, rating, duration, description
            assume show title is unique

        Returns
        -------
        None.
        '''
        self._name = name
        self._shows = {}
        self._identities = {}
        self._inv_index = InvertedIndex()
        for _, row in show_data.iterrows():
            self.add_show(*row)


    def get_name(self):
        '''
        return the name (string)
        '''
        return self._name

    def get_all_shows(self):
        '''
        return a generator for the shows

        Yields
        ------
        show : Show
            Show available from the streaming service
            
        '''
        shows = []
        for show in self._shows.values():
            shows.append(show)
        return shows

    def add_show(self, title, director, cast, country, show_type, year_added, rating, duration, genre, description):
        '''
        add a show to the streaming service. Assume show title is unique

        Parameters
        ----------
        title : str
            title of the show
        show_type : str
            whether the show is a TV show or a movie
        year_added : int
            the year added to the streaming service
        rating : str
            parental guidelines rating
        duration : str
            length of the movie or the TV show
        description : str
            description of the show

        Returns
        -------
        None.

        '''
        self._shows[title] = Show(title, director, cast, country, show_type, year_added, rating, duration, genre, description)
        self._inv_index.add_text(title, len(self._identities))
        self._inv_index.add_text(str(director), len(self._identities)) 
        self._inv_index.add_text(str(cast), len(self._identities))
        self._inv_index.add_text(str(country), len(self._identities))
        self._inv_index.add_text(show_type, len(self._identities))
        self._inv_index.add_numeric(year_added, len(self._identities))
        self._inv_index.add_text(str(rating), len(self._identities))
        self._inv_index.add_text(duration, len(self._identities))
        self._inv_index.add_text(str(genre), len(self._identities))
        self._inv_index.add_text(description, len(self._identities))
        self._identities[len(self._identities)] = self._shows[title]
        

    def get_show(self, show_title):
        '''
        Get a show given the title of the show

        Parameters
        ----------
        show_title : str
            title of the show to get. It needs to match perfectly (including case, spacing, etc)

        Raises
        ------
        KeyError
            if the corresponding show is not available from the streaming service

        Returns
        -------
        Show
            the show with the given title

        '''
        try:
            return self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not available from {self.get_name()}.")

    def remove_show(self, show_title):
        '''
        remove a show from the streaming service given the title of the show

        Parameters
        ----------
        show_title : string
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Raises
        ------
        KeyError
            if the corresponding show is not available from the streaming service

        Returns
        -------
        None.
        '''
        try:
            del self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not available from {self.get_name()}.")
            
    def find_show(self, id_given):
        ''' 
        Given an id index, it returns the corresponding show
        '''
        return self._identities[id_given]
            
    def search(self, term, unsure = False):
        '''
        searches for shows with matching key words
        
        Parameters
        ----------
        term : str
            The string to search for.
        unsure : bool, optional
            Broadens the search range to shows with any matching words, ordering the shows by word matches. The default is False.

        Returns
        -------
        matching_shows: list
            The shows that match the search term
        '''
        matching_shows = []
        words_and_results = []
        terms = clean_text(term)
        for word in terms:
            try:
                show_id = self._inv_index.return_index()[word]
                words_and_results.append(show_id)
            except:
                print(f"Excluding '{word}' from the search as no matches were found")
                pass
            
        if len(words_and_results) == 0:
            raise ValueError("None of the search phrase matches a show")
            
        if unsure == True:
            for word in words_and_results:
                for idenitiy in word:
                    matching_shows.append(self._identities[idenitiy])
            matching_shows = list(chain.from_iterable(repeat(i, c) for i,c in Counter(matching_shows).most_common())) # orders them by number of occurences
            matching_shows = OrderedDict.fromkeys(matching_shows)
            matching_shows = list(matching_shows)
      
        if unsure == False:
            common_values = set(words_and_results[0]).intersection(*words_and_results) # Finds the common value in the lists of lists (words that match all the input) without letting duplicates in twice (which occurs if a common word is in two places likee description and title. 
            for value in common_values:
                matching_shows.append(self._identities[value])
                
        return matching_shows      
            
    def get_inv_index(self):
        ''' 
        returns the inverted index
        '''
        return self._inv_index.dic()
            
    
        

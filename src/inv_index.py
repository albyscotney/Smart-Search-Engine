from cleaner import clean_text

class InvertedIndex:
    
    '''
    Creates an inveerted index
    '''
    
    
    def __init__(self):
        '''
        Makes an empty inverted index

        Returns
        -------
        None.

        '''
        self._inv_index = {}
        
    def add_numeric(self, value, identity):
        '''
        Add numeric values to the inverted index as strings
        
        Parameters
        ----------
        value : int
            value to add to index.
        identity : int
            The index value of the show.

        Returns
        -------
        None.

        '''
        
        if str(value) in self._inv_index:
            self._inv_index[str(value)].append(identity)
        else:
            self._inv_index[str(value)] = [identity]
                
    def add_text(self, text, identity):
        '''
        Add text to the inverted index

        Parameters
        ----------
        text : str
            Text to add to the index.
        identity : int
            The index value of the show.

        Returns
        -------
        None.

        '''
        cleaned = clean_text(text)
        for word in cleaned:
            if word in self._inv_index:
                self._inv_index[word].append(identity)
            else:
                self._inv_index[word] = [identity]

            
    def return_index(self):
        '''
        Returns the inverted indeex
        '''
        
        return self._inv_index
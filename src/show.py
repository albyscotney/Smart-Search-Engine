
class Show:
    '''
    Show represents a TV show / movie by storing and providing different information about the corresponding show
    '''
    _id_counter = 0
    def __init__(self, title, director, cast, country, show_type, year_added, rating, duration, genre, description):
        '''
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
        self._title = title
        self._director = director
        self._cast = cast
        self._country = country
        self._show_type = show_type
        self._year_added = year_added
        self._rating = rating
        self._duration = duration
        self._genre = genre
        self._description = description
        self._id = Show._id_counter
        Show._id_counter += 1

    def get_id(self):
        '''
        return the unique id of the show (int)
        '''
        return self._id

    def get_title(self):
        '''
        return the title of the show (string)
        '''
        return self._title

    def get_show_type(self):
        '''
        return the show type like TV show or Movie (string)
        '''
        return self._show_type

    def get_year_added(self):
        '''
        return the year the show is added (int)
        '''
        return self._year_added

    def get_rating(self):
        '''
        return the parental guidelines rating (string)
        '''
        return self._rating

    def get_duration(self):
        '''
        return the duration description (string)
        '''
        return self._duration

    def get_description(self):
        '''
        return the description of the show (string)
        '''
        return self._description

    def __str__(self):
        return f"{self.get_title()} ({self.get_show_type()})"

    def __repr__(self):
        return str(self)
    
    

import datetime
from favouriteplaylist import FavouritePlaylist
from dateutil.relativedelta import relativedelta

class User:
    '''
    Represents a user of a streaming_service
    '''

    def __init__(self, birth_day, birth_month, birth_year):
        '''

        Parameters
        ----------
        birth_day : int
            The day of birth.
        birth_month : int
            The month of birth.
        birth_year : int
            The year of birth.

        Returns
        -------
        None.

        '''
        
        self._birthday = datetime.datetime(birth_year, birth_month ,birth_day)
        self._history = {}
        self._watch_later = {}
        self._favourites = FavouritePlaylist('Favourites', 100)
        
    def watch_later(self, show):
        '''
        add a show to a users watch later playlist
        
        Parameters
        ----------
        show : Show
            The show to add to the watch later playlist.

        Returns
        -------
        None.

        '''
       
        self._watch_later[show.get_title()] = show
        
    def dont_watch_later(self, show_title):
        '''
        removes a show from a users watch later playlist
        Parameters
        ----------
        show_title : str
            Title of the show to be removed.

        Returns
        -------
        None.

        '''
        try:
            del self._watch_later[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")
        
    def play_watch_later(self, show_title = None):
        '''
        Play a show from the users watch later playlist
        
        Parameters
        ----------
        show_title : Show, optional
            The show to play from the watch later playlist. The default is None.

        Returns
        -------
        show_played : Show
            The show that was played.

        '''
        
        if show_title is None:
            try:
                show_title = list(self._watch_later)[0] # first show name in the playlist
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._watch_later[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")
        
        try:
            self._history[show.get_title()] = show    
            show_played = self._watch_later[show_title]
            del self._watch_later[show_title]
            play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
            print(play_str)
        except:
            raise IndexError("Show not in playlist")
        return show_played

    def favourite(self, show):
        '''
        
        Parameters
        ----------
        show : Show
            The show to add to favourites.

        Returns
        -------
        None.

        '''
       
        self._favourites.add_show(show)
        
    def unfavourite(self, show_title):
        '''
    

        Parameters
        ----------
        show_title : str
            The title of the show to remove.

        Returns
        -------
        None.

        '''
        try:
            self._favourites.remove_show(show_title)
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")
        
    def play_favourite(self, show_title = None):
        '''
        Plays a selected or random show from the users favourite playlist.

        Parameters
        ----------
        show_title : str, optional
            The title of the show to play. The default is None.

        Returns
        -------
        show : Show
            The show that was played.

        '''
        try: 
            show = self._favourites.play_show(show_title)
            if show_title == None: 
                show_title = show.get_title()        
            self._history[show_title] = show
            if show_title in self._watch_later:
               del self._watch_later[show_title]             
            return show
        except IndexError:
            raise IndexError("There are no shows to play")
    
    def get_favourites(self):
        '''
        Returns a list of the users favourite shows
        '''
        return self._favourites._shows
    
    def get_watch_later(self):
        '''
        Returns a dictionary of the users watch later playlist 
        '''        
        return self._watch_later
    def get_history(self):
        '''
        Returns the users previously played shows
        '''
        return self._history
    
    def clear_history(self):
        '''
        Clears the users watch history
        '''
        self._history = {}
        print("Your history has been cleared")
        return
    
    def get_age(self):
        '''
        Returns the age of the user
        '''
        now = datetime.datetime.now()
        age = relativedelta(now, self._birthday)
        return age.years

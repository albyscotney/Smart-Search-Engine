import random

class CapacityError(Exception):
    '''
    error to raise when the playlist is full
    '''
    pass

class Playlist:
    '''
    Playlist represents a playlist like "watch later" or "favorite" for which it stores different TV and movie shows
    '''
    def __init__(self, name, capacity):
        '''
        Parameters
        ----------
        name : str
            name of the playlist
        capacity : positive int
            maximum number of shows can be stored in the playlist

        Raises
        ------
        TypeError
            when the given capacity is not int
        ValueError
            when the given capacity is not positive

        Returns
        -------
        None.

        '''
        if not isinstance(capacity, int):
            raise TypeError(f"Capacity needs to be an integer, but {type(capacity)} is given.")
        if capacity <= 0:
            raise ValueError(f"Capacity of the playlist is expected to be a positive integer, but {capacity} is given.")
        self._name = name
        self._capacity = capacity
        self._shows = {}

    def get_name(self):
        '''
        return the name of the playlist (string)
        '''
        return self._name

    def add_show(self, show):
        '''
        add a show to the playlist

        Parameters
        ----------
        show : Show
            show to add to the playlist

        Raises
        ------
        CapacityError
            if the playlist is already full

        Returns
        -------
        None.

        '''
        if len(self._shows) < self._capacity:
            self._shows[show.get_title()] = show
        else:
            raise CapacityError(f"The playlist {self.get_name()} is full.")

    def remove_show(self, show_title):
        '''
        Remove a show corresponding to the given show_title

        Parameters
        ----------
        show_title : str
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Raises
        ------
        KeyError
            if the corresponding show is not available from the playlist

        Returns
        -------
        None.
        '''

        try:
            del self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")

    def play_show(self, show_title = None):
        '''
        "play" a show with a given title in the playlist by printing and returning a string describing 1. which show was played and 2. the duration of the show. If show_title is not given, the show that has been added to the playlist first will be play

        Parameters
        ----------
        show_title : str, optional
            Show to play. It has to match the title perfectly (including case, spacing, etc)
            The default is None and the first show added to the playlist will be played.

        Raises
        ------
        IndexError
            when the playlist is empty
        KeyError
            when the given show is not in the playlist

        Returns
        -------
        play_str : str
            description about what show was played and the duration of the show

        '''
        if show_title is None:
            try:
                show_title = list(self._shows)[0] # first show name in the playlist
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")
            
        show_played = self._shows[show_title]
        del self._shows[show_title]
        play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
        print(play_str)
        return show_played

    def shuffle_play(self):
        '''
        "play" a random show in the playlist by printing and returning a string describing what show was played and the duration of the show

        Raises
        ------
        IndexError
            when the playlist is empty

        Returns
        -------
        string
            description about what show was played and the duration of the show

        '''
        try:
            show_title = random.choice(list(self._shows.keys())) # get a random show title
            return self.play_show(show_title)
        except IndexError:
            raise IndexError("No show is in the playlist.")

    def __len__(self):
        '''
        return the number of shows in the playlist
        '''
        return len(self._shows)
    


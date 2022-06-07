import playlist
from random import randint

class FavouritePlaylist(playlist.Playlist):
    '''
    FavouritePlaylist is a child class of Playlist, if a show is played it is not removed from the list.
    '''
    
    def __init__(self, name, capacity):
        '''
        Parameters
        ----------
        name : str
            The name of the playlist.
        capacity : int
            The capacity of the playlist.

        Returns
        -------
        None.

        '''
        playlist.Playlist.__init__(self, name, capacity)
        
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
        self._shows[show_title] : Show
            The instance of show that was played.

        '''
        if show_title is None:
            try:
                show_title = list(self._shows)[randint(0, len(self._shows)-1)] # Chooses a random show
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")
        
        play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
        print(play_str)
        return self._shows[show_title]
    
        
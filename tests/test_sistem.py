import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))
import pytest
from sistem import SongNode, ArtistNode, AlbumNode

def test_song_and_artist_nodes():
    artist = ArtistNode("Coldplay")
    assert artist.artist_name == "Coldplay"
    
    artist.add_song(1, "Yellow", "4:29", genre="Alternative Rock")
    assert artist.songs_head is not None
    assert artist.songs_head.title == "Yellow"
    assert artist.songs_head.duration == "4:29"

import unittest
import pandas as pd
from src.music_filter import filter_music

class TestMusicFilter(unittest.TestCase):

    def setUp(self):
        data = {
            'track_artist': ['Artist1', 'Artist2'],
            'track_album_name': ['Album1', 'Album2'],
            'playlist_genre': ['Pop', 'Rock'],
            'playlist_subgenre': ['Synthpop', 'Alternative Rock'],
            'emotion': ['Happy', 'Sad'],
            'decade': ["2010's", "2000's"]
        }
        self.df = pd.DataFrame(data)

    def test_filter_music_by_genre(self):
        result = filter_music(self.df, genres=['Pop'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['track_artist'], 'Artist1')
        
if __name__ == '__main__':
    unittest.main()

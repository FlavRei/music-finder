import pandas as pd
from src.data_preprocessing import load_data, clean_data

def test_load_data():
    df = load_data("data/raw/musics.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_clean_data():
    raw_data = {
        'track_name': ['song1', 'song2', None],
        'track_artist': ['artist1', 'artist2', 'artist3'],
        'track_album_name': ['album1', 'album2', 'album3'],
        'track_album_release_date': ['2019-01-01', '2020-02-02', '2021-03-03'],
        'track_popularity': [50, 60, 70],
        'playlist_name': ['playlist1', 'playlist2', 'playlist3'],
        'playlist_genre': ['genre1', 'genre2', 'genre3'],
        'playlist_subgenre': ['subgenre1', 'subgenre2', 'subgenre3'],
        'track_id': ['id1', 'id2', 'id3'],
        'tempo': [120, 130, 0]
    }
    df = pd.DataFrame(raw_data)
    df = clean_data(df)
    
    assert 'track_popularity' not in df.columns
    assert 'playlist_name' not in df.columns
    assert df.shape[0] == 2 
    assert df['track_album_release_year'].dtype == int
    assert df['playlist_genre'].str.istitle().all()
    assert df['playlist_subgenre'].str.istitle().all()
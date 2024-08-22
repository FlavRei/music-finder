import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df.drop(columns=['track_popularity', 'playlist_name'])
    df = df.dropna(subset=['track_name', 'track_artist', 'track_album_name'])
    df['track_album_release_year'] = pd.to_datetime(df['track_album_release_date'], errors='coerce').dt.year.fillna(0).astype(int)
    df = df.drop(columns=['track_album_release_date'])
    df = df[df['track_album_release_year'] != 0]
    df = df[df['tempo'] != 0]
    df = df.drop_duplicates(subset=['track_id'])
    return df

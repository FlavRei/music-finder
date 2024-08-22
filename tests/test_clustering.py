import pandas as pd
from src.clustering import perform_clustering, assign_emotion_labels

def test_perform_clustering():
    raw_data = {
        'danceability': [0.5, 0.7, 0.9, 0.4, 0.6],
        'energy': [0.6, 0.8, 0.5, 0.7, 0.9],
        'loudness': [-5, -7, -6, -5.5, -6.5],
        'acousticness': [0.1, 0.3, 0.2, 0.15, 0.25],
        'instrumentalness': [0.05, 0.07, 0.06, 0.04, 0.05],
        'valence': [0.2, 0.4, 0.3, 0.25, 0.35],
        'tempo': [120, 130, 125, 135, 140]
    }
    df = pd.DataFrame(raw_data)
    features = ['danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness', 'valence', 'tempo']
    
    df, kmeans = perform_clustering(df, features)
    
    assert 'emotion' in df.columns
    assert len(df['emotion'].unique()) <= 5

def test_assign_emotion_labels():
    raw_data = {'emotion': [0, 1, 2, 3, 4]}
    df = pd.DataFrame(raw_data)
    emotion_labels = {
        0: 'Happy',
        1: 'Sad',
        2: 'Epic',
        3: 'Chill',
        4: 'Exciting'
    }
    df = assign_emotion_labels(df, emotion_labels)
    
    expected_emotions = ['Happy', 'Sad', 'Epic', 'Chill', 'Exciting']
    assert df['emotion'].tolist() == expected_emotions

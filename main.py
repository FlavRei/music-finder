from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import scale_features, add_decade_column
from src.clustering import perform_clustering, assign_emotion_labels

def main():
    filepath = "data/raw/musics.csv"
    
    df = load_data(filepath)
    df = clean_data(df)
    
    features = ['danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness', 'valence', 'tempo']
    df = scale_features(df, features)
    df = add_decade_column(df)
    
    df, kmeans = perform_clustering(df, features)
    emotion_labels = {
        0: 'Happy',
        1: 'Sad',
        2: 'Epic',
        3: 'Chill',
        4: 'Exciting'
    }
    df = assign_emotion_labels(df, emotion_labels)
    
    df.to_csv('data/processed/musics.csv', index=False)

if __name__ == "__main__":
    main()

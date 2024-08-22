from sklearn.cluster import KMeans

def perform_clustering(df, features, n_clusters=5, random_state=42):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df['emotion'] = kmeans.fit_predict(df[features])
    return df, kmeans

def assign_emotion_labels(df, emotion_labels):
    df['emotion'] = df['emotion'].replace(emotion_labels)
    return df

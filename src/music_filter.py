def filter_music(df, artist=None, album=None, genres=None, subgenres=None, emotions=None, decades=None):
    """
    Filters music based on specified criteria.
    
    Args:
        df (pd.DataFrame): The music dataset.
        genres (list, optional): List of genres to include.
        subgenres (list, optional): List of subgenres to include.
        emotions (list, optional): List of emotions to include.
        decades (list, optional): List of decades to include.
    
    Returns:
        pd.DataFrame: A DataFrame filtered according to the criteria.
    """
    if artist:
        df = df[df['track_artist'].isin(artist)]

    if album:
        df = df[df['track_album_name'].isin(album)]

    if genres:
        df = df[df['playlist_genre'].isin(genres)]
    
    if subgenres:
        df = df[df['playlist_subgenre'].isin(subgenres)]    

    if emotions:
        df = df[df['emotion'].isin(emotions)]
    
    if decades:
        df = df[df['decade'].isin(decades)]
    
    return df
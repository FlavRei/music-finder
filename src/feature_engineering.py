from sklearn.preprocessing import StandardScaler

def scale_features(df, features):
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df

def assign_decade(year):
    if year < 1960:
        return "1950's"
    elif year >= 1960 and year < 1970:
        return "1960's"
    elif year >= 1970 and year < 1980:
        return "1970's"
    elif year >= 1980 and year < 1990:
        return "1980's"
    elif year >= 1990 and year < 2000:
        return "1990's"
    elif year >= 2000 and year < 2010:
        return "2000's"
    elif year >= 2010 and year < 2020:
        return "2010's"
    else:
        return "2020's"

def add_decade_column(df):
    df['decade'] = df['track_album_release_year'].apply(assign_decade)
    return df

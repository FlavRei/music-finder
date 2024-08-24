import streamlit as st
from src.data_preprocessing import load_data
from src.music_filter import filter_music

df = load_data('data/processed/musics.csv')

def get_sorted_options(column):
    return sorted(df[column].unique())

def filter_by_genres_and_subgenres(df, genres, subgenres):
    if genres:
        return df[df['playlist_genre'].isin(genres) | df['playlist_subgenre'].isin(subgenres)]
    return df

def get_available_subgenres(df, genres):
    if genres:
        return sorted(df[df['playlist_genre'].isin(genres)]['playlist_subgenre'].unique())
    return []

def get_available_albums(df, artists):
    if artists:
        return sorted(df[df['track_artist'].isin(artists)]['track_album_name'].unique())
    return sorted(df['track_album_name'].unique())

def main():
    st.title("Music Finder")
    st.sidebar.header("Choose your criteria")

    selected_genres = st.sidebar.multiselect("Select genres", options=get_sorted_options('playlist_genre'))
    
    available_subgenres = get_available_subgenres(df, selected_genres)
    selected_subgenres = st.sidebar.multiselect("Select subgenres", options=available_subgenres)

    filtered_df = filter_by_genres_and_subgenres(df, selected_genres, selected_subgenres)

    selected_emotions = st.sidebar.multiselect("Select emotions", options=sorted(filtered_df['emotion'].unique()))
    selected_decades = st.sidebar.multiselect("Select decades", options=sorted(filtered_df['decade'].unique()))

    if selected_emotions or selected_decades:
        filtered_df = filtered_df[filtered_df['emotion'].isin(selected_emotions) | filtered_df['decade'].isin(selected_decades)]
    
    if selected_emotions and selected_decades:
        filtered_df = filtered_df[(filtered_df['emotion'].isin(selected_emotions)) & (filtered_df['decade'].isin(selected_decades))]

    selected_artists = st.sidebar.multiselect("Select artists", options=sorted(filtered_df['track_artist'].unique()))

    available_albums = get_available_albums(filtered_df, selected_artists)
    selected_albums = st.sidebar.multiselect("Select albums", options=available_albums)

    if st.sidebar.button("Show results"):
        filtered_df = filter_music(filtered_df, 
                                   artist=selected_artists, 
                                   album=selected_albums, 
                                   genres=selected_genres, 
                                   subgenres=selected_subgenres, 
                                   emotions=selected_emotions, 
                                   decades=selected_decades)
        
        st.write(f"### {len(filtered_df)} results")
        st.dataframe(filtered_df[['track_name', 'track_artist', 'track_album_name', 'emotion', 'playlist_genre', 'playlist_subgenre', 'decade']])
    else:
        st.write("### Please select criteria to display musics.")

if __name__ == "__main__":
    main()

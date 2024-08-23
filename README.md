### Exploration Notebook
**Data Cleaning**  
We start by removing the 'track_popularity' and 'playlist_name' columns which do not interest us.
Next, we remove rows containing null values ​​in the 'track_name', 'track_artist' and 'track_album_name' columns.
We create a 'track_album_release_year' column from the 'track_album_release_date' column to keep only the date, then we delete the old column.

**Fixing Inconsistencies**  
We look for outliers in the numeric columns.
The 'track_album_release_year' and 'tempo' columns contain values ​​of 0, so we delete the rows containing these values.

**Removing Duplicates**  
We remove duplicate values ​​in the 'track_id' column.

**Standardization**  
In order to manipulate data efficiently, we standardize numerical data (except the 'track_album_release_year' column).

**Exploratory Data Analysis**  
Here we observe that the gender distribution is not too unbalanced.
On the other hand, the distribution of years of music release follows an exponential trend. 

**Emotions Clustering**  
For the application, we will need to select different emotions regarding the music.
These clusters are defined from musical data, namely the columns 'danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness', 'valence', 'tempo'
We start by determining how many clusters would be ideal using the KMeans method.
This gives us 5 clusters, so we group our data into these 5 clusters.
Then by analyzing the data from each cluster, we define the titles: Happy, Sad, Epic, Chill and Exciting

**Assigning Decades**  
Here we group music from different decades (1950's, 1960's, 1970's, 1980's, 1990's, 2000's, 2010's and 2020's).

### Modeling Notebook

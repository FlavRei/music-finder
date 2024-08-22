### Exploration Notebook
**Data Cleaning**
Nous commençons par retirer les colonnes 'track_popularity' et 'playlist_name' qui ne nous intéressent pas.
Ensuite, nous supprimons les lignes contenant des valeurs nulles dans les colonnes 'track_name', 'track_artist' et 'track_album_name'.
Nous créons une colonne 'track_album_release_year' à partir de la colonne 'track_album_release_date' pour ne garder que la date, puis nous supprimons l'ancienne colonne.

**Fixing Inconsistencies**
Nous recherchons les valeurs aberrantes dans les colonnes numériques.
Les colonnes 'track_album_release_year' et 'tempo' contiennent des valeurs à 0, donc nous supprimons les lignes contenant ces valeurs.

**Removing Duplicates**
Nous supprimons les valeurs en double dans la colonne 'track_id'.

**Standardization**
Afin de manipuler les données efficacement, nous standardisons les données numériques (sauf la colonne 'track_album_release_year').

**Exploratory Data Analysis**
Ici, nous observons que la distribution des genres n'est pas trop déséquilibrée.
En revanche, la distribution des années de sortie des musiques suit une tendance exponentielle.  

**Emotions Clustering**
Pour l'application, nous aurons besoin de sélectionner différentes émotions concernant les musiques.
Ces clusters sont définis à partir des données musicales, à savoir les colonnes 'danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness', 'valence', 'tempo'
Nous commençons par déterminer combien de clusters seraient idéals avec la méthode KMeans.
Cela nous donne 5 clusters, nous regroupons donc nos données dans ces 5 clusters.
Puis en analysant les données de chaque cluster, nous définissons les intitulés :
- Happy
- Sad
- Epic
- Chill
- Exciting

**Assigning Decades**
Ici, nous regroupons les musiques dans différentes décennies (50s, 60s, 70s, 80s, 90s, 00s, 10s et 20s).
-- my genres
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_shows
ON tv_show_genres.genre_id = tv_shows.id
WHERE tv_genres.title = "Dexter"
ORDER BY tv_genres.name;;

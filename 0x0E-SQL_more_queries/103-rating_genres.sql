-- List all genres by their rating
SELECT
	tg.name,
	SUM(tsr.rate) AS `rating`
FROM
	tv_genres AS tg
	LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
	LEFT JOIN tv_show_ratings AS tsr ON tsr.show_id = tsg.show_id
GROUP BY
	tg.name
ORDER BY
	SUM(tsr.rate) DESC;

WITH recursive cte (id, pid, NAME, description) as(
	SELECT id, pid, NAME, description
	FROM tree_table
	WHERE id=1
	UNION all
	SELECT a.id, a.pid, a.name, a.description
	FROM tree_table a
	INNER JOIN cte
	ON a.pid = cte.id
)
SELECT * FROM cte ORDER BY pid asc, id asc;
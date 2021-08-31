SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM
    (SELECT *, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS row_id 
    FROM student) AS tmp
GROUP BY row_id;
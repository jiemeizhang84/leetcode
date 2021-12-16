WITH tmp AS (
    SELECT f.user1_id as user_id, l.page_id as page_id
    FROM friendship f
    INNER JOIN likes l
    ON f.user2_id = l.user_id
    UNION ALL
    SELECT f.user2_id as user_id, l.page_id as page_id
    FROM friendship f
    INNER JOIN likes l
    ON f.user1_id = l.user_id
)

SELECT t.user_id, t.page_id, count(t.page_id) friends_likes
FROM tmp t
WHERE not exists (SELECT l.user_id, l.page_id FROM likes l where t.user_id = l.user_id and t.page_id = l.page_id)
GROUP BY 1,2
ORDER BY 1 ASC, 3 DESC
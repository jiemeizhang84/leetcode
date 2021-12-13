with cte as
(
select user1_id, user2_id from Friendship
union all
select user2_id as user1_id, user1_id as user2_id from Friendship
)


SELECT DISTINCT l1.user_id user_id, l2.user_id recommended_id
FROM listens l1
INNER JOIN listens l2
ON l1.song_id=l2.song_id 
AND l1.day=l2.day
AND l1.user_id<>l2.user_id
WHERE NOT EXISTS (SELECT * FROM cte f WHERE l1.user_id = f.user1_id AND l2.user_id = f.user2_id)
GROUP BY l1.user_id, l2.user_id, l1.day
HAVING COUNT(distinct l1.song_id)>=3
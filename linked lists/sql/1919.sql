SELECT DISTINCT f.user1_id, f.user2_id
FROM friendship f
INNER JOIN listens l1
ON f.user1_id = l1.user_id
INNER JOIN listens l2
ON f.user2_id = l2.user_id
and l1.song_id = l2.song_id AND l1.day = l2.day
GROUP BY f.user1_id, f.user2_id, l1.day
HAVING COUNT(distinct l1.song_id)>=3

# select distinct
# user1_id,
# user2_id
# from Friendship f
# join Listens l1
# on f.user1_id = l1.user_id
# join Listens l2
# on f.user2_id = l2.user_id
# where l1.song_id = l2.song_id
# and l1.day = l2.day
# group by 1,2,l1.day
# having count( distinct l1.song_id) >=3
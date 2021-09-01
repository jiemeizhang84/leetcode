SELECT id, COUNT(*) num
FROM 
(SELECT requester_id id 
FROM request_accepted 
UNION ALL
SELECT accepter_id id 
FROM request_accepted) tmp  
GROUP BY id  
ORDER BY num DESC  
LIMIT 1;

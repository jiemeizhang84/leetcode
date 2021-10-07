SELECT request_at Day, 
    ROUND(COUNT(IF(Status!='completed', True, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
AND driver_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Day


SELECT request_at Day, 
    ROUND(SUM(case when Status!='completed' then 1 else 0 end) / COUNT(*), 2) AS 'Cancellation Rate'
FROM trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
AND driver_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Day
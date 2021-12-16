SELECT request_at Day, 
    ROUND(COUNT(IF(Status!='completed', True, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
AND driver_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Day

--solution2
SELECT request_at Day, 
    ROUND(SUM(case when Status!='completed' then 1 else 0 end) / COUNT(*), 2) AS 'Cancellation Rate'
FROM trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
AND driver_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Day

select t.request_at Day,
       coalesce(round(sum(case when t.status<>'completed' then 1 else 0 end)*1.00/count(*), 2), 0.00) "Cancellation Rate"
from trips t
inner join users u
on t.client_id=u.users_id and u.banned='No'
inner join users u1
on t.driver_id=u1.users_id and u1.banned='No'
where t.request_at between '2013-10-01' and '2013-10-03'
group by 1
       
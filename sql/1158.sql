select u.user_id as buyer_id, join_date, ifnull(count(order_id),0) as orders_in_2019
from users u
left join 
orders o
on u.user_id = o.buyer_id
and year(order_date)='2019'
group by u.user_id
order by u.user_id;



select u.user_id as buyer_id, join_date, ifnull(cnt,0) as orders_in_2019
from users u
left join 
(select buyer_id, count(order_id) cnt
from orders
where year(order_date)='2019'
group by buyer_id) o
on u.user_id = o.buyer_id
order by u.user_id;
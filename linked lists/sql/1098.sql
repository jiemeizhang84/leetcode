select b.book_id, b.name
from (select * from books where available_from < '2019-05-23') b
left join (select * from orders where dispatch_date between '2018-06-23' and '2019-06-23') o
on b.book_id = o.book_id
group by b.book_id, b.name
having ifnull(sum(o.quantity),0) < 10;
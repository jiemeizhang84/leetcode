select q1.person_name
from queue q1 join queue q2
on q1.turn >= q2.turn
group by q1.turn
having sum(q2.weight) <= 1000
order by sum(q2.weight) desc
limit 1

select person_name
from (
    select *, 
        sum(weight) over(order by turn rows unbounded preceding) total_wt,
        lead(weight, 1) over(order by turn) next_wt
    from queue
) q1
where total_wt <= 1000 and (total_wt + next_wt > 1000 or next_wt is Null)
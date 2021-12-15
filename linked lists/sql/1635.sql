with recursive cte1 as (
    select 1 as month
    union all
    select month+1 as month
    from cte1 
    where month < 12
),

cte2 as(
    select driver_id, join_date,
           case when join_date<'2020-1-1' then 1
            else month(join_date) end as month
    from drivers 
    where join_date < '2021-1-1'    
    ),
cte3 as (
    select month(r.requested_at) month,
          count(r.requested_at) over(partition by left(r.requested_at,7) ) accepted_rides
    from rides r
    join acceptedrides a
    on r.ride_id = a.ride_id
    where requested_at between '2020-1-1' and '2020-12-31'
)


select cte1.month,
    count(distinct cte2.driver_id) as active_drivers,
    ifnull(cte3.accepted_rides,0) as accepted_rides
from cte1
    left join cte2
        on cte2.month <= cte1.month
     left join cte3
        on cte1.month = cte3.month
group by cte1.month
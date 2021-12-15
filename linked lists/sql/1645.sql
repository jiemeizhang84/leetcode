with recursive all_month as (
    select 1 month
    union all
    select month+1 month
    from all_month
    where month<12
),
active_driver as (
    select a.month, 
            coalesce(count(distinct d.driver_id),0) driver_cnt
    from all_month a
    left join drivers d
    on a.month>=month(d.join_date) or year(d.join_date)<2020
    where year(d.join_date)<=2020
    group by a.month
),
accepted_driver as (
    select a.month,
           coalesce(count(distinct d.driver_id),0) accepted_cnt
    from all_month a
    left join (
        select month(r.requested_at) month,
               a.driver_id
        from rides r
        join acceptedrides a
        on r.ride_id = a.ride_id
        where year(requested_at) = 2020
    ) d
    on a.month=d.month
    group by a.month
)

select a.month, 
        case when driver_cnt is null then 0 else round(accepted_cnt*100.00/driver_cnt,2) end as working_percentage
from all_month a
left join accepted_driver b on a.month=b.month
left join active_driver c on a.month=c.month
order by 1
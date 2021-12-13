select s1.spend_date, s1.platform, ifnull(sum(s2.total_amount),0) total_amount, ifnull(count(distinct s2.user_id),0) as total_users
from
(select distinct spend_date, 'mobile' as platform
from spending
union all
select distinct spend_date, 'desktop' as platform
from spending
union all
select distinct spend_date, 'both' as platform
from spending) s1
left join
(select user_id, spend_date, 
        case
            when count(distinct platform) = 2 then 'both'
            else platform
        end as platform,
        sum(amount) total_amount
from spending
group by user_id, spend_date) s2
on s1.spend_date = s2.spend_date and s1.platform = s2.platform
group by s1.spend_date, s1.platform;

select round(avg(daily_avg) * 100, 2) average_daily_percent
from
(select count(distinct r.post_id)/count(distinct a.post_id) daily_avg
from actions a
left join removals r
on a.post_id = r.post_id and r.remove_date > a.action_date
where a.extra = 'spam'
group by a.action_date) a1;



select round(avg(daily_avg) * 100,2) average_daily_percent
from
(select a.action_date, ifnull(count(r.remove_date), 0)/count(a.post_id) daily_avg
from
(select distinct post_id, action_date
from actions
where action = 'report' and extra = 'spam') a
left join removals r
on a.post_id = r.post_id and r.remove_date > a.action_date
group by a.action_date) a1;


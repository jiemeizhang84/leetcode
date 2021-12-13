select install_dt, count(a1.player_id) as installs,
       round(count(a2.player_id) / count(a1.player_id),2) as Day1_retention
from
 (
    select player_id, min(event_date) as install_dt
    from activity
    group by player_id
) as a1
left join activity as a2
on a1.player_id = a2.player_id
and a1.install_dt + 1 = a2.event_date
group by install_dt;
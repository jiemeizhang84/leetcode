select team_id, team_name,
       SUM(case when team_id=host_team and host_goals>guest_goals then 3 else 0 end) +
       sum(case when team_id=host_team and host_goals=guest_goals then 1 else 0 end) +
       sum(case when team_id=guest_team and host_goals<guest_goals then 3 else 0 end) +
       sum(case when team_id=guest_team and host_goals=guest_goals then 1 else 0 end)
       as num_points
from teams 
left join matches 
on team_id = host_team or team_id = guest_team
group by team_id
order by num_points desc, team_id
select business_id
from
(select *, avg(occurences) over(partition by event_type) avg_occur
from events) e
where occurences > avg_occur
group by business_id
having count(event_type) > 1;


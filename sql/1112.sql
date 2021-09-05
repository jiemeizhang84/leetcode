select student_id, course_id, grade
from
(select *, row_number() over(partition by student_id order by grade desc, course_id) rk
 from enrollments
) e
where rk = 1
order by student_id;


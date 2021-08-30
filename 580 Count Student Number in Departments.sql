WITH tmp AS (
    SELECT dept_id, COUNT(student_id) student_number
    FROM student
    GROUP BY dept_id
)

SELECT dept_name, IFNULL(student_number, 0) student_number
FROM department d
LEFT JOIN tmp t
ON d.dept_id = t.dept_id
ORDER BY student_number DESC

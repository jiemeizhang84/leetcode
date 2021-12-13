WITH tmp AS(
    SELECT employee_id, experience, salary,
       SUM(salary) OVER(PARTITION BY experience ORDER BY salary) AS running_sum
    FROM candidates
),
senior_tmp AS(
    SELECT employee_id, experience, running_sum
    FROM tmp
    WHERE running_sum <= 70000 AND experience = 'Senior'
),
junior_tmp AS(
    SELECT employee_id, experience, running_sum
    FROM tmp
    WHERE running_sum <= 70000 - (SELECT COALESCE(MAX(running_sum), 0) FROM senior_tmp) AND experience = 'Junior'
)

SELECT 'Senior'AS experience,
        COALESCE(COUNT(employee_id),0) AS accepted_candidates
FROM senior_tmp
UNION ALL
SELECT 'Junior'AS experience,
        COALESCE(COUNT(employee_id),0) AS accepted_candidates
FROM junior_tmp
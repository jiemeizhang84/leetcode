WITH tmp AS 
(SELECT employee_id, experience,
        SUM(salary) OVER (PARTITION BY experience ORDER BY salary) AS running_sum
FROM candidates),

senior_tmp AS
(SELECT employee_id, running_sum
FROM tmp
WHERE running_sum <= 70000 AND experience = 'Senior'),

junior_tmp AS
(SELECT employee_id, running_sum
FROM tmp
WHERE running_sum <= (70000 - (SELECT COALESCE(MAX(running_sum), 0) FROM senior_tmp))
AND experience = 'Junior')



SELECT employee_id
FROM senior_tmp
UNION ALL
SELECT employee_id
FROM junior_tmp
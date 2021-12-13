SELECT e1.id, MAX(e2.month) month, SUM(e2.salary) salary
FROM employee e1, employee e2
WHERE e1.id = e2.id
AND e2.month BETWEEN (e1.month - 3) AND (e1.month - 1)
GROUP BY e1.id, e1.month
ORDER BY id, month DESC;


-- SELECT id, month, salary
-- FROM (
--     SELECT id,
--            month,
--            SUM(salary) OVER(PARTITION BY Id ORDER BY month ROWS 2 PRECEDING) AS salary,
--            DENSE_RANK() OVER(PARTITION BY Id ORDER BY month DESC) AS rk
--     FROM Employee
-- )
-- WHERE rk > 1 
-- ORDER BY id, month DESC;
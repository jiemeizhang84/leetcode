select left(trans_date, 7) month,
       country, 
       count(state) trans_count,
       sum( state = 'approved') approved_count,
       sum(amount) trans_total_amount,
       sum(case 
           when state = 'approved' then amount
           else 0
           end) as approved_total_amount
from transactions
group by month, country;


SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(id) AS trans_count,
    COUNT(IF(state = 'approved', 1, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state='approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY 1, 2
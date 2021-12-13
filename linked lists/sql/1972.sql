with tmp AS(
    SELECT caller_id AS caller,
           recipient_id AS recipient,
           call_time
    FROM calls
    UNION ALL
    SELECT recipient_id AS caller,
           caller_id AS recipient,
           call_time
    FROM calls
),

tmp1 AS (
    SELECT caller,
           recipient,
           DATE(call_time) c_date,
           RANK() OVER(PARTITION BY DATE(call_time), caller ORDER BY call_time) AS first_call,
           RANK() OVER(PARTITION BY DATE(call_time), caller ORDER BY call_time DESC) AS last_call
    FROM tmp
)

SELECT DISTINCT t1.caller AS user_id
FROM (SELECT caller, recipient, c_date FROM tmp1 WHERE first_call=1) t1
INNER JOIN (SELECT caller, recipient, c_date FROM tmp1 WHERE last_call=1) t2
ON t1.caller=t2.caller 
AND t1.recipient=t2.recipient
AND t1.c_date=t2.c_date
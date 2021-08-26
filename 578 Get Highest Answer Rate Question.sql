
SELECT question_id AS survey_log
FROM (
    SELECT question_id,
           SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) AS answer_number,
           SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) AS show_number
    FROM survey_log 
    GROUP BY question_id) AS tmp
ORDER BY answer_number/show_number DESC
LIMIT 1; 
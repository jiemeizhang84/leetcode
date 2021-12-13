WITH tmp AS (SELECT *, 
                    SUM(frequency) OVER(ORDER BY number) freq, 
                    (SUM(frequency) OVER())/2 median_freq,
             FROM numbers)

SELECT AVG(number) AS median
FROM tmp
WHERE median_freq BETWEEN (freq - frequency) AND freq;
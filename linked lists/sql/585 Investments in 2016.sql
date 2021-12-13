-- 1
SELECT ROUND(SUM(TIV_2016),2) TIV_2016
FROM insurance i1
WHERE 1 = (SELECT COUNT(*) FROM insurance i2 WHERE i1.LAT = i2.LAT AND i1.LON = i2.LON)
AND 1 < (SELECT COUNT(*) FROM insurance i3 WHERE i1.TIV_2015 = i3.TIV_2015);


-- 2
SELECT ROUND(SUM(TIV_2016),2) TIV_2016
FROM insurance
WHERE PID IN (
    SELECT i1.PID
    FROM insurance i1, insurance i2
    WHERE i1.TIV_2015 = i2.TIV_2015
    AND i1.PID <> i2.PID
    AND (i1.LAT+i1.LON) <> (i2.LAT+i2.LON) 
)
AND PID NOT IN (
    SELECT i1.PID
    FROM insurance i1, insurance i2
    WHERE (i1.LAT+i1.LON) = (i2.LAT+i2.LON) 
    AND i1.PID <> i2.PID
);
  
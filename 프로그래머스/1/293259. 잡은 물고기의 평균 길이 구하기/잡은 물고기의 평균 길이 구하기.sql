SELECT ROUND(AVG(LENGTH),2) as AVERAGE_LENGTH
FROM (SELECT CASE WHEN LENGTH is NULL THEN 10
      ELSE LENGTH END as LENGTH
     FROM FISH_INFO) FI
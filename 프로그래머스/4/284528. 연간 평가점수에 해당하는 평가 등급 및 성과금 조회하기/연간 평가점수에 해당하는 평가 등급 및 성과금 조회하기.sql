SELECT HE.EMP_NO,EMP_NAME,GRADE
,CASE WHEN GRADE = 'S' THEN SAL*0.2
WHEN GRADE = 'A' THEN SAL*0.15
WHEN GRADE = 'B' THEN SAL*0.1
ELSE 0 END AS BONUS
FROM HR_EMPLOYEES HE
JOIN (SELECT EMP_NO,
      CASE WHEN AVG(SCORE) >= 96 THEN 'S'
      WHEN AVG(SCORE) >= 90 THEN 'A'
      WHEN AVG(SCORE) >= 80 THEN 'B'
      ELSE 'C' END AS GRADE
      FROM HR_GRADE
      GROUP BY EMP_NO) HG
ON HE.EMP_NO = HG.EMP_NO
ORDER BY EMP_NO ASC
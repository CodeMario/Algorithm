SELECT EDC.ID as ID
,EDC.GENOTYPE as GENOTYPE
,EDP.GENOTYPE as PARENT_GENOTYPE
FROM ECOLI_DATA EDC
JOIN ECOLI_DATA EDP
ON EDC.PARENT_ID = EDP.ID
WHERE EDC.GENOTYPE & EDP.GENOTYPE = EDP.GENOTYPE
ORDER BY ID asc
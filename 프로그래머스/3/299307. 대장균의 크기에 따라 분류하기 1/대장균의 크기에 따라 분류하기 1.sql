SELECT
    ID,
    IF(SIZE_OF_COLONY <= 100, 'LOW', IF(SIZE_OF_COLONY > 1000, 'HIGH', 'MEDIUM')) AS SIZE
FROM ECOLI_DATA 
ORDER BY ID ASC;
SELECT COUNT(*) AS FISH_COUNT, f2.FISH_NAME
FROM FISH_INFO AS f1
INNER JOIN FISH_NAME_INFO AS f2 ON f1.FISH_TYPE = f2.FISH_TYPE
GROUP BY f2.FISH_NAME
ORDER BY FISH_COUNT DESC;

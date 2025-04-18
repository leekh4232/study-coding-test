SELECT i.INGREDIENT_TYPE, SUM(f.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO AS i
INNER JOIN FIRST_HALF AS f ON i.FLAVOR = f.FLAVOR
GROUP BY i.INGREDIENT_TYPE
ORDER BY f.TOTAL_ORDER ASC;
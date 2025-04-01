SELECT F.FLAVOR
FROM FIRST_HALF AS F
INNER JOIN ICECREAM_INFO AS I ON F.FLAVOR=I.FLAVOR
WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
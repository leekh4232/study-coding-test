SELECT
    ROUTE,
    CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
    CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
-- TOTAL_DISTANCE를 사용할 경우 CONCAT함수의 결과인
-- 문자열로 변환되기 때문에 정렬 기준이 달라진다.
ORDER BY ROUND(SUM(D_BETWEEN_DIST), 1) DESC;
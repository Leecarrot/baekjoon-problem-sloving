-- 코드를 입력하세요
SELECT A.CAR_ID, A.CAR_TYPE, ROUND(daily_fee * (1 - DISCOUNT_RATE / 100) * 30) AS FEE
FROM (SELECT *
      FROM CAR_RENTAL_COMPANY_CAR
      WHERE (CAR_TYPE = '세단' OR CAR_TYPE = 'SUV') AND CAR_ID IN (SELECT CAR_ID
                                                                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                                   GROUP BY CAR_ID
                                                                   HAVING MAX(END_DATE) < '2022-11-01')) AS A
LEFT JOIN (SELECT CAR_TYPE, DISCOUNT_RATE
           FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
           WHERE DURATION_TYPE	= '30일 이상') AS B
ON A.CAR_TYPE = B.CAR_TYPE
WHERE ROUND(daily_fee * (1 - DISCOUNT_RATE / 100) * 30) BETWEEN 50000 AND 2000000
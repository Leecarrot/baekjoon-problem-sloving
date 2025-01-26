-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM MEMBER_PROFILE AS MP
RIGHT JOIN REST_REVIEW AS RR
ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE MEMBER_NAME IN (SELECT MEMBER_NAME
                        FROM (SELECT MEMBER_NAME, COUNT(RR.MEMBER_ID) AS NUM
                              FROM MEMBER_PROFILE AS MP
                              RIGHT JOIN REST_REVIEW AS RR
                              ON MP.MEMBER_ID = RR.MEMBER_ID
                              GROUP BY RR.MEMBER_ID) AS D
                        WHERE D.NUM = (SELECT MAX(NUM) AS NUM
                                       FROM (SELECT MEMBER_NAME, COUNT(RR.MEMBER_ID) AS NUM
                                             FROM MEMBER_PROFILE AS MP
                                             RIGHT JOIN REST_REVIEW AS RR
                                             ON MP.MEMBER_ID = RR.MEMBER_ID
                                             GROUP BY RR.MEMBER_ID) AS C))
ORDER BY MEMBER_NAME, REVIEW_DATE;
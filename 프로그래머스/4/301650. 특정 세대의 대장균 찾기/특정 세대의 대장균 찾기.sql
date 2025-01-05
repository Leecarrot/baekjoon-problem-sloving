SELECT
    C.ID
FROM    
    ECOLI_DATA AS C
INNER JOIN (SELECT
            A.ID
            FROM
            ECOLI_DATA AS A
            INNER JOIN (SELECT ID
                        FROM ECOLI_DATA
                        WHERE PARENT_ID IS NULL) AS B
                        ON A.PARENT_ID = B.ID) AS D
ON C.PARENT_ID = D.ID
ORDER BY 
    ID ASC;
-- 코드를 입력하세요
SELECT I.FLAVOR
FROM ICECREAM_INFO AS I
INNER JOIN FIRST_HALF AS F ON F.FLAVOR = I.FLAVOR
WHERE TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
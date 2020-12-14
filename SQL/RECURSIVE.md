* 재귀함수
  > 0 ~ 23을 출력한다.
```SQL
    WITH RECURSIVE hour as(
    SELECT 0 as HOUR
    UNION ALL
    SELECT HOUR + 1 
    FROM hour 
    WHERE HOUR < 23
    )SELECT * FROM hour;
```

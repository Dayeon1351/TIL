* DATE_FORMAT(값, '원하는 형태')
  ```SQL
    SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') AS '날짜' 
    FROM ANIMAL_INS;
  ```

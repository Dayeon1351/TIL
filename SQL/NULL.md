* IFNULL
  > NAME의 값이 NULL인 경우 'No name'으로 대체한다.
  ```SQL
  SELECT ANIMAL_TYPE, IFNULL (NAME,'No name') AS 'NAME', SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID;
  ```

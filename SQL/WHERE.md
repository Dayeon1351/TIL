* WHERE의 조합  
  + AND  
  + OR  
  + IN  
  여러 값을 OR 관계로 묶어서 나열
  ```SQL
      SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS 
      WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty'); 
  ```
  + NOT

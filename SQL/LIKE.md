* LIKE  
부분적으로 일치하는 문자 찾기
  + %  
  들어갈 수 있는 문자의 갯수를 지정하지 않음
  ```SQL
      SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
      WHERE NAME LIKE '%el%';       // el이 들어가는 이름
  ```
  + _  
  들어갈 수 있는 문자의 갯수 지정
   ```SQL
      SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
      WHERE NAME LIKE '_el';       // _el이 들어가는 이름
  ```

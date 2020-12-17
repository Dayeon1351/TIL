* sort 
> 배열 정렬
  ```Java
  Arrays.sort(배열);    // 올림차순
  Arrays.sort(배열,Collections.reverseOrder());     // 내림차순
  ```
  
  * copyOfRange  
  > 배열 복사
  ```Java
  Arrays.copyOfRange(원본배열,복사할길이);
  Arrays.copyOfRange(원본배열,시작인덱스,끝인덱스);   //끝인덱스 포함하지 않음
  int[] array = {1,2,3,4,5}
  Arrays.copyOfRange(array,2,5);  // {3,4,5}    
  ```
  

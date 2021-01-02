* Array Initialization
> 배열 초기화
```Java
int[] num1 = {1,2};

int[] num2 = {};
num2 = new int[2];
num2[0]=1;
num2[1]=2;

int[] num3 = {};
num3 = new int[]{1,2}
```

* ArrayList  
> 데이터의 중복 허용하지 않는다. 자동 중복 제거
```Java
ArrayList<Integer> al = new ArrayList<>();
al.add(3);
```

* sort 
> 배열 정렬  
> byte, char, double, short, long, int, float는 내림차순 불가능
  ```Java
  Arrays.sort(배열);    // 올림차순
  Arrays.sort(배열,Collections.reverseOrder());     // 내림차순
  Arrays.sort(배열,Comparator.reverseOrder());      // 내림차순
  ```
  
  * copyOfRange  
  > 배열 복사
  ```Java
  Arrays.copyOf(원본배열,복사할길이);
  Arrays.copyOfRange(원본배열,시작인덱스,끝인덱스);   //끝인덱스 포함하지 않음
  int[] array = {1,2,3,4,5}
  Arrays.copyOfRange(array,2,5);  // {3,4,5}    
  ```
  

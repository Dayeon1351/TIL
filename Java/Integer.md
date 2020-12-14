* 숫자의 길이
  > 12345의 길이는 5이다.
  + 방법1  
  String 변수에 int/long 변수를 더해 length()를 구할 수 있다.
  ```JAVA
    long num = 12345;
    String str = "" + num;
    System.out.println(str.length());   // 5
  ```
   + 방법2  
  int/long 변수를 String 변수로 형변환 후 length()를 구할 수 있다.
  ```JAVA
    long num = 12345;
    System.out.println(Long.toString(num).length());   // 5
  ```

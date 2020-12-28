* String.format  
  > n은 총 자리수  
  > d는 십진정수 s는 문자열
  ```Java
  str = String.format("%0"+ n + "d",str);   // 0은 채워질 문자
  str = String.format("%"+ n + "s",str);    // 공백이 채워진다
  ```  

---

* toCharArray()  
  > String을 char 배열로 변환
  ```Java
  String str = "ABC123";
  char[] c = str.toCharArray();
  // c = {'A','B','C','1','2','3'}
  ```

* split()  
  > String을 String 배열로 변환
  ```Java
  String s1 = "ABC";
  String[] str1 = s1.split("");     // str1 = {"A","B","C"}
  String s2 = "A B C ";
  String[] str = s.split(" ",-1);   // str2 = {"A","B","C"," "}
  ```  

==> 값 비교시 String의 값을 비교하는 것 보다 char의 값을 비교하는 시간이 더 적게 걸린다.  
```Java
Stirng s = "A";
char c = 'A';
if(s.equals("A"))   // 1번
if(c == 'A')        // 2번
// 2번의 경우가 더 빠르다.
```

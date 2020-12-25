* String.format  
> n은 총 자리수  
> d는 십진정수 s는 문자열
```Java
str = String.format("%0"+ n + "d",str);   // 0은 채워질 문자
str = String.format("%"+ n + "s",str);    // 공백이 채워진다
```

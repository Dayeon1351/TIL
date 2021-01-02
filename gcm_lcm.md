* 최대공약수(GCM)   
  > 두 수 m과 n의 공약수 중 가장 큰 값
* 최소공배수(LCM)  
  > 두 수 m과 n의 곱을 최대공약수로 나눈 값  
```Java
 int max = Math.max(n,m);     
 for(int i =1;i<max;i++){
   if(n%i==0&&m%i==0){
     answer[0]=i;
     answer[1] =(m*n)/i;
   }
 }
``` 

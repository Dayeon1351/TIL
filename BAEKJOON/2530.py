import time
from datetime import datetime,timedelta
h,m,s = map(int,input().split())

sec = int(input())
result = datetime(1,1,1,h,m,s)+timedelta(seconds=sec)
print(result.hour,result.minute,result.second)

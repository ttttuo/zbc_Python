#상수
#하드디스크에 저장되는 것.
#한 번 지정되면 변하지 않는다
#변수에 들어갈 수 있는 값

import sys #sys라는 모듈 즉 라이브러리 중 sys.maxsize라는 변수 값을 가져오는 것
t1 = sys.maxsize
t2 = t1 + 1 #그러고 보니까 가장 큰 값인데 1을 더하네.. 버전이 바뀌면서 가능해짐
t3 = t2 **10
print(t1)
print(t2)
print(t3)
print(type(t1))
print(type(t2))
print(type(t3))

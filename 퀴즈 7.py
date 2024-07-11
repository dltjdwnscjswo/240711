# while문을 사용하여 1부터 45사이의 랜덤한 수 6개를 생성하고, 이를 result 리스트 변수에 추가하는 코드
# 작성하라.
# 랜덤한 수 생성 방법
# import random

import random

num=[]
a = 0

while a < 6 :
    a = a + 1
    b=random.randint(1, 45)
    num.append(b)
print(num)




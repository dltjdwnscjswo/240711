# while문을 사용하여 1부터 100까지 수에 존재하는 모든 홀수의 합을 구하시오.
num = []

a = 0

while a < 100 :
   a = a + 1
   if (a % 2) != 0 :
       num.append(a)
c = sum(num)
print(c)

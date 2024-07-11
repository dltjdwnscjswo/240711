# 사용자가 입력한 수가 3의 배수이면 ok 출력하는 프로그램을 작성하시오.
# 그렇지 않으면 no를 출력하시오.

a = int(input("숫자를 입력해주세요."))

b = a%3

if b == 0 :
    print("ok")

else:
    print("no")
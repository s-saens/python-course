def accsum(j, k):
    sum = 0
    for i in range(j, k+1):
        sum += i
    return sum

num = int(input("1. 수식계산  |  2. 누적합: "))
if num == 1:
    exp = input("수식:")
    print("수식 결과는 ", eval(exp), "입니다.")

if num == 2:
    a = int(input("첫번째 수: "))
    b = int(input("두번째 수: "))
    print(a, "+ ... +", b, "=",accsum(a, b))
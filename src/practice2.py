m = int(input("교환할 돈은 얼마?: "))
l = [500, 100, 50, 10]

for i in l:
    print(i,"원짜리 ---> ",m//i,"개")
    m = m % i;

print("바꾸지 못한 잔돈 ---> ",m,"원")
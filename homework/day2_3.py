y=int(input())
if (y % 10 == 0):
    print(f'{y}能被10整除，商：{int(y / 10)}, 餘：{y%10}')
else:
    print(f'{y}不能被10整除，商：{int(y / 10)}, 餘：{y%10}')
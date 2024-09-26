A=int(input("輸入一個三位數:"))
ans=A//100+A//10-A//100*10 +A%10
print("每位數字總和:",ans)
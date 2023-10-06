n, m, goal = map(int, input().split()); # 낮 올 // 밤 내 // 총 길이

if goal < n : 
    print(1)
else:
    if (goal-n) % (n-m) == 0 :
        print((goal-n) // (n-m) +1)
    else :
        print((goal-n) // (n-m) +2)

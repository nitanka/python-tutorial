N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]
idx = [i for i, x in enumerate(B) if x % 2 == 1 ]
if len(idx) % 2 == 1:
    print("NO")
else:
    print(sum([(idx[i+1]-idx[i])*2 for i in range(0,len(idx),2)]))

#!/bin/env python3 

if __name__ == '__main__':
    name = []
    score = []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
        
    second_lowest=sorted(set(score))[1]
    marks = [[a,b] for a,b in zip(name,score)]
    for item in sorted([[a,b] for a,b in marks if b == second_lowest]): print(item[0])
        

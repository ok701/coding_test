H, M = map(int, input().split())

if M - 45 < 0:
    M_2 = 60 + (M - 45)
    H_2 = H - 1

else:
    M_2 = M - 45
    H_2 = H

if H_2 < 0:
    H_2 = 24 + H_2

print(H_2, M_2)
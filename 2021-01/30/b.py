# https://atcoder.jp/contests/abc190/tasks/abc190_b


N, S, D = map(int, input().split())
list = [list(map(int, input().split())) for l in range(N)]
for l in list:
  if S > l[0] and D < l[1]:
    print("Yes")
    exit()

print("No")

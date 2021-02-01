# https://atcoder.jp/contests/abc190/tasks/abc190_a

A, B, C = map(int, input().split())

if C == 0:
  if A > B:
    print("Takahashi")
  else:
    print("Aoki")
else:
  if B > A:
    print("Aoki")
  else:
    print("Takahashi")

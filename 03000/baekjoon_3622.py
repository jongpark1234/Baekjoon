A, a, B, b, P = map(int, input().split())
print('No' if A > P or B > P else 'Yes' if A + B <= P or a >= B or b >= A else 'No')

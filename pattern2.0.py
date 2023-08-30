# for i in range(5):
#     for j in range(i):
#         if j==0 or j==i-1 or i==4:
#             print('*',end="")
#         else:
#             print(' ',end="")
#     print
#------------------------------------------
# n=5
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print(" ",end="")
#     for j in range(i):
#         print('*',end="")
#     print()
# --------------------------------------------------
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print('*',end="")
#     print()
# -----------------------------------------------------
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         if j==0 or j==2*i-2 or i==n:
#             print('*',end="")
#         else:
#             print(' ',end="")
#     print()
# ------------------------------------------------------------
# n=3
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(2*(n-i)-1):
#         print('*',end="")
#     print()
# -----------------------------------------------------------------
# for i in range(9):
#     if i<=4:
#         for j in range(i):
#             print('*',end="")
#         print()
#     else:
#         val=9-i
#         for j in range(val):
#             print('*',end="")
#         print()        
#     print()
# ------------------------------------------------
# n=3
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(2*(n-i)-1):
#         print("*",end="")
#     print()
# for i in range(2,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()
# --------------------------------------------------
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     for k in range(i,n+1):
#         print(" ",end="")
#     for l in range(n-i):
#         print(" ",end="")
#     for m in range(i):
#         print('*',end="")
#     print()
# n=5
# for i in range(2,n+1):
#     for j in range(n+1-i):
#         print('*',end="")
#     for k in range(i-1):
#         print(" ",end="")
#     for l in range(i):
#         print(" ",end="")
#     for m in range(n+1-i):
#         print('*',end="")
#     print()

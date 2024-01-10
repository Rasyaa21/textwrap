text = input()
n = int(input())
texlen = len(text)
howmany = texlen // n
if texlen % n > 0 :
    howmany += 1
for x in range(0,howmany*n,n):
    print(text[x:x+n])
quit()
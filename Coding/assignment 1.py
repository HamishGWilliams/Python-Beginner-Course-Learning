print("hello world")
x = 1
print(x)
# 1

x = x+1
print(x)
# 2

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

name = input("clown.txt:")
handle = open(name, 'r')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

quit()
import time

cont = open('cont.txt', 'r')
softreset = int(cont.readline())

print("Vc esta no Softreset de numero ",softreset)

while True:
    x = input()
    
    if(x == ''):
        softreset+=1
    print("Softreset de numero ",softreset)
    if(x != ''): break

cont = open('cont.txt', 'w')
cont.write(str(softreset))
cont.close()

time.sleep(1)
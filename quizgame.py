import random
import time

def RandI():
    x = None
    R = time.time()
    random.seed(R)
    x = random.randint(0, 690)
    return x

def Rand():
    arr = []
    x = None
    R = time.time()
    random.seed(R)
    for i in range(9):
        arr.append(random.randint(0, 999))
    x = random.randint(0, 999)
    return (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], x)

if __name__ == "__main__":
    m, n, o, p, ab, bc, cd, ef, gh, rand_num = Rand()
    l = 0
    Chin, Phyn, Mean = '', '', ''
    Chi, Phy, Mn = [], [], []
    # file name
    file_name = 'characters.txt'  # replace with the actual file name
    try:
        with open(file_name, 'r') as coeff:
            curr_line = coeff.readline()
            while curr_line != '':
                Chin, Phyn, Mean = curr_line.split("-")
                Chi.append(Chin)
                Phy.append(Phyn)
                Mn.append(Mean[:-1])
                curr_line = coeff.readline()
                l += 1
        N = l - 1
        
        card = [i for i in range(N)]
        
        for i in range(N):
            print(card[i], end=' ')
        print()
        
        j = rand_num % N
        m, n, o, p, ab, bc, cd, ef, gh = (m % N, n % N, o % N, p % N, ab % N, bc % N, cd % N, ef % N, gh % N)
        for i in range(N):
            card[ab], card[bc] = card[bc], card[ab]
            card[ef], card[gh] = card[gh], card[ef]
            card[i], card[j] = card[j], card[i]
            card[m], card[n] = card[n], card[m]
        
        for i in range(N):
            print(card[i], end=' ')
        print()
        
        R = 0
        W = 0
        for jj in range(10):
            aa = RandI()
            tmp = card[jj]
            print("\nWhat is the character?")
            print(Mn[tmp])
            
            if aa % 4 == 0:
                print("1. ", Chi[tmp], Phy[tmp])
                print('2. ', Chi[(tmp+7) % N], Phy[(tmp+7) % N])
                print('3. ', Chi[(tmp+14) % N], Phy[(tmp+14) % N])
                print('4. ', Chi[(tmp+21) % N], Phy[(tmp+21) % N])
                nn = int(input())
                if nn == 1:
                    print('Correct')
                    R += 1
                else:
                    print(Chi[tmp], Phy[tmp])
                    W += 1
            elif aa % 4 == 1:
                print("1. ", Chi[(tmp+7) % N], Phy[(tmp+7) % N])
                print('2. ', Chi[tmp], Phy[tmp])
                print('3. ', Chi[(tmp+14) % N], Phy[(tmp+14) % N])
                print('4. ', Chi[(tmp+21) % N], Phy[(tmp+21) % N])
                nn = int(input())
                if nn == 2:
                    print('Correct')
                    R += 1
                else:
                    print(Chi[tmp], Phy[tmp])
                    W += 1
            elif aa % 4 == 2:
                print("1. ", Chi[(tmp+14) % N], Phy[(tmp+14) % N])
                print('2. ', Chi[(tmp+7) % N], Phy[(tmp+7) % N])
                print('3. ', Chi[tmp], Phy[tmp])
                print('4. ', Chi[(tmp+21) % N], Phy[(tmp+21) % N])
                nn = int(input())
                if nn == 3:
                    print('Correct')
                    R += 1
                else:
                    print(Chi[tmp], Phy[tmp])
                    W += 1
            elif aa % 4 == 3:
                print("1. ", Chi[(tmp+21) % N], Phy[(tmp+21) % N])
                print('2. ', Chi[(tmp+7) % N], Phy[(tmp+7) % N])
                print('3. ', Chi[(tmp+14) % N], Phy[(tmp+14) % N])
                print('4. ', Chi[tmp], Phy[tmp])
                nn = int(input())
                if nn == 4:
                    print('Correct')
                    R += 1
                else:
                    print(Chi[tmp], Phy[tmp])
                    W += 1
        
        print('\nResults: {} correct, {} incorrect'.format(R, W))
    
    except FileNotFoundError:
        print("File not found")

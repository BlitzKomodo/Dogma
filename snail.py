def gen_alpha(x):
    line = list(range(alpha[x][0]+1,alpha[x][-1]+1))
    matrix.append(line)

def gen_beta(x):
    line = list(range(beta[x][0] , beta[x][-1], -1))
    matrix.append(line)

def gen_gamma(x,s,e):
    line = list(range(gamma[x][0]+1,gamma[x][-1]+1))
    count = 0
    for i in range(s,e+1):
        matrix[i].append(line[count])
        count += 1

def gen_delta(x,s,e):
    line = list(range(delta[x][0]+1 , delta[x][-1]+1))[::-1]
    count = 0 
    for i in range(s,e+1):
        matrix[i].insert(0,line[count])
        count += 1

def get_layers():
    if n < 4 :
        b[1] = n**2-1
    else:
        for i in range(1,half):
            b[i] = (n-(2*(i-1)))**2 - (n-(2*i))**2

def get_alpha():
    alpha[1] = [0,n]
    summation = 0
    jump = n
    i = 0
    for i in range(2,half+1):
        summation += b[i-1]
        jump -= 2
        #print("{} , {}".format(summation , jump))
        alpha[i] = [summation , summation + jump]
    if n % 2 == 1 and i != 0:
        alpha[i+1] = [n**2-1,n**2]
    elif i == 0:
        alpha[2] = [n**2-1,n**2]

def get_beta():
    beta[1] = [alpha[1][-1]+n+n-2    ,   alpha[1][0]+n+n-2]
    jump = 2
    if n%2 == 1:
        jump = 4

    i = 0
    
    for i in range(half,1,-1):
        beta[i] = [alpha[i][-1]+jump, alpha[i][0]+jump]
        jump += 4

def get_gamma():
    if n%2 == 1:
        # gamma[half] = [ alpha[half][-1] , beta[half][-1] ]
        # gamma[half-1] =  [ alpha[half-1][-1] , beta[half-1][-1] ]
        for i in range(half,1-1,-1):
            gamma[i] = [ alpha[i][-1], beta[i][-1] +1]
    else:
        for i in range(half,1-1,-1):
            gamma[i] = [ alpha[i][-1], beta[i][-1] +1]

def get_delta():
    if n%2 == 1:
        delta[half] = [ beta[half][0]    ,   alpha[half+1][0]   ]
        z = 1
        for i in range(half-z,1-1,-1):
            delta[i] = [ beta[i][0]    ,   alpha[i+1][0]  ]
    else:
        # delta[half-1] = [ beta[half-1][0]    ,   alpha[half][0]     ]
        # delta[half-2] = [ beta[half-2][0]    ,   alpha[half-1][0]   ]

        for i in range(half-1,1-1,-1):
            delta[i] = [ beta[i][0]    ,   alpha[i+1][0]   ]

n = int( input("ENTER A NATURAL NUMBER: ") )
half = int(n/2)

matrix = []

b = {}

alpha = {}
beta = {}
gamma = {}
delta = {}

get_layers()
get_alpha()

if half == 0:
    half = 1

if n % 2 == 1:
    z = 2
else:
    z = 1
try:
    for i in range(1,half+z):
        gen_alpha(i)
except:
    pass

get_beta()

for i in range(half,0,-1):
    gen_beta(i)

get_gamma()

if n%2 == 1:
    tmid = int(n/2)
    count = 0
    for i in range(half,1-1,-1):
        gen_gamma(i, tmid-count,tmid+count)
        count += 1
else:
    mid1 = int(n/2 - 1)
    mid2 = int(n/2)
    count = 0
    for i in range(half-1,1-1,-1):
        gen_gamma(i, mid1-count, mid2+count)
        count += 1

get_delta()

if n%2 == 1:
    if n%2==1:
        tmid = int(n/2)
    count = 0
    for i in range(half,1-1,-1):
        gen_delta(i, tmid-count,tmid+count)
        count += 1
else:
    mid1 = int(n/2 - 1)
    mid2 = int(n/2)

    count = 0

    # gen_delta(4,mid1,mid2)
    # gen_delta(3,mid1-1,mid2+1)
    # gen_delta(2,mid1-2,mid2+2)
    # gen_delta(1,mid1-3,mid2+3)
    # # gen_delta(3,mid1-1,mid2+1)
    for i in range(half-1,1-1,-1):
        gen_delta(i, mid1-count, mid2+count)
        count += 1

for i in matrix:
    for j in i:
        print("{:5}".format(j),end=" ")
    print()
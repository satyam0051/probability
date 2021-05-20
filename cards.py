def prob(favourable,total):      #This function is used to calculate the probability ,in this finction we gives favourable outcome and total outcome 
    assert favourable<=total,'Please provide valide favourable value'


    return favourable/total  

def fact(n):     #This is the factorial function for calculate the factorial of number 
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        return n*fact(n-1)


def NcR(n,r):                              #This function is used for calculate NcR
    assert r<=n,'r can not greater then n'

    return (fact(n)/(fact(r)*fact(n-r)))

"""This is usefull  where the (or condition is given in questions)"""

def CHSD_or_AKQJ(n,m):     #here we are found the favourable outcome and call the prob function
    assert 0<=n<5 and -1<=m <5,'This (n,m) can not be negative integer'
    if n==0:
        return prob(m*4,52)        #When we give the n=0, m=3(probability of Face card),m=1(ace or king or queen or jack) ,m=4(probability of Honour card)
    else:
        return prob(n*13+m*3,52)  #when we n=2,m=0 (black card only,red card only,two spade or two club etc),one spade pr one king etc
                               #when we give n=3,m=-1 (probability of digit card)

def Pick_or_Drawnp(m,r,*args):          # In this function we are take user define arguments and m,r is fix arguments 
                                                         
                                               #  and after this we call the NCR function for calculate the NcR and after the we add this ncr value one bye one and re                                                 
                                        
                                        #return the sum and also we calculate ncr vale of m,r and sum is divided by ncr of m,r value and after this we we call the pr                                           # function for calculating the probability and return the probabilit
    sum=0
    for arg in range(0,len(args)-1,2):

        sum=sum+NcR(args[arg],args[arg+1])

    return sum/NcR(m,r)





def Pick_and_Drawnp(m,r,*args):

    multi=1

    for arg in range(0,len(args)-1,2):

        multi=multi*NcR(args[arg],args[arg+1])
    return multi/NcR(m,r)

"This is used for Bionomial "
def Bionomial(n,r,a,b):

    return (NcR(n,r)*(a**r)*(b**(n-r)))


"This function is used for Bionomial sequence of sum"


def Bioseq(n,j,a,b,term):
    sum=0

    for i in range(j,term):

        sum=sum+Bionomial(n,i,a,b)

    return sum

        

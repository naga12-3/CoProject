import re


fo=open('C:/Users/Lokesh/Desktop/hi2.txt','r')
sti = fo.read()
a = sti.split('.text')

'''code  for ascii'''

k = a[0].split('\"');

asci_list = list();
for i in range(1, len(k), 2):
    asci_list.append(k[i]);

for i in asci_list:
    k.remove(i)
x = re.findall("[\w]+[:]", a[0])
g = list()
g1 = list()
for i in k:
    for j in (i.split('\n')):
        if (j.strip().isspace() != True and len(j) != 0):
            g1.append(j.strip())



k = -1;

dict1 = dict()
list1 = list()
k1 = -1
fg = g1[:];
ads_var = 0; # to store keys
ads_dict = dict()#dictionary to store address


g1.remove(".data")
i = 0;
k1 = -1
for i in range(len(asci_list)):
    asci_list[i]=asci_list[i].replace('\\n','\n')
while (i < len(g1)):
    if (g1[i] in x):
        for i1 in range(len(x)):
            if (g1[i] == x[i1]):
                if (g1[i + 1][0:5] == ".word"):
                    f = list(map(int, g1[i + 1][6:].split(', ')))
                    dict1.update({x[i1]: ads_var})
                    for gh in f:
                        ads_dict.update({ads_var: gh})
                        ads_var += 4


                elif (g1[i + 1][0:7] == ".asciiz"):
                    k1 = k1 + 1
                    vb = 0
                    dict1.update({x[i1]: ads_var})
                    while (vb < len(asci_list[k1])):
                        ads_dict.update({ads_var: asci_list[k1][vb:vb + 4]})
                        ads_var += 4
                        vb += 4

        i += 2
    elif (g1[i][:5] == '.word'):
        ads_dict.update({ads_var: int(g1[i][6:])})
        ads_var += 4
        i += 1
bus,bdr=a[1].split(".globl main")
dumb,main_fun=bdr.split('main:')
main_list=main_fun.split(':')
loop_list=re.findall("[\w]+[:]",main_fun)
fmain_dict=dict();
for i in range(len(main_list)-1):
    temp=main_list[i].rfind('\n')
    main_list[i]=main_list[i][:temp]
loop_dict=dict();
inst_list=list()

for i in range(len(main_list)):
    for j in main_list[i].split('\n'):
        if(len(j)!=0 and j.isspace()!=True):
            inst_list.append(j.strip())
    if(i!=(len(main_list)-1)):
        loop_dict.update({loop_list[i]:len(inst_list)})

str1='''R0  [r0] = 0
R1  [at] = 0
R2  [v0] = 0
R3  [v1] = 0
R4  [a0] = 1
R5  [a1] = 7ffff67c
R6  [a2] = 7ffff684
R7  [a3] = 0
R8  [t0] = 0
R9  [t1] = 0
R10 [t2] = 0
R11 [t3] = 0
R12 [t4] = 0
R13 [t5] = 0
R14 [t6] = 0
R15 [t7] = 0
R16 [s0] = 0
R17 [s1] = 0
R18 [s2] = 0
R19 [s3] = 0
R20 [s4] = 0
R21 [s5] = 0
R22 [s6] = 0
R23 [s7] = 0
R24 [t8] = 0
R25 [t9] = 0
R26 [k0] = 0
R27 [k1] = 0
R28 [gp] = 10008000
R29 [sp] = 7ffff678
R30 [s8] = 0
R31 [ra] = 0''';
reg_list=str1.split('\n')
reg_dict=dict()
for i in  reg_list:
    reg_dict.update({'$'+i[5:7]:0})


def print_reg():
    print("printing Registers")
    for i in reg_list:
        print(i[:11], end="")
        print(reg_dict['$' + i[5:7]])

def print_adsdict():
    s12=8
    lis=[]
    print('                         DATA SEGMENT')
    #print(ads_dict)
    for i in ads_dict:
        if(i==ads_var+4):
            break
        if(i%16==0):
            hj=hex(i)
            jk=10010000+int(hj[2:])
            print('[',end='')
            print(jk,end=']      ')
        if(type(ads_dict[i])==type(s12)):

            #print(hex(i+4096),':',end='')
            print('0'*(10-len(hex(ads_dict[i]))),end='')
            print(hex(ads_dict[i])[2:],end='  ')
            lis.append('. '*4)

        else:
            #print(hex(i+4096),end=': ')
            ds=''
            for j in range(4):
                try:
                    dfs=str(hex(ord(ads_dict[i][3-j]))[2:])
                    ds=ds+'0'*(2-len(dfs))+dfs
                except:
                    ds=ds+"00"
            vc=''

            print(ds,end='  ')
            for hg in range(4):
                try:
                    if(ads_dict[i][hg]!='\n'):
                        vc=vc+ads_dict[i][hg]+' '
                    else:
                        vc=vc+'. '
                except:
                    vc=vc+'. '
            lis.append(vc)
        if(i%16==12):
            for h22 in lis:
                print(h22,end='')
            lis=[]
            print()

        s12=i
    asw=3-(int((s12%16)/4))

    if(s12%16!=12):
        for gh12 in range(asw):
            print('0'*8,end='  ')
            lis.append('. '*4)
        for h22 in lis:
            print(h22, end='')
    print()
pc=0
'''modification of instruction list'''
i=list()
for j in inst_list:
    v=j.find(' ')
    wan=j[0:v]+" "
    bf=j[v:].split(',')
    gf=0
    while(gf<len(bf)):
        if(gf!=len(bf)-1):
            wan=wan+bf[gf].strip()+","
        else:
            wan = wan + bf[gf].strip()
        gf+=1
    i.append(wan)

for hj in range(len(i)):
    i[hj]=i[hj].replace('$zero','$r0')

k=1;
rq=list()
rq=i[:]
#print(rq)
#print(loop_dict)
s1=0;
s2=0;
s3=0;
s4=0;
s5=0;
k=1;
cycle=0;
count=1;
iso_list=[];
v=0;
p1=0;
stalls=0
instructions=0


'''  cache   '''

import math


print('Enter size in bytes')
print('Size of main memory :',end='')
M1=int(input())
print('Size of Cache-level-1 :',end='')
C1=int(input())
print('Block size for Cache-level-1 :',end='')
Block1=int(input())
print('Associvity :',end="")
A1=int(input())
print('Size of cache-level-2 :',end='')
C2=int(input())
print('Block size for Cache-level-2 :',end='')
Block2=int(input())
print('Associvity :',end="")
A2=int(input())
print('Time taken to access Cache_level_1(cycles):',end='')
T1=int(input())
print('Time taken to access Cache_level_2(cycles):',end='')
T2=int(input())
print('Time taken to access Main_Memory(cycles):',end='')
T3=int(input())
global hit1
global hit2
global access
hit1=0
hit2=0
access=0
'''Main_memory=dict()
for i7 in range(int(M1/4)):
    Main_memory.update({i7*4:0})'''

global b1
global set_bits1
global offset_bits1
global tag_bits1
global tot_bits
global b2
global set_bits2
global offset_bits2
global tag_bits2

b1=list()
tot_bits=int(math.log(M1,2))
offset_bits1=int(math.log(Block1,2))
set_bits1=int(math.log(C1/(Block1*A1),2))
tag_bits1=tot_bits-(offset_bits1+set_bits1)
'''print('total bits  :',tot_bits)
print('Cache at level 1')
print('offset bits :',offset_bits1)
print('set bits    :',set_bits1,int(pow(2,set_bits1)))
print('tag bits    :',tag_bits1)'''
b2=list()
offset_bits2=int(math.log(Block2,2))
set_bits2=int(math.log(C2/(Block2*A2),2))
tag_bits2=tot_bits-(offset_bits2+set_bits2)
'''print('Cache at level 2')
print('offset bits :',offset_bits2)
print('set bits    :',set_bits2,int(pow(2,set_bits2)))
print('tag bits    :',tag_bits2)'''

class block:
    valid=0
    dirty=0
    tag="None"
    order=0



for i7 in range(int(pow(2,set_bits1))+1):
    b1.append(list())
    for j in range(A1):
        b1[i7].append(block())
for i7 in range(int(pow(2,set_bits2))+1):
    b2.append(list())
    for j in range(A2):
        b2[i7].append(block())

class functions:
    global b1
    global set_bits1
    global offset_bits1
    global tag_bits1
    global tot_bits
    def search1(x):
        y = '0' * (tot_bits + 2 - len(bin(x))) + bin(x)[2:]
        set = y[tot_bits - (set_bits1 + offset_bits1):tot_bits - (offset_bits1)]
        offset = y[tot_bits - (offset_bits1):]
        tag1= y[0:tot_bits - (set_bits1 + offset_bits1)]
        '''print('set No:',set)
        print('offset :',offset,int(offset,2))
        print('tag :',tag1)'''
        if (len(set) == 0):
            v = 0
        else:
            v = int(set, 2)
        for i7 in range(A1):
            #print(b1[v][i].tag)
            if(b1[v][i7].tag==tag1 and b1[v][i7].valid==1) :
                df=b1[v][i7].order
                if(df!=1):
                    b1[v][i7].order = 1
                    for j in range(A1):
                        if(j!=i7 and b1[v][j]!=0 and b1[v][j].order<df ):
                            b1[v][j].order+=1;

                return True
        return False
    def remove(x):
        y = '0' * (tot_bits + 2 - len(bin(x))) + bin(x)[2:]
        set = y[tot_bits - (set_bits1 + offset_bits1):tot_bits - (offset_bits1)]
        offset = y[tot_bits - (offset_bits1):]
        tag1 = y[0:tot_bits - (set_bits1 + offset_bits1)]
        if(len(set)==0):
            v=0
        else:
            v = int(set, 2)
        for i7 in range(A1):
            # print(b1[v][i].tag)
            if (b1[v][i7].tag == tag1 and b1[v][i7].valid == 1):
                df = b1[v][i7].order
                if (df != 1):
                    b1[v][i7].order = 0
                    for j in range(A1):
                        if (j != i7 and b1[v][j] != 0 and b1[v][j].order > df):
                            b1[v][j].order -= 1;





    def load1(x):
        y = '0' * (tot_bits + 2 - len(bin(x))) + bin(x)[2:]
        set = y[tot_bits - (set_bits1 + offset_bits1):tot_bits - (offset_bits1)]
        offset = y[tot_bits - (offset_bits1):]
        tag1 = y[0:tot_bits - (set_bits1 + offset_bits1)]
       # print('set No:', set, int(set, 2))
       # print('offset :', offset, int(offset, 2))
        #print('tag :', tag1)
        k=-1
        f=0
        if (len(set) == 0):
            v = 0
        else:
            v = int(set, 2)
        for i7 in range(A1):
            #print(b1[v][i].valid)
            if (b1[v][i7].valid == 0):
                b1[v][i7].tag=tag1
                b1[v][i7].order=1
                b1[v][i7].valid=1
                f=1
                for j in range(A1):
                    if(i7!=j and b1[v][j].valid!=0):
                        b1[v][j].order+=1
                break;


        if(f!=1):
            for i7 in range(A1):
                #print(b1[v][i].valid)
                if (b1[v][i7].order == A1):
                    evict_ads=int((b1[v][i7].tag+bin(v)[2:]+'0'*offset_bits1),2)
                    #functions.load2(evict_ads)
                    b1[v][i7].tag = tag1
                    b1[v][i7].order = 1
                else:
                    b1[v][i7].order += 1

    def search2(x):
        y = '0' * (tot_bits + 2 - len(bin(x))) + bin(x)[2:]
        set = y[tot_bits - (set_bits2 + offset_bits2):tot_bits - (offset_bits2)]
        offset = y[tot_bits - (offset_bits2):]
        tag1 = y[0:tot_bits - (set_bits2 + offset_bits2)]
        '''print('set No:',set, int(set, 2))
        print('offset :',offset,int(offset,2))
        print('tag :',tag1)'''

        if(len(set)==0):
            v=0
        else:
            v = int(set, 2)
        for i7 in range(A2):
            # print(b1[v][i].tag)
            if (b2[v][i7].tag == tag1 and b2[v][i7].valid == 1):
                df = b2[v][i7].order

                functions.load1(x)
                if (df != 1):
                    b2[v][i7].order = 1
                    for j in range(A2):
                        if (j != i7 and b2[v][j] != 0 and b2[v][j].order < df):
                            b2[v][j].order += 1;

                return True
        return False
    def load2(x):
        y = '0' * (tot_bits + 2 - len(bin(x))) + bin(x)[2:]
        set = y[tot_bits - (set_bits2 + offset_bits2):tot_bits - (offset_bits2)]
        offset = y[tot_bits - (offset_bits2):]
        tag1 = y[0:tot_bits - (set_bits2 + offset_bits2)]
        '''print('set No:',set, int(set, 2))
        print('offset :',offset,int(offset,2))
        print('tag :',tag1)'''
        k = -1
        f = 0
        if(len(set)==0):
            v=0
        else:
            v = int(set, 2)
        for i7 in range(A2):
            # print(b1[v][i].valid)
            if (b2[v][i7].valid == 0):
                b2[v][i7].tag = tag1
                b2[v][i7].order = 1
                b2[v][i7].valid = 1
                f = 1
                for j in range(A2):
                    if (i7 != j and b2[v][j].valid != 0):
                        b2[v][j].order += 1
                break;

        if (f != 1):
            for i7 in range(A2):
                # print(b1[v][i].valid)
                if (b2[v][i7].order == A2):
                    evict_ads = int((b2[v][i7].tag + bin(v)[2:] + '0' * offset_bits2), 2)
                    functions.remove(evict_ads)
                    b2[v][i7].tag = tag1
                    b2[v][i7].order = 1
                else:
                    b2[v][i7].order += 1
def check(adss):
    #print('Enter the address u want to search for')
    #ads=int(input())
    global access
    global hit1
    global hit2
    access+=1
    if(functions.search1(adss)):
        #print('It is found in the cache -level-1 HIT  ,  cycles taken = ',T1)
        hit1+=1
        return T1
    elif(functions.search2(adss)):
        #print('It is found in the cache -level-2  HIT   ,   cycles taken = ',T1+T2)
        hit2+=1
        return T1+T2
    else:
        functions.load1(adss)
        functions.load2(adss)
        #print('It is in memory - MISS   ,   cycles taken = ',T1+T2+T3)
        return T1+T2+T3
def pint():
    for i7 in range(A1):
        print('Block ',i7,end="")
        print('  tag = ',b1[0][i7].tag,end="")
        print('  order =',b1[0][i7].order)
        print()
    for i7 in range(A2):
        print('Block ',i7,end="")
        print('  tag = ',b2[0][i7].tag,end="")
        print('  order =',b2[0][i7].order)
''' cache  '''
#print_adsdict()
love=0
love1=0
while(1):
    cycle=cycle+1;
    if(1):
        if(s4!=0):
            s5=s4;
            s4=0;
        else:
            s5=0
        if((s5!=0 and  rq[s5-1]=="jr $ra") or s5==len(rq)):#need to remove statemnt after or
            #print(cycle,' - ',s1, s2, s3, s4, s5)
            break

    if(s4==0):
        if(s3!=0):

            if(rq[s3-1][0:2]=="lw"):
                bket = rq[s3-1].rfind('(')
                bket = int(rq[s3-1][7:bket]) + reg_dict[rq[s3-1][bket + 1:len(rq[s3-1]) - 1]]
                if(love==0):
                    st_ch=check(bket)
                    love=1
                if(st_ch!=0):
                    st_ch-=1;
                    stalls+=1;
                if(st_ch==0):
                    reg_dict[rq[s3 - 1][3:6]] = ads_dict[bket]
                    love = 0
                    s4 = s3;
                    s3 = 0;
                    stalls-=1
            elif(rq[s3-1][0:2]=="sw"):
                if(rq[s3-1][3:6] not in iso_list):
                    bket = rq[s3 - 1].rfind('(')
                    bket = int(rq[s3 - 1][7:bket]) + reg_dict[rq[s3 - 1][bket + 1:len(rq[s3 - 1]) - 1]]
                    if (love1 == 0):
                        st_ch1 = check(bket)
                        love1 = 1
                        #print(st_ch1)
                    if (st_ch1 != 0):
                        st_ch1 -= 1;
                        stalls += 1;
                    if(st_ch1==0):
                        love1=0
                        stalls-=1
                        ads_dict[bket]=reg_dict[rq[s3 - 1][3:6]]
                        s4 = s3;
                        s3 = 0
                else:
                    stalls+=1
            else:
                s4=s3;
                s3=0;



    if(s3==0):
        if(s2!=0):
            if(rq[s2-1][0:4]=="addi"):
                if (rq[s2 - 1][9:12] not in iso_list):
                    iso_list.append(rq[s2 - 1][5:8])
                    # print('add',rq[s2-1][4:7])
                    reg_dict[rq[s2 - 1][5:8]] = reg_dict[rq[s2 - 1][9:12]] + int(rq[s2 - 1][13:])
                    s3 = s2;
                    s2 = 0
                else:
                    stalls += 1


            elif(rq[s2-1][0:3]=="add"):
                if((rq[s2-1][8:11] not in iso_list) and (rq[s2-1][12:15] not in iso_list)):
                    iso_list.append(rq[s2-1][4:7])
                    #print('add',rq[s2-1][4:7])
                    reg_dict[rq[s2-1][4:7]]=reg_dict[rq[s2-1][8:11]]+reg_dict[rq[s2-1][12:15]]
                    s3=s2;
                    s2=0
                else:
                    stalls+=1
            elif (rq[s2 - 1][0:4] == "subi"):
                if (rq[s2 - 1][9:12] not in iso_list):
                    iso_list.append(rq[s2 - 1][5:8])
                    # print('add',rq[s2-1][4:7])
                    reg_dict[rq[s2 - 1][5:8]] = reg_dict[rq[s2 - 1][9:12]] -int(rq[s2 - 1][13:])
                    s3 = s2;
                    s2 = 0
                else:
                    stalls += 1

            elif(rq[s2-1][0:3]=="sub"):
                if ((rq[s2 - 1][8:11] not in iso_list) and (rq[s2 - 1][12:15] not in iso_list)):
                    iso_list.append(rq[s2- 1][4:7])
                    reg_dict[rq[s2 - 1][4:7]] = reg_dict[rq[s2 - 1][8:11]] - reg_dict[rq[s2 - 1][12:15]]
                    s3 = s2;
                    s2 = 0;
                else:
                    stalls+=1
            elif(rq[s2-1][0:2]=="lw"):
                bket=rq[s2-1].find('(')

                if(rq[s2-1][bket:(len(rq[s2-1])-1)] not in iso_list):
                    iso_list.append(rq[s2-1][3:6])
                    s3=s2;
                    s2=0;
                else:
                    stalls+=1
            elif(rq[s2-1][0:2]=="sw"):
                bket = rq[s2 - 1].find('(')

                if (rq[s2 - 1][bket+1:(len(rq[s2 - 1]) - 1)] not in iso_list):
                    s3 = s2;
                    s2 = 0;
                else:
                    stalls += 1
            elif(rq[s2-1][0:3]=="sll"):
                if(rq[s2 - 1][8:11] not in iso_list):
                    iso_list.append(rq[s2 - 1][4:7])
                    reg_dict[rq[s2 - 1][4:7]] = reg_dict[rq[s2 - 1][8:11]] *pow(2,int( rq[s2 - 1][12:]))
                    s3 = s2;
                    s2 = 0;
                else:
                    stalls += 1
            elif (rq[s2 - 1][0:3] == "slt"):
                if (rq[s2 - 1][8:11] not in iso_list and rq[s2-1][12:15] not in iso_list):
                    iso_list.append(rq[s2 - 1][4:7])
                    if(reg_dict[rq[s2 - 1][8:11]] < reg_dict[rq[s2 - 1][12:]]):
                        reg_dict[rq[s2 - 1][4:7]] = 1
                    else:
                        reg_dict[rq[s2 - 1][4:7]] =0
                    s3 = s2;
                    s2 = 0;
                else:
                    stalls += 1

            else:
                s3=s2;
                s2=0;


    if(s2==0):
        if(s1!=0):
            if(rq[s1-1][0:3]=="bne" or rq[s1-1][0:3]=="beq"):
                if(rq[s1-1][4:7]==rq[s1-1][8:11]):
                    if (rq[s1 - 1][0:3] == "beq"):
                        count = loop_dict[rq[s1 - 1][12:] + ':'] + 1
                    else:
                        count=count;
                    s2 = s1;
                    s1 = 0;
                    v = 1


                elif((rq[s1-1][4:7] in iso_list) or (rq[s1-1][8:11] in iso_list)):
                    #print('in')
                    stalls+=1;

                else:
                    if(rq[s1-1][0:3]=="bne"):
                        if(reg_dict[rq[s1-1][4:7]]!=reg_dict[rq[s1-1][8:11]]):
                            #print('yes')
                            count=loop_dict[rq[s1-1][12:]+':']+1
                    else:
                        if(reg_dict[rq[s1-1][4:7]]==reg_dict[rq[s1-1][8:11]]) :
                            count = loop_dict[rq[s1 - 1][12:] + ':'] + 1
                    s2=s1;
                    s1=0;
                    v=1
            elif(rq[s1-1][0:2]=='la'):
                reg_dict[rq[s1-1][3:6]]=dict1[rq[s1-1][7:]+':']
                iso_list.append(rq[s1-1][3:6])
                s2=s1;
                s1=0;
            else:
                s2=s1;
                s1=0;


    if(s1==0):
        if(p1!=1 and v!=1):
            s1=count;
            if(rq[s1-1][0:2]=="j "):
                count=loop_dict[rq[s1-1][2:]+':']+1
            else:
                count=count+1;
            instructions+=1;

            if (rq[s1-1] == "jr $ra"):
                p1 = 1
        if (v == 1):
            stalls += 1
            v=0



    #print(iso_list)
    if(rq[s3-1][0:4]=="addi" or rq[s3-1][0:4]=="subi"):
        if(rq[s3-1][5:8] in iso_list):
            iso_list.remove(rq[s3-1][5:8])
    elif(rq[s3-1][0:3]=="add" or rq[s3-1][0:3]=="sub"):
        if(rq[s3-1][4:7] in iso_list):
            iso_list.remove(rq[s3-1][4:7])
    elif(rq[s3-1][0:3]=="sll" or rq[s3-1][0:3]=="slt"):
        if (rq[s3 - 1][4:7] in iso_list):
            iso_list.remove(rq[s3 - 1][4:7])


    if(rq[s4-1][0:2]=="lw"):
        if(rq[s4-1][3:6] in iso_list):
            iso_list.remove(rq[s4-1][3:6])
    if(rq[s2-1][0:2]=='la'):
        if(rq[s2-1][3:6] in iso_list):
            iso_list.remove(rq[s2 - 1][3:6])
    #print(cycle,' - ',s1,s2,s3,s4,s5)

print("stalls = ",stalls)
print("cycles = ",cycle)
print("Number of Instructions executed = ",instructions)
print("IPC = ",instructions/(instructions+stalls))
print_adsdict()
#print_reg()
print(ads_dict)
H1=hit1/access
H2=hit2/access
mr1=(access-hit1)/access
mr2=(access-hit2)/access
print("Tavg =", H1 * T1 + mr1 * (H2 * T2 +mr2 *T3 ))
#print(dict1)
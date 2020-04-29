import re
'''from tkinter import *
from tkinter import filedialog
loki=Tk()

loki.withdraw()
file_path=filedialog.askopenfilename()'''

fo=open('/home/lokesh/Desktop/hhh.asm','r')
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
#print_adsdict()
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
                reg_dict[rq[s3-1][3:6]] = ads_dict[bket]

                s4 = s3;
                s3 = 0;
            elif(rq[s3-1][0:2]=="sw"):
                if(rq[s3-1][3:6] not in iso_list):
                    bket = rq[s3 - 1].rfind('(')
                    bket = int(rq[s3 - 1][7:bket]) + reg_dict[rq[s3 - 1][bket + 1:len(rq[s3 - 1]) - 1]]
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
                            print('yes')
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
#print(ads_dict)
#print(dict1)

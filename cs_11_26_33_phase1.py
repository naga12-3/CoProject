import re
from tkinter import *
from tkinter import filedialog
loki=Tk()

loki.withdraw()
file_path=filedialog.askopenfilename()

fo=open(file_path,'r')
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
ads_var = 0;
ads_dict = dict()
g1.remove(".data")
i = 0;
k1 = -1
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

while(pc<len(i)):
    if(i[pc][:6]=="jr $ra"):
        break;

    elif(i[pc][:2]=="li"):
        reg_dict[i[pc][3:6]] = int(i[pc][7:])
        pc = pc + 1
    elif(i[pc][:3]=="sub"):
        reg_dict[i[pc][4:7]] = reg_dict[i[pc][8:11]] - reg_dict[i[pc][12:15]]
        pc = pc + 1
    elif(i[pc][:1]=="j"):
        pc=loop_dict[i[pc][2:]+':'];

    elif(i[pc][:3]=="bne"):
         if (reg_dict[i[pc][4:7]] != reg_dict[i[pc][8:11]]):
            pc= loop_dict[i[pc][12:]+':']
         else:
            pc=pc+1
    elif(i[pc][:3]=="beq"):
        if (reg_dict[i[pc][4:7]] == reg_dict[i[pc][8:11]]):
            pc = loop_dict[i[pc][12:] + ':']
        else:
            pc = pc + 1
    elif(i[pc][:2]=="la"):
        reg_dict[i[pc][3:6]]=dict1[i[pc][7:]+":"]
        pc=pc+1
    elif(i[pc][:3]=="sll"):
        reg_dict[i[pc][4:7]]=reg_dict[i[pc][8:11]]*pow(2,int(i[pc][12:]))
        pc=pc+1
    elif(i[pc][:2]=="lw"):
        bket=i[pc].rfind('(')
        bket=int(i[pc][7:bket])+reg_dict[i[pc][bket+1:len(i[pc])-1]]
        reg_dict[i[pc][3:6]]=ads_dict[bket]
        pc=pc+1
    elif(i[pc][:2]=="sw"):
        bket = i[pc].rfind('(')
        bket = int(i[pc][7:bket]) + reg_dict[i[pc][bket + 1:len(i[pc])-1]]
        ads_dict[bket]=reg_dict[i[pc][3:6]]
        pc=pc+1
    elif(i[pc][:3]=="slt"):
        if (reg_dict[i[pc][8:11]] < reg_dict[i[pc][12:]]):
            reg_dict[i[pc][4:7]]=1
        else:
            reg_dict[i[pc][4:7]]=0
        pc=pc+1
    elif(i[pc][:4]=="addi"):
        reg_dict[i[pc][5:8]] = reg_dict[i[pc][9:12]] + int(i[pc][13:])
        pc=pc+1
    elif (i[pc][:3] == "add"):
        reg_dict[i[pc][4:7]] = reg_dict[i[pc][8:11]] + reg_dict[i[pc][12:15]]
        pc = pc + 1




print("printing  address and data stored")
for ine in sorted(ads_dict):
    print(hex(ine+4096)," :",ads_dict[ine])
print_reg()



loki1=Tk(className=' Simulator')
loki1.geometry("700x500+200+100")
loki1.configure()
l1=Label(loki1,text="Registers",font="12")
l1.place(x=15,y=20)
l2=Label(loki1,text="Address - Data",font="12")
l2.place(x=320,y=20)
frame=Frame(loki1)
frame.place(x=10,y=50)
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)
mylist =Listbox(frame, height=25,width=40,yscrollcommand=sb.set)

for i in reg_list:
    var=""
    var1=i[:11]
    var1=var1+str(reg_dict['$' + i[5:7]])
    mylist.insert(END,var1)

mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

frame1=Frame(loki1)
frame1.place(x=320,y=50)
sb1 = Scrollbar(frame1)
sb1.pack(side=RIGHT, fill=Y)
mylist1 =Listbox(frame1,height=25,width=60,yscrollcommand=sb1.set)
for i in sorted(ads_dict):
    y = hex(i + 4097)
    j=1
    if (type(ads_dict[i]) == type(j)):
        z = hex(ads_dict[i])
        z = '0' * (10 - len(z)) + z[2:]
    else:
        z = ""
        for k in ads_dict[i]:
            z = z + hex(ord(k))[2:]
        if(len(ads_dict[i])!=4):
            for d in range(4-len(ads_dict[i])):
                z="00"+z
    z=str(hex(i+4096))+"   :   "+z+"        "+str(ads_dict[i])

    mylist1.insert(END,z)
mylist1.pack(side=LEFT)
sb1.config(command=mylist1.yview)


loki1.mainloop()


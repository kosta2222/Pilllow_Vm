# Код для применения операций ко всем изображениям
# присутствует в папке один за другим
# операции, такие как вращение, обрезка,
# import PIL as pil
from PIL import Image, ImageFilter
import os
import numpy as np
from vm_print import b_c, console, vm_proc_print

make_filter=1
r=0
push_i=2
push_str=3
resize=4
L=5
push_fl=6
norm=7
pars=8
rot=9
rgb=10
filt_contour=11
filt_edge_enhance=12
readme=13
ops=["r","make_filter","push_i","push_str","resize","L","push_fl","norm","pars","rot","rgb","filt_contour","filt_edge_enhance","readme"]

console() # отладка
def main():
    b_c=[0]*40
    i=""
    splitted_cmd:list=['']*2
    main_cmd=''
    c=''
    par_cmd=''
    cmd_in_ops=''
    cn = -1
    exit_flag = False
    while True:
        print("Zdravstvuite ya sostavitel bait-coda dla etoi programmi,dla polnogo vihoda exit ")
        print("Dostupnie codi")
        for c in ops:
            print(c, end=' ')
        print()
        while True:
            i=input(">>>")
            if i=="r":
                break
            elif i=="exit":
                exit_flag = True
                break
            # Ищем код в списке In:i:str Out:b_c:list
            splitted_cmd_src=i.split()
            for cn1 in range(len(splitted_cmd_src)):
                splitted_cmd[cn1]=splitted_cmd_src[cn1]
            main_cmd=splitted_cmd[0]
            par_cmd=splitted_cmd[1]
            for c in range(len(ops)):
                cmd_in_ops=ops[c]
                if cmd_in_ops==main_cmd:
                    cn+=1
                    b_c[cn]=c
                    if par_cmd!='':
                        cn+=1
                        b_c[cn]=par_cmd
                # Очищаем
                splitted_cmd[0]=''
                splitted_cmd[1]=''
            cn+1
        if exit_flag == True:
            print("by-by!)")
            break
        vm_to_process_im(b_c)



def vm_to_process_im(b_c:list):
    ip=0
    sp=-1
    sp_str=-1
    sp_fl=-1
    steck=[0]*10
    steck_fl=[0.0]*10
    steck_str=['']*10
    op=0
    op=b_c[ip]
    while True:
        if op==push_i:
            sp+=1
            ip+=1
            steck[sp]=int(b_c[ip]) # Из строкового параметра
        elif op == push_fl:
            sp_fl += 1
            ip += 1
            steck_fl[sp_fl] = float(b_c[ip])  # Из строкового параметра
        elif op==push_str:
            sp_str+= 1
            ip += 1
            steck_str[sp_str] = b_c[ip]
        elif op==resize:
            # filter_=steck_str[sp_str]
            # sp_str-=1
            basewidth=steck[sp]
            sp-=1
            outPath=steck_str[sp_str]
            sp_str-=1
            inPath=steck_str[sp_str]
            sp_str-=1

            resize_(inPath,outPath,basewidth)
        elif op==L:
            outPath=steck_str[sp_str]
            sp_str-=1
            inPath=steck_str[sp_str]
            sp_str-=1

            l(inPath,outPath)
        elif op == norm:
            h=steck[sp]
            sp-=1
            w=steck[sp]
            sp-=1
            seed_=steck[sp]
            sp-=1
            scale=steck_fl[sp_fl]
            sp_fl-=1
            loc=steck_fl[sp_fl]
            sp_fl-=1
            outPath = steck_str[sp_str]
            sp_str -= 1

            normal_(outPath,loc,scale,seed_,w,h)
        elif op== pars:
            inPath=steck_str[sp_str]
            sp_str-=1
            pars_(inPath)
        elif op == rot:
            angle=steck[sp]
            sp-=1
            f_name=steck_str[sp_str]
            sp_str-=1
            outPath = steck_str[sp_str]
            sp_str -= 1
            inPath = steck_str[sp_str]
            sp_str -= 1

            rot_(inPath, outPath, f_name, angle)
        elif op == rgb:
            outPath = steck_str[sp_str]
            sp_str -= 1
            inPath = steck_str[sp_str]
            sp_str -= 1
            rgb_(inPath, outPath)
        elif op == filt_contour:
            outPath = steck_str[sp_str]
            sp_str -= 1
            inPath = steck_str[sp_str]
            sp_str -= 1

            filt_contour_(inPath,outPath)
        elif op == filt_edge_enhance:
            outPath = steck_str[sp_str]
            sp_str -= 1
            inPath = steck_str[sp_str]
            sp_str -= 1

            filt_edge_enhance_(inPath,outPath)
        elif op == readme:
            inPath = steck_str[sp_str]
            sp_str -= 1
            readme_(inPath)


        elif op == r:
            break
        else:
            print("Unknown byte-code",ops[op])
        ip+=1
        op = b_c[ip]

def readme_(inPath):
    from pathlib import Path
    f_n1="Readme.md"
    f_n2="desc.txt"
    f_n3="ver"
    f_n4=".gitignore"
    f_proj_fold=os.path.basename(inPath)
    msy64_etc_f_send=None
    f_n5="{0}_send.bash".format(f_proj_fold)
    for_cpu_inf=os.environ.get('PROCESSOR_ARCHITECTURE')+' '+ os.environ.get('PROCESSOR_ARCHITEW6432')
    with open(os.path.join(inPath,f_n1),"w",encoding='utf-8') as f1:
        read_info="""
<Имя программы>\n
=================
Описание:\n
Тестировалась на:\n
Предустановленные пакеты:\n
ОС:\n
CPU: {0}\n
RAM:\n
Дата:\n
Автор: Мухамеджанов Константин К.\n
Лицензия: As is\n
""".format(for_cpu_inf)
        f1.write(read_info)

    with open(os.path.join(inPath,f_n2),"w",encoding='utf-8') as f2:
        f2.write("Более подробное описание:")
    with open(os.path.join(inPath, f_n3), "w") as f3:
        f3.write("1.0")
    with open(os.path.join(inPath, f_n4), "w") as f4:
        f4.write(
""""
*.back
*.bac
*.bak
.idea/
venv/
__pycache__/
Makefile
build/
dist/
nbproject/""")
    # msy64_etc_f_send = f_n5

    # куда писать bash чтобы отправлять по ssh
    with open(os.path.join(inPath, f_n5), "w") as f5:
        f5.write(
"""cd ../home/msys_u/code/c/{0}
pwd
comm=$1
git add --all
git commit -m $comm
git push origin HEAD
""".format(f_proj_fold))
    vm_proc_print(b_c,locals(),globals())




def filt_edge_enhance_(inPath, outPath):
    l:list=None
    l=os.listdir(inPath)
    for imagePath in l:
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'filt_edge_enhance_' + imagePath)
        img=img.filter(ImageFilter.EDGE_ENHANCE)
        img.save(fullOutPath)
        print(fullOutPath)

def filt_contour_(inPath,outPath):
    l:list=None
    l=os.listdir(inPath)
    for imagePath in l:
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'filt_contour_' + imagePath)
        img=img.filter(ImageFilter.CONTOUR)
        img.save(fullOutPath)
        print(fullOutPath)

def rgb_(inPath:str, outPath:str):
    l:list=None
    l=os.listdir(inPath)
    for imagePath in l:
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'rgb_' + imagePath)
        img=img.convert(mode='RGB')
        img.save(fullOutPath)
        print(fullOutPath)

def rot_(inPath:str, outPath:str, f_name:str, angle:int):
    img=None
    inputPath=os.path.join(inPath, f_name)
    img = Image.open(inputPath)
    img = img.rotate(angle)
    fullOutPath = os.path.join(outPath, 'rotate_' + str(angle)+'_' + f_name)
    img.save(fullOutPath)
    print(fullOutPath)


def l(inPath:str,outPath:str):
    l:list=None
    l=os.listdir(inPath)
    for imagePath in l:
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'L_' + imagePath)
        img=img.convert(mode='L')
        img.save(fullOutPath)
        print(fullOutPath)


def resize_(inPath:str,outPath:str,basewidth,filter='.png'):
    ext=''
    ext=filter
    fullOutPath = None #  содержит полный путь (с именами файлов) к выводу
    img = None
    l:list=None
    l=os.listdir(inPath)
    for imagePath in l:#list(filter(lambda x: x[-3:]=='jpg',
                                # l)):
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        fullOutPath = os.path.join(outPath, 'resize_' + imagePath)
        # изображение, которое нужно сгенерировать
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(fullOutPath)
        print(fullOutPath)


def normal_(outPath:str,loc:float,scale:float,seed_:int,width,height):
    np.random.seed(seed_)
    size:tuple=None
    fullOutPath=""
    size_=(width,height)
    new_img=None
    fullOutPath=os.path.join(outPath,"Gaus_normal_loc_"+str(loc)+"_scale_"+str(scale)+"_seed_"+str(seed_)+".png")
    new_img=Image.fromarray(10*np.uint8(np.random.normal(loc,scale,size=size_)))
    new_img.save(fullOutPath)
    print(fullOutPath)

def pars_(inPath:str):
    l:list=None
    l=os.listdir(inPath)
    inputPath=''
    img=None
    width=0
    height=0
    f_size=0
    f_size_mb=0
    for imagePath in l:
        # imagePath содержит имя изображения
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        width=img.size[0]
        height=img.size[1]
        print("img name:",imagePath)
        print("img size: width =",width,"height =",height)
        f_size=os.path.getsize(inputPath)
        f_size_mb=f_size/(1024*1024)
        print("img Mb:",round(f_size_mb,3))
        print()


if __name__ == '__main__':
    main()
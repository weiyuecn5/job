"""
图片处理工具
"""
import time
from PIL import Image ,ImageDraw , ImageFont
import os

font = ImageFont.truetype("C:\Windows\Fonts\ARIALNI.TTF", 55)
font1 = ImageFont.truetype("C:\Windows\Fonts\ARIALNI.TTF", 180)
font2 = ImageFont.truetype("C:\Windows\Fonts\ARIALNI.TTF", 40)
font3 = ImageFont.truetype("C:\Windows\Fonts\ARIALNI.TTF", 130)

if os.path.exists('new')==False:
    os.makedirs('new')

def xishi():
    files = [d for d in os.listdir('截屏')]
    for file in files:
        print(file)
        pic=Image.open('截屏/'+file)
        draw = ImageDraw.Draw(pic)
        draw.text((95, 318),file[:-6], (255, 0, 0), font=font)
        new_pic=pic.crop((5,300,660,1080))
        w, h = new_pic.size
        new_pic.thumbnail((w // 2, h // 2))
        new_pic.save('new/'+file)
        os.remove('截屏/'+file)

def hebing():
    files = [d for d in os.listdir('截屏')]
    all_list=[] #所有编号的图片  需去重
    new_list=[] #从新组合的编号列表 类似 [[A1-1,A1-2,A1-3],[A2]]
    for file in files:
        if '-' in file:
            all_list.append(file.split('-')[0])
        else:
            all_list.append(file[:-4])
    all_list=list(set(all_list))

    for one in all_list:
        a_list=[]
        for file in files:
            if '-' in file and file.split('-')[0]==one:
                a_list.append(file)
            elif file==one+'.png':
                a_list.append(file)
        new_list.append(a_list)

    for i in new_list:
        if len(i)==1:
            pic=Image.open('截屏/'+i[0])
            draw = ImageDraw.Draw(pic)
            draw.text((100, 590),i[0][:-4], (255, 0, 0), font=font1)
            now_time = time.strftime("%Y/%m/%d", time.localtime())
            draw.text((450, 1120), now_time, (255, 0, 0), font=font)
            draw.text((10, 1120), 'wwvihs.cn', (255, 0, 0), font=font)
            w, h = pic.size
            pic.thumbnail((w // 2.5, h // 2.5))
            pic.save('new/'+i[0])
            # os.remove('截屏/'+i[0])
        elif 6<len(i)<=9:
            heng=3
            shu=3
            to_image = Image.new('RGB', (shu * 192, heng * 341) ) # 创建一个新图
            for y in range(1,heng+1):
                for x in range(1,shu+1):
                    try:
                        from_image = Image.open('截屏/' + i[shu * (y - 1) + x - 1]).resize(
                            (192, 341), Image.ANTIALIAS)
                        to_image.paste(from_image, ((x - 1) * 192, (y - 1) * 341))
                    except:
                        pass
            draw = ImageDraw.Draw(to_image)
            draw.text((100, 300), i[0][:-6], (255, 0, 0), font=font3)
            now_time = time.strftime("%Y/%m/%d", time.localtime())
            draw.text((380, 30), now_time, (255, 0, 0), font=font2)
            draw.text((10, 30), 'wwvihs.cn', (255, 0, 0), font=font2)
            to_image.save('new/'+i[0][:-6]+'.png')
        elif 3<len(i)<=6:
            heng=2
            shu=3
            to_image = Image.new('RGB', (shu * 192, heng * 341) ) # 创建一个新图
            for y in range(1,heng+1):
                for x in range(1,shu+1):
                    try:
                        from_image = Image.open('截屏/' + i[shu * (y - 1) + x - 1]).resize(
                            (192, 341), Image.ANTIALIAS)
                        to_image.paste(from_image, ((x - 1) * 192, (y - 1) * 341))
                    except:
                        pass
            draw = ImageDraw.Draw(to_image)
            draw.text((100, 270), i[0][:-6], (255, 0, 0), font=font3)
            now_time = time.strftime("%Y/%m/%d", time.localtime())
            draw.text((380, 30), now_time, (255, 0, 0), font=font2)
            draw.text((10, 30), 'wwvihs.cn', (255, 0, 0), font=font2)
            to_image.save('new/'+i[0][:-6]+'.png')
        elif 1<len(i)<=3:
            heng=1
            shu=3
            to_image = Image.new('RGB', (shu * 192, heng * 341) ) # 创建一个新图
            for y in range(1,heng+1):
                for x in range(1,shu+1):
                    try:
                        from_image = Image.open('截屏/' + i[shu * (y - 1) + x - 1]).resize(
                            (192, 341), Image.ANTIALIAS)
                        to_image.paste(from_image, ((x - 1) * 192, (y - 1) * 341))
                    except:
                        pass
            draw = ImageDraw.Draw(to_image)
            draw.text((100, 120), i[0][:-6], (255, 0, 0), font=font3)
            now_time = time.strftime("%Y/%m/%d", time.localtime())
            draw.text((380, 290), now_time, (255, 0, 0), font=font2)
            draw.text((10, 290), 'wwvihs.cn', (255, 0, 0), font=font2)
            to_image.save('new/'+i[0][:-6]+'.png')

hebing()

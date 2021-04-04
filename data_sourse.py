from math import log2

from PIL import Image
def open_image(fileName):
    im = Image.open(fileName)
    pix = im.load()
    num = []
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            p=pix[i,j]
            num.append(p[0])
            num.append(p[1])
            num.append(p[2])
    return num

def read_data(namefile):
    with open(namefile+'.bin', 'r') as f:
       return f.read()

def save_data_compression(data, fileName, length_word):
    list_pixes=[]
    colors=1
    for i in range(0,data.__len__()-1):
        power = length_word+int(log2(colors)+1) - 8
        colors = data[i]
        while(power>8):
            color=int(colors/(2**power))
            list_pixes.append(color)
            colors=colors%(2**power)
            power=power - 8
        data[i+1]+=colors*(2**length_word)
        itr=list_pixes.__iter__()
        im=Image
        im = Image.open(fileName)
        pix = im.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                try:
                    pix[i, j] = (list_pixes[itr.__next__()], list_pixes[itr.__next__()], list_pixes[itr.__next__()])
                except:
                    print("error")

        im.save("result.PNG")
    print(list_pixes)
#str(string).replace(',','').replace('[','').replace(']','')

def open_image2(fileName):
    im = Image.open(fileName)
    pix = im.load()
    length=im.size[0]
    width=im.size[1]
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix[i,j]=(255,0,255)
    im.save("result.PNG")



open_image2("test.PNG")
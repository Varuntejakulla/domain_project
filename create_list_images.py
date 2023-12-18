import glob
imglist =glob.glob("data/test/*.jpg",recursive=False)
with open("data/test.txt","w",encoding='utf-8')as f:
    for img in imglist:
        img = img.replace("\\","/")
        f.write(img+'\n')
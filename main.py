# Importing Image class from PIL module
from PIL import Image
import os
from pathlib import Path
from progress.bar import PixelBar
import argparse

def main():
    parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
    parser.add_argument('-i', '--image_path', type=str, help='carpeta de imagenes')
    #parser.add_argument('-b', '--numero_b', type=int, help='Parámetro b')
    parser.add_argument('-r', '--rescale',
                        type=str,
                        default='rescale', required=True,
                        help='rescalado')

    args = parser.parse_args()

    if args.rescale == 'rescale':
        
       subdirs(args.image_path)



def rescale(path,percent):
    #path de imagen ya reescalada
    respath = Path("res_images",path)
    
    save = Path(Path.cwd(),respath).with_suffix('.webp')

 

    image = Image.open(path)
    width, height = image.size
    new_image = image.resize((int(width/percent), int(height/percent)))
    

    new_image.save(save, format="webp")

    # print(image.size) # Output: (1920, 1280)
    # print(new_image.size) # Output: (400, 400)

def listdir(filess):
    bar = PixelBar('Processing', max=filess)
    for path in Path("images").glob("**/*.*"):
        
        rescale(path,2)
        bar.next()
    bar.finish()



def subdirs(root):
    # root = "images"
    print(root)
    saved = "res_images\\"+root
    filess=0
    
    for path in Path(root).glob("**/*.*"):
        filess+=1
    print(filess)
    for path, subdirs, files in os.walk(root):
        for name in subdirs:
            subdir = os.path.join(saved, name)
            for name in files: 
                try:
                     os.makedirs(subdir)
                except FileExistsError:
                    pass
    
    listdir(filess)
    
main()   

    
    # listdir(filess)
# list files of a directory

   



# subdirs()




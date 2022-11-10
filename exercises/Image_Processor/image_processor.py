
from PIL import Image,ImageEnhance,ImageFilter
import os

before_path= 'exercises\Image_Processor\Before'
after_path= 'exercises\Image_Processor\After'


def edit_pics():
  for files in os.listdir(before_path):
    img= Image.open(f"{before_path}/{files}")
    edit= img.filter(ImageFilter.SHARPEN) 
    final_name= os.path.splitext(files)[0] 
    return edit.save(f".{after_path}/{final_name}_edited.jpegx")


edit_pics()
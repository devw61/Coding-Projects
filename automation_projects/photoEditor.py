from PIL import Image, ImageEnhance, ImageFilter
import os


#check local file
path = "/Users/devin_wingfield/coding projects/images/" 
#check photo librarys
# path = "/Users/devin_wingfield/Pictures/photo_library_vscode"
pathOut = "/Users/devin_wingfield/coding projects/images/"

# input_filename = input("enter filename output(with file type): ")
input_filename = "3FBED0C9-5397-4E17-858A-7DECF488F0AF_1_105_c.jpeg"

#check if file exists
try:
    img = Image.open(f'{path}/{input_filename}')
    print(f"found file {input_filename}")
except IOError:
    print(f"unable to find file: {input_filename}")
    quit()

#check if file type is universally supported (for funsies)
file_type = os.path.splitext(input_filename)[1]
file_name = os.path.splitext(input_filename)[0] 
formate_types = '.png', '.jpg', '.jpeg', '.bmp', '.dds', '.gif', '.tiff', '.tif'
file_format_detector = file_type.lower().endswith(formate_types)
if file_format_detector == False :
    print("WARNING: file type is not universally supported")

# if you want to make it universal
# while file_format_detector == False :
#     input_filename = input(f"enter a valid file format {formate_types}: ")
#     file_type = os.path.splitext(input_filename)[1]
#     file_format_detector = file_type.lower().endswith(formate_types)
        
#edit the file to make black and white, sharppen, rotate, and increase contrast
edit = img.filter(ImageFilter.SHARPEN)
factor = 1.5
enhancer = ImageEnhance.Contrast(edit)
edit = enhancer.enhance(factor)

# crop the file
# right(width) > left(how much cropped from left) and bottom > top (same thing but vertical respectively)
# left = 100
# top = 10
# right = 500
# bottom = 700
# edit = edit.crop((left, top, right, bottom))

# save to designated folde
# edit.save(f'{pathOut}/image_edited.jpg')
edit.save(f'{pathOut}/{file_name}_edited{file_type}')
print(input_filename, "has been edited and saved in:", pathOut)
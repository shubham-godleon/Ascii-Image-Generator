The code description is here. But first thanks to the EzSnippet guy aka Neeraj Walia. I saw his project on rust and successfully implemented it in python.
 
- First things first: Imported PIL or Pillow (install using: pip install Pillow in your terminal)
- then imported the image using Image from PIL
- converted it to grayscale image.convert("L")
- resize the image as per your need
- I have put in the ascii chararacters as per the density of them and their appearance visually "#$%@&!/+=*^-;,'. " like # being the most dense and ' ' space being the least. (but the string is reversed).
- run a for nested loop on height and width and for each y and x respectively, get the image pixel intensity using image.getpixel   which varies from 0 to 255.
- ascii_chars[int(pixel_intensity * len(ascii_chars) / 256)] choosing the ascii character is easier according to the length of the string the stronger the intensity the denser the character. (as the string is reversed)
(I know i could have just input the correct string but I am lazy so...)
- anyways that's all.

Happy Coding !
GodleoN

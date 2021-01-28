from openpyxl import load_workbook
from io import BytesIO

import requests
from openpyxl.drawing.image import Image

wb = load_workbook('baza_test.xlsx')
all_sectors = wb.active


for i in range(3,11):
        response = requests.get(all_sectors['M'+ str(i)].value)
        img = Image(BytesIO(response.content))
        all_sectors.add_image(img, 'N'+ str(i))
  

wb.save("baza_with_img.xlsx")

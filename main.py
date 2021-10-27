from pdf2image import convert_from_path
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'
import re

paths = []
i=0
for i in range(10):
    st = 'C:\\Users\\jayzo\\PycharmProjects\\DS_week1_proj1\\PDFs\\in' + str(i) + '-converted.pdf'
    paths.append(st)
    img = convert_from_path(paths[i], 400,
                             poppler_path="C:\\Users\\jayzo\\Downloads\\poppler-0.68.0_x86\\poppler-0.68.0\\bin" )
    for p in img:
        strr = 'im'+str(i)+'.jpg'
        p.save(strr,'JPEG')
        i = i+1

images_cv = []
for k in range(10):
    stn = "C:\\Users\\jayzo\\PycharmProjects\\DS_week1_proj1\\im"+str(k)+'.jpg'
    images_cv.append(cv2.imread(stn))

clean_images = []
text = []
for m in range(10):
    oneimg = images_cv[m]
    gray_img = cv2.cvtColor(oneimg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresh = cv2.GaussianBlur(thresh, (5, 5), 0)
    clean_images.append(thresh)
    text.append(pytesseract.image_to_string(thresh))

result_num =[]
result_total=[]
for o in range(10):
    match_num =[]
    match_tot =[]
    text_fin = text[o]
    numbers = re.compile(r"[-+]?\d*\.\d+|\d+")
    matches1 = numbers.finditer(text_fin)
    total_var = re.compile('total',re.IGNORECASE)
    matches2 = total_var.finditer(text_fin)

    for match in matches1:
        match_num.append(match)

    for match in matches2:
        match_tot.append(match)

    result_num.append(match_num)
    result_total.append(match_tot)


for t in range(10):
    print(result_num[t])
    print(result_total[t])
    print("++++++++++++++++++++++")
from pdfminer import high_level
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pathlib import Path
import tabula
import pandas as pd
from os import listdir

merger = PdfFileMerger()
mergelist = []

# length of window from right side of page
winr = float(input('how big do you want the read window from the right side of the page? ---> '))


# length of window down from top of page
wint = float(input('how big do you want the read window from the top of the page? ---> '))



def croppedWindow(winr,wint):
    winr = winr
    wint = wint
    # length in points
    winr_pts = winr * 72
    # length in points
    wint_pts = wint * 72
    # get actual size of page
    pgsize = pgread.mediaBox
    # if page is 11x17
    if pgsize[2] == 1224:
        # gets current dimension of upper right corner of document
        pgread1 = pgread.mediaBox.upperRight
        # subtracts user offset from upper right horizontal coordinate
        win_r = pgread1[0] - winr_pts
        # subtracts user offset from upper right vertical coordinate
        win_t = pgread1[1] - wint_pts
        # sets upper left edge of cropped window
        pgread.mediaBox.upperLeft = (win_r, pgsize[3])
        # sets lower left edge of cropped window
        pgread.mediaBox.lowerLeft = (win_r, win_t)
    # if page is 24x18
    elif pgsize[2] == 1728:
        win_r2 = winr * 1.65
        winr_pts = win_r2 * 72
        win_t2 = wint * 1.85
        wint_pts = win_t2 * 72
        # gets current dimension of upper right corner of document
        pgread1 = pgread.mediaBox.upperRight
        # subtracts user offset from upper right horizontal coordinate
        win_r2 = pgread1[0] - winr_pts
        # subtracts user offset from upper right vertical coordinate
        win_t2 = pgread1[1] - wint_pts
        # sets upper left edge of cropped window
        pgread.mediaBox.upperLeft = (win_r2, pgsize[3])
        # sets lower left edge of cropped window
        pgread.mediaBox.lowerLeft = (win_r2, win_t2)
    # if page is 36x24
    elif pgsize[2] == 2592:
        win_r2 = winr * 2.45
        winr_pts = win_r2 * 72
        win_t2 = wint * 2.55
        wint_pts = win_t2 * 72
        # gets current dimension of upper right corner of document
        pgread1 = pgread.mediaBox.upperRight
        # subtracts user offset from upper right horizontal coordinate
        win_r2 = pgread1[0] - winr_pts
        # subtracts user offset from upper right vertical coordinate
        win_t2 = pgread1[1] - wint_pts
        # sets upper left edge of cropped window
        pgread.mediaBox.upperLeft = (win_r2, pgsize[3])
        # sets lower left edge of cropped window
        pgread.mediaBox.lowerLeft = (win_r2, win_t2)
    # if page is any other size than the two above
    else:
        pass

def dataFrame():
    tabula.io.convert_into("C:/users/brock/documents/GitHub/PDF_Text/cropped_pages.pdf", "C:/users/brock/documents/GitHub/PDF_Text/cropped_pages.csv", output_format="csv",
                            lattice=True, pages="all")


pdf_path = (
    Path.home()
    / "documents"
    / "sales"
    / "civica es"
    / "civica - for fabrication.pdf"
)

# pdf file input
pdf_input = PdfFileReader(str(pdf_path))
# get number of pages in pdf file
pgnum = pdf_input.getNumPages()
print('there are',pgnum,'pages in this file')
# for loop to go through all pages of pdf file
pgread = pdf_input.getPage(1)
croppedWindow(winr,wint)
pdf_writer = PdfFileWriter()
pdf_writer.addPage(pgread)
with Path("cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
num = 1
while num != pgnum:
    # read certain page of pdf file
    pgread = pdf_input.getPage(num)
    croppedWindow(winr,wint)
    npgread = str("cropped_pages" + str(num) + ".pdf")
    mergelist.append(npgread)
    pdf_writer.addPage(pgread)
    with Path("cropped_pages.pdf").open(mode="wb") as output_file:
        pdf_writer.write(output_file)
    num += 1

else:
    pass

print('The contents of mergelist variable', mergelist)
print('Your cropped pages file is ready')
print('generating dataframe')
dataFrame()

























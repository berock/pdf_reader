# pdf_reader
pdf drawing reader with tabula. 
Capture a portion of pdf and convert the text to .csv file.

# user inputs
(first prompt) 'how big do you want the read window from the right side of the page? ---> '
- This is the dimension from the far right of the page that sets the left edge of the capture window. 
- object type : float

(second prompt) 'how big do you want the read window from the top of the page? ---> '
- This is the dimension from the far top of the page that sets the bottom edge of the capture window.
- object type : float

# page sizes 
- 11x17 landscape
- 24x18
- 36x24

# functionality
- takes original pdf document
- crops dacument to user selected window size
- creates "cropped_file"
- appends all pages to "cropped_file"
- tabula runs on cropped file to create .csv file

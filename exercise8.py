from PyPDF2 import PdfWriter
from os import path, mkdir, listdir

demo_folder = "./res/exercise8/demo"
out_folder = "./res/exercise8/out"

try:
    mkdir(out_folder)
except:
    pass

merged_file = path.normpath(path.join(out_folder, "merged.pdf"))
list_of_pdf = [(file) for file in listdir(demo_folder) if file.endswith(".pdf")]

merger = PdfWriter()

for file in list_of_pdf:
    pdf_path = path.normpath(path.join(demo_folder, file))
    merger.append(pdf_path)

merger.write(merged_file)
merger.close()
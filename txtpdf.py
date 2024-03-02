import glob
from fpdf import FPDF
from pathlib import Path
import pandas as pd

filepaths = glob.glob("files/*txt")

pdf = FPDF(orientation='P', unit="mm", format="A4")

for filepath in filepaths:
    f = open(filepath)
    pdf.add_page()
    filename = Path(filepath).stem
    print(filename)
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=20, h=10, txt=filename, ln=1, border=1)
    pdf.set_font(family="Arial", size=12, style="")
    pdf.multi_cell(w=0, h=12, txt=f.read(), border=1)

pdf.output("pdf-out.pdf")

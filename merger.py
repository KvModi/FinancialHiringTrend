from PyPDF2 import PdfFileMerger
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
#rel_path = "venv/processed_text.txt"
#abs_file_path = os.path.join(script_dir, rel_path)

pdfs = ['Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services.pdf', 'WEF_A_Blueprint_for_Digital_Identity.pdf', 'WEF_The_future__of_financial_services.pdf', 'WEF_The_future_of_financial_infrastructure.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    pathpdf=os.path.join(script_dir, pdf)
    merger.append(open(pathpdf, 'rb'))
    print("Merged",pdf)

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
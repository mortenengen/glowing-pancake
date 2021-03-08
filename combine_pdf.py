import PyPDF2

pdfs = [
    # 'C219-KV-Q-CA-00001 - MAIN.pdf',
    'C219-KV-Q-CA-00001 - General. Structural Global Analysis and Load Specification Report.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 1.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 2.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 3.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 4.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 5.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 6.pdf',
    'C219-KV-Q-CA-00001 - APPENDIX 7.pdf'
    ]

pdfname = 'C219-KV-Q-CA-00001_COMPLETE.pdf'

pdf_merger = PyPDF2.PdfFileMerger()

for this_pdf in pdfs:
    pdf_merger.append(this_pdf)

pdf_merger.write(pdfname)
pdf_merger.close()
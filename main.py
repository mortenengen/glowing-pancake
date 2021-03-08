import os
import subprocess

import PyPDF2

files_to_convert = []
pdf_files = ['FEM006.pdf', 'FEM007.pdf']

files = os.listdir()
for thisfile in files:
    if thisfile.endswith('.eps'):
        files_to_convert.append(thisfile)

config = {
    'inkscape':{
        'path':'C:\\Program Files\\Inkscape\\bin\\inkscape.exe'
        },
    'convert_several_ps':{
        'run':False,
        'files':files_to_convert,
        'format':'emf',
        'out_dpi':400
        },
    'combine_pdfs':{
        'run':True,
        'pdfs':pdf_files,
        'outfile':'combined_pdf.pdf'
        }
    }

def ps_to_pdf(psfile):
    """
    """
    filename = psfile[:psfile.index('.')]
    outfile = filename + '.pdf'
    arguments = ['ps2pdf', psfile, outfile]
    run_status = subprocess.run(arguments)
    return run_status

def pdf_convert(pdffile, outformat, outdpi=300):
    """
    """
    pdf_in = PyPDF2.PdfFileReader(open(pdffile, 'rb'))
    num_pages = pdf_in.numPages
    pages = []
    file_first_name = None
    if 'pdf' in pdffile:
        file_first_name = pdffile[:pdffile.index('.pdf')]
    elif 'PDF' in pdffile:
        file_first_name = pdffile[:pdffile.index('.PDF')]
    
    # Split pdf
    for page in range(num_pages):
        pages.append(file_first_name + f'_p_{page}')
        pdf_out = PyPDF2.PdfFileWriter()
        pdf_out.addPage(pdf_in.getPage(page))
        stream = open(pages[-1] + '.pdf', 'wb')
        pdf_out.write(stream)
        stream.close()
    
    # Convert each page
    run_status = None

    for page in [pages[this_page] for this_page in range(num_pages)]:
        arguments = []
        arguments.append(config['inkscape']['path'])
        arguments.append(f'--export-type={outformat}')
        if outformat.lower() == 'png':
            arguments.append(f'--export-dpi={outdpi}')
        arguments.append(f'{page}.pdf')
        run_status = subprocess.run(
            arguments
            , creationflags=subprocess.CREATE_NEW_CONSOLE
            )
    
    # Delete split pages
    for page in pages:
        pagename = page + '.pdf'
        if pagename in os.listdir():
            os.remove(pagename)

    return run_status

def combine_pdfs():
    """
    """
    pdf_merger = PyPDF2.PdfFileMerger()

    for this_pdf in config['combine_pdfs']['pdfs']:
        pdf_merger.append(this_pdf)
    
    pdf_merger.write(config['combine_pdfs']['outfile'])
    pdf_merger.close()

    return

def convert_several_ps():
    """
    """
    infiles = config['convert_several_ps']['files']

    for psfile in infiles:
        psfirstname = psfile[:psfile.index('.')]
        pdffile = psfirstname + '.pdf'
        if 'out_dpi' in config['convert_several_ps'].keys():
            out_dpi = config['convert_several_ps']['out_dpi']
        else:
            out_dpi = None
        print(f'Start converting {psfile}')
        ps_to_pdf(psfile)
        print(f'PS converted to PDF, start converting {pdffile}')
        pdf_convert(
            pdffile,
            config['convert_several_ps']['format'],
            outdpi=out_dpi
            )
        print('Finished converting PDF')
        
    return

if config['convert_several_ps']['run']:
    convert_several_ps()

if config['combine_pdfs']['run']:
    combine_pdfs()
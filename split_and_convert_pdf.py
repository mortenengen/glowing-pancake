import PyPDF2
import subprocess
import os

config = {
    'file_to_convert': 'css_pt_t0.pdf',
    'out_format':'emf',
    'out_dpi':650
}

pdf_in = PyPDF2.PdfFileReader(open(config['file_to_convert'],'rb'))
pages = []
# pages_to_print = [109, 110, 111]
pages_to_print = list(range(10))

if 'pdf' in config['file_to_convert']:
    file_first_name = config['file_to_convert'][:config['file_to_convert'].index('.pdf')]
elif 'PDF' in config['file_to_convert']:
    file_first_name = config['file_to_convert'][:config['file_to_convert'].index('.PDF')]

for page in range(pdf_in.numPages):
    pages.append(file_first_name+'_p_{}'.format(page))
    pdf_out = PyPDF2.PdfFileWriter()
    pdf_out.addPage(pdf_in.getPage(page))
    stream = open(pages[-1]+'.pdf','wb')
    pdf_out.write(stream)
    stream.close()

# for page in pages:
for page in [pages[this_page] for this_page in pages_to_print]:
    arguments = []
    arguments.append('C:\\Program Files\\Inkscape\\inkscape.exe')
    arguments.append('-f={}.pdf'.format(page))
    arguments.append('--export-{1}={0}.{1}'.format(page,config['out_format']))
    # arguments.append('--export-type=\"{}\"'.format(config['out_format']))
    if config['out_format'] is 'png':
        arguments.append('--export-dpi={}'.format(config['out_dpi']))
    # arguments.append('{}.pdf'.format(page))
    # argument_string = ' '.join(arguments)
    run_status = subprocess.run(arguments,creationflags=subprocess.CREATE_NEW_CONSOLE)
    # print(run_status)

for page in pages:
    if page + '.pdf' in os.listdir():
        os.remove(page + '.pdf')
import io
import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
def extract_text_from_pdf(pdf_files):
    # resource_manager = PDFResourceManager()
    # fake_file_handle = io.StringIO()
    # converter = TextConverter(resource_manager, fake_file_handle)
    # page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    for PDF_file in pdf_files:
        
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        with open(PDF_file, 'rb') as fh:
            for page in PDFPage.get_pages(fh, 
                                        caching=True,
                                        check_extractable=True):
                page_interpreter.process_page(page)
    
            text = fake_file_handle.getvalue()
        # close open handles
        
        
        # file = open("text1.txt")
        output_file = PDF_file[:-4]
        output_file_name = os.path.join(output_file + ".txt")
        f = open(output_file_name, "a")
        for line in text.split(". "):
            if ("GOODWILL AND OTHER INTANGIBLE ASSETS" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if ("GOODWILL AND OTHER" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if ("ACQUISITION" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if("BUSINESS COMBINATION" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if("DIVESTITURE" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if ("GOODWILL AND OTHER" in line.upper()):
                # print(line)
                f.write(line)
                f.write("\n")
            if("ACQUISITIONS" in line.upper()):
                # print(line)       
                f.write(line)
                f.write("\n")

        f.close()
    # if text:
    #     return text
        converter.close()
        fake_file_handle.close()
        text = ""
 
if __name__ == '__main__':
    # print(
    # extract_text_from_pdf('AGCO CORP  DE_2009-02-27_10-K.pdf')
    files = [f for f in os.listdir('/Users/shikhashah/Desktop/')  if ((f.endswith('.pdf')) or (f.endswith('.pdf')))]
    extract_text_from_pdf(files)
    # print(files)
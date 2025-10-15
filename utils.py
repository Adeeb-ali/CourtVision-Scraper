import os
import requests
from pylatex import Document, Section, Tabular, Command, NoEscape

LATEX_DIR = "cause_lists/latex/"
PDF_DIR = "cause_lists/pdfs/"

def save_case_latex_table(case_data_list, filename):
   
    os.makedirs(LATEX_DIR, exist_ok=True)
    doc = Document()
    doc.preamble.append(Command('title', 'Case Details'))
    doc.preamble.append(Command('author', 'eCourts Scraper'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Cases')):
        if not case_data_list:
            doc.append("No cases found or invalid CNR.")
        else:
            with doc.create(Tabular('|l|l|l|l|l|')) as table:
                table.add_hline()
                table.add_row(["CNR", "Serial", "Court Name", "Status", "PDF Link"])
                table.add_hline()
                for case in case_data_list:
                    table.add_row([
                        case.get('cnr', 'N/A'),
                        case.get('serial', 'N/A'),
                        case.get('court_name', 'N/A'),
                        case.get('status', 'N/A'),
                        case.get('pdf_link', 'N/A')
                    ])
                    table.add_hline()

    tex_path = os.path.join(LATEX_DIR, filename)
    doc.generate_tex(tex_path.replace('.tex',''))
    print(f"[INFO] LaTeX file created: {tex_path}")


def download_case_pdf(pdf_url, filename):
   
    os.makedirs(PDF_DIR, exist_ok=True)
    try:
        response = requests.get(pdf_url)
        if response.status_code == 200:
            path = os.path.join(PDF_DIR, filename)
            with open(path, "wb") as f:
                f.write(response.content)
            print(f"[INFO] Case PDF downloaded: {path}")
        else:
            print("[WARN] PDF not available")
    except Exception as e:
        print(f"[ERROR] Failed to download PDF: {e}")

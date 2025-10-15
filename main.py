import argparse
from scraper import ECourtsScraper
from utils import save_case_latex_table, download_case_pdf

def main():
    parser = argparse.ArgumentParser(description="eCourts Scraper CLI")
    parser.add_argument("--cnr", help="Enter CNR Number", required=True)
    args = parser.parse_args()

    scraper = ECourtsScraper()
    scraper.open_site()
    scraper.search_case(args.cnr)

    cases = scraper.get_all_case_details()
    for case in cases:
        case['cnr'] = args.cnr

    print("[INFO] Cases Found:", cases)

    save_case_latex_table(cases, f"{args.cnr}_cases.tex")

    for i, case in enumerate(cases):
        if case.get("pdf_link") and case["pdf_link"] != "N/A":
            download_case_pdf(case["pdf_link"], f"{args.cnr}_case_{i+1}.pdf")

    scraper.close()

if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import csv
import sys
from typing import List, Dict

from pubmed_fetcher.pubmed_fetcher import fetch_pubmed_ids, fetch_paper_details


def save_to_csv(results: List[Dict[str, str]], filename: str):
    """
    Saves the fetched research papers to a CSV file.
    
    Args:
        results (List[Dict[str, str]]): List of research papers.
        filename (str): File path to save the CSV.
    """
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, nargs="?", help="Search query for PubMed.", default="cancer")
    parser.add_argument("-f", "--file", type=str, help="File to save results (CSV).", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    
    pubmed_ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"Fetched {len(pubmed_ids)} PubMed IDs.")

    paper_details = fetch_paper_details(pubmed_ids)
    if args.debug:
        print(f"Fetched details for {len(paper_details)} papers.")

    if args.file:
        save_to_csv(paper_details, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in paper_details:
            print(paper)

if __name__ == "__main__":
    main()


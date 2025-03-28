#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load API Key from environment or fallback to a default
load_dotenv()
API_KEY = os.getenv("PUBMED_API_KEY", "603df8e40542005810c8f6ec178cd9105d08")
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str, max_results: int = 50) -> List[str]:
    """
    Fetches PubMed IDs for a given query.
    
    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to fetch.

    Returns:
        List[str]: List of PubMed IDs.
    """
    url = f"{BASE_URL}esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "api_key": API_KEY,
        "retmode": "json"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PubMed IDs: {e}")
        return []

def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict[str, Optional[str]]]:
    """
    Fetches details of research papers given a list of PubMed IDs.
    
    Args:
        pubmed_ids (List[str]): List of PubMed IDs.

    Returns:
        List[Dict[str, Optional[str]]]: List of dictionaries containing paper details.
    """
    if not pubmed_ids:
        return []
    
    url = f"{BASE_URL}esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "api_key": API_KEY,
        "retmode": "json"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        results = []
        for pmid in pubmed_ids:
            paper = data.get("result", {}).get(pmid, {})
            results.append({
                "PubmedID": pmid,
                "Title": paper.get("title", "Unknown"),
                "Publication Date": paper.get("pubdate", "Unknown"),
                "Non-academic Author(s)": "",  # To be extracted
                "Company Affiliation(s)": "",  # To be extracted
                "Corresponding Author Email": ""  # Not directly available in summary
            })
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper details: {e}")
        return []


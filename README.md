# Pubmedapi
Objective
Create a Python package (pubmed-fetch-api) that fetches PubMed papers.

Structure the project correctly for packaging and distribution.

Use Poetry for dependency management and publishing.

Publish the package to PyPI.

Use the package via CLI and as a Python module.

Initialize Poetry
Poetry is used to manage dependencies and build the package.

Navigate to the project folder:
cd pubmed-fetch-api

Initialize Poetry:
poetry init

It will ask for details like package name, version, description, etc.
Provide appropriate values and finish the setup.

Configure pyproject.toml
Implement the Package
pubmed_fetcher.py (Main Module)
This file contains the logic for fetching papers from PubMed.

fetch_papers.py (CLI Script)
This script allows users to fetch papers from the command line.

Build the Package
poetry build
This will create a .tar.gz and .whl file in the dist/ folder.

Publish to PyPI
poetry publish --build -u __token__ -p YOUR_PYPI_TOKEN

Install and Test the Package
pip install pubmed-fetch-api

Use the CLI Tool
get-papers "COVID-19"
This should fetch PubMed papers and save the results to output.csv.
✅ Configured pyproject.toml correctly
✅ Implemented a CLI tool (get-papers)
✅ Published the package to PyPI
✅ Successfully installed and tested it

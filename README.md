# nubank-report
Scrape Nubank desktop version of website to download your credit card expenses as a pandas DataFrame

### Requirements
`BeautifulSoup`, `pandas`

### How To
Open your dashboard in Nubank's website, make sure to select the appropriate time window.
Download the HTML file and run `python nubank_parse.py [your-html-file]`. This will generate a `nubank.csv` with your purchases using your credit card. 
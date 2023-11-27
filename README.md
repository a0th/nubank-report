# nubank-report
Scrape [Nubank](https://nubank.com.br/) desktop version of website to download your credit card expenses as a pandas DataFrame

> [!IMPORTANT]
> Nubank re-designed their website and this script is no longer working. I will update it as soon as I have time.


### Requirements
`BeautifulSoup`, `pandas`

### How To
Open your dashboard in Nubank's website, make sure to select the appropriate time window.
Download the HTML file and run `python nubank_parse.py [your-html-file]`. This will generate a `nubank.csv` with your purchases using your credit card. 
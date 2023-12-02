import tools.csv_exporter as exporter
import tools.data_cleaner as cleaner
import tools.webpage_scraper as scraper


ENABLE_SCRAPING = 1
ENABLE_CLEANING = 1
ENABLE_EXPORTING = 1


urls = ["https://www.thewholesaler.biz/Cardstock"]

for url in urls:
    if ENABLE_SCRAPING:
        data = scraper.scrape_webpage(url)
    if ENABLE_CLEANING:
        data = cleaner.clean_data(data)
    if ENABLE_EXPORTING:
        exporter.export_to_csv(data)

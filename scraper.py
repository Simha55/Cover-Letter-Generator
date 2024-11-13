from selenium import webdriver
from bs4 import BeautifulSoup
from utils import TextProcessor
import time

class JobDescriptionScraper:
    def __init__(self, url):
        self.url = url

    def scrape_job_description(self):
        """
        Scrape job description from the given URL.
        """
        # Initialize Chrome options with headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode (no browser window)
        options.add_argument('--no-sandbox')  # Disable sandbox for compatibility
        options.add_argument('--disable-dev-shm-usage')  # Avoid issues in Docker environments
        options.add_argument('--remote-debugging-port=9222')  # Debugging port (optional)
        options.add_argument('--disable-software-rasterizer')  # Disable GPU rasterizer

        # Now instantiate the driver with the configured options
        driver = webdriver.Chrome(options=options)
        
        try:
            # Open the job URL
            driver.get(self.url)

            # Wait for content to load (can be adjusted depending on the page's load speed)
            time.sleep(5)

            # Get page content and parse it with BeautifulSoup
            page_content = driver.page_source
            soup = BeautifulSoup(page_content, 'html.parser')
        finally:
            # Ensure the driver is properly closed
            driver.quit()

        # Process and return the scraped job description
        processor = TextProcessor(soup.get_text())
        return processor.preprocess_text()

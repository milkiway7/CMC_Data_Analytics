import logging
from abc import ABC, abstractmethod

class DataScrapingBase(ABC):
    def __init__(self, headless=False,proxy=None):
        self.headless = headless
        self.proxy = proxy
        self.browser = None
        

    async def launch_browser(self, playwright):
        try:
            logging.info("Launching browser playwright")
            browser_options = {"headless": self.headless}
            if self.proxy:
                browser_options["proxy"] = self.proxy
            self.browser = await playwright.chromium.launch(**browser_options)
        except Exception as e:
            logging.error(f"Error: Launching browser failed {e}")
            return None
        
    async def create_page(self):
        try:
            logging.info("Creating page")
            if not self.browser:
                raise Exception("Browser not launched")
            self.page = await self.browser.new_page()
            return self.page
        except Exception as e:
            logging.error(f"Error: Creating page failed {e}")
            return None
    
    async def go_to_url(self,url):
        try: 
            if not self.page:
                raise Exception("Page not created")
            await self.page.goto(url)
        except Exception as e:
            logging.error(f"Error: Going to url failed {e}")
    
    async def close_browser(self):
        try:
            logging.info("Closing browser")
            if self.browser:
                await self.browser.close()
        except Exception as e:
            logging.error(f"Error: Closing browser failed {e}")

    @abstractmethod
    async def log_in():
        pass
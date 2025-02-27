from Modules.DataScraping.DataScrapingBase import DataScrapingBase
import logging
from playwright.async_api import async_playwright
from Modules.DataScraping.scraping_constants import DATA_SCRAPING_X
import time

class ScrapingModule(DataScrapingBase):
    def __init__(self, headless=False,proxy=None):
        super().__init__(headless,proxy)

    async def scrape_protal_x(self, url):
        try:
            async with async_playwright() as playwright:
                await self.launch_browser(playwright)
                await self.create_page()
                await self.go_to_url(url)
                await self.log_in()
                await self.go_to_profile()
        except Exception as e:
            logging.error(f"Scraping failed: {e}")
        finally:
            await self.close_browser()

    async def log_in(self):
        try:
            await self.page.fill("input[name='text']", "EMAIL")
            await self.page.get_by_text("Dalej").click()
            user_name = self.page.locator("span:text['Wprowadź swój numer telefonu lub nazwę użytkownika']")
            if user_name.is_visible():
                await self.page.fill("input[type='text']", "USER_NAME")
                await self.page.get_by_text("Dalej").click()
            await self.page.fill("input[name='password']", "PASSWORD")
            await self.page.get_by_text("Zaloguj się").click()
        except Exception as e:
            logging.error(f"Log in failed to X portal: {e}")

    async def go_to_profile(self):
        scraped_profiles = 0
        for profile in DATA_SCRAPING_X["profiles"]:
            try:
                time.sleep(3)
                # await self.page.wait_for_load_state("networkidle")
                await self.go_to_url("https://x.com/CmC2025CmC")
                await self.page.get_by_text("Following").click()
                
                elements = self.page.locator("span",has_text=f"{profile}")
                time.sleep(2)
                count = await elements.count()
                if count > 1:
                    await elements.nth(0).click()
                else:
                    await self.page.get_by_text(profile).click()
                scraped_profiles += 1
            except Exception as e:
                logging.error(f"Go to profile '{profile}' failed: {e}")
        
        if scraped_profiles == len(DATA_SCRAPING_X["profiles"]):
            logging.info("All profiles scraped successfully")
import asyncio
from playwright.async_api import async_playwright


class BrowserAutomation:

    def __init__(self, url):
        """Initialize internal state variables."""
        self.url = url
        self._playwright = None
        self._browser = None
        self.page = None

    async def start(self, headless: bool = False) -> None:
        """Launch Playwright instance and open a new page."""
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(headless=False)
        self.page = await self._browser.new_page()

    async def navigate(self) -> None:
        """Load the specified page URL."""
        if not self.page:
            raise RuntimeError(
                "Browser session is not started. Call start() first."
            )
        await self.page.goto(self.url)

    async def stop(self) -> None:
        """Close browser context and terminate Playwright instance."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()

async def main():
    bot = BrowserAutomation( url = "https://example.com")
    await bot.start()
    await bot.navigate()
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())
    

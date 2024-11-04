import webbrowser
from json import load

class GoogleSearchExecutor:
    def __init__(
            self, 
            config_file: str="sites.json",
            chrome_path: str="C:/Program Files/Google/Chrome/Application/chrome.exe"
            ):
        
        self.base_url = "https://www.google.com/search?q="
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        self._load_sites(config_file)

    def open_search(self, query):
        """
        Открывает Chrome с поисковым запросом в Google.

        :param query: Поисковый запрос.
        """
        search_url = f"{self.base_url}{query.replace(' ', '+')}"
        webbrowser.get(using='chrome').open(search_url)
    def open_link(self, link):
        webbrowser.get(using='chrome').open(self.sites[link])

    def _load_sites(self, config_file: str="sites.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            sites = load(file)
            print("сайты загружены!", sites)
            self.sites = sites


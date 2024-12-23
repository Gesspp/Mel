import webbrowser
from json import load, dump

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

    def add_sites(self, site_name, site_url, config_file: str="sites.json"):
        self._load_sites()
        sites = self.sites
        if site_name in sites.keys():
            raise Exception(f"Программа {site_name} уже существует")
        sites[site_name] = site_url
        # Добавить проверку на существование файла
        with open(config_file, "w", encoding="utf-8") as file:
            dump(sites, file, separators=(",\n", ": "))
        self._load_sites()
        print(self.sites)

    
    def youtube_search(self, query):
        webbrowser.get(using='chrome').open(f"https://www.youtube.com/results?search_query={query}")

    def _load_sites(self, config_file: str="sites.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            sites = load(file)
            print("сайты загружены!", sites)
            self.sites = sites


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
        with open(config_file, "w", encoding="utf-8") as file:
            dump(sites, file, separators=(",\n", ": "))
        self._load_sites()
        print(self.sites)

    def remove_site(self, site_name: str, config_file: str="sites.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            sites = load(file)
        with open(config_file, "w", encoding="utf-8") as file:
            del sites[site_name]
            dump(sites, file, separators=(",\n", ": "))
        self._load_sites()

    def edit_site(self, site_name: str, new_name: str, new_path: str, config_file: str="sites.json"):
        with open (config_file, "r", encoding="utf-8") as file:
            sites = load(file)
        print(sites)
        with open(config_file, "w", encoding="utf-8") as file:
            sites[site_name] = new_path
            if site_name != new_name:
                sites = dict([
                    (key, value) if key != site_name else (new_name, new_path)
                    for key, value in sites.items()
                ])
            print(sites, "после")
            dump(sites, file, separators=(",\n", ": "))
        self._load_sites()

    def youtube_search(self, query):
        webbrowser.get(using='chrome').open(f"https://www.youtube.com/results?search_query={query}")

    def _load_sites(self, config_file: str="sites.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            sites = load(file)
            print("сайты загружены!", sites)
            self.sites = sites


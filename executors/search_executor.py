import webbrowser

class GoogleSearchExecutor:
    def __init__(self):
        self.base_url = "https://www.google.com/search?q="
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

    def open_search(self, query):
        """
        Открывает Chrome с поисковым запросом в Google.

        :param query: Поисковый запрос.
        """
        search_url = f"{self.base_url}{query.replace(' ', '+')}"
        webbrowser.get(using='chrome').open(search_url)


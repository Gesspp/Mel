import requests


class GoogleSearchAPI:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query, num_results=10):
        """
        Выполняет поиск по Google Custom Search API.

        :param query: Запрос для поиска
        :param num_results: Количество результатов
        :return: Список найденных ссылок и заголовков
        """
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query,
            "num": num_results
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            results = response.json().get("items", [])
            
            return [
                {
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"]
                }
                for item in results
            ]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []

if __name__ == "__main__":
    api_key = "AIzaSyAGE1U0uBm0oHra1wpoUCDz8iPm8LCFCy4"
    cse_id = "11172acf97fb1476a"
    google_search = GoogleSearchAPI(api_key, cse_id)

    results = google_search.search("никита михалков")
    for result in results:
        print(result["title"], result["link"])
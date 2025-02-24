# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time

# # Настроим Selenium WebDriver (например, Chrome)
# driver = webdriver.Chrome()  # Проверьте, чтобы драйвер был установлен

# # Переходим на YouTube и вводим запрос
# query = "Python tutorial"  # Запрос на YouTube
# driver.get("https://www.youtube.com")
# search_box = driver.find_element(By.NAME, "search_query")
# search_box.send_keys(query)
# search_box.send_keys(Keys.RETURN)

# # Ожидаем загрузки результатов
# time.sleep(3)

# # Получаем HTML-код страницы
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Находим ссылки на видео в результатах поиска
# videos = soup.find_all("a", {"id": "video-title"})
# for i, video in enumerate(videos[:5], start=1):  # Например, первые 5 видео
#     title = video.get("title")
#     url = "https://www.youtube.com" + video.get("href")
#     print(f"{i}. {title}: {url}")

# # Закрываем браузер
# driver.quit()

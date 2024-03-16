import requests
from bs4 import BeautifulSoup

def free_servers():
    print("Starting...")

    ########################################################################
    # URL страницы со списком новых серверов Minecraft на minecraftrating.ru
    url2 = "https://minecraftrating.ru/new-servers/"
    try:
        # Отправляем GET запрос на вторую страницу
        response2 = requests.get(url2)

        # Проверяем успешность запроса
        if response2.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML второй страницы
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            
            # Находим все элементы с классом "tooltip", которые содержат информацию о серверах
            tooltip_elements = soup2.find_all(class_="tooltip")
            
            # Выводим информацию о серверах с minecraftrating.ru
            print("\nСписок серверов на minecraftrating.ru:")
            for tooltip_element in tooltip_elements:
                server_info = tooltip_element.text.strip()
                # Проверяем, содержит ли текст элемента домены из списка
                if any(suffix in server_info for suffix in [".gamely.pro", ".rioncloud.su", ".veroid.net", ".apexnodes.xyz", ".game4free.net", ".rustix.su"]):
                    print(server_info)
                    with open("done_filter.txt", "a") as file:
                        file.write(server_info + "\n")
        else:
            print("Произошла ошибка при получении страницы", url2)
    except Exception as e:
        print("Произошла ошибка:", e)

    ########################################################################
    # URL страницы со списком новых серверов Minecraft на misterlauncher.org
    url3 = "https://misterlauncher.org/servera-novye/"
    try:
        # Отправляем GET запрос на третью страницу
        response3 = requests.get(url3)

        # Проверяем успешность запроса
        if response3.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML третьей страницы
            soup3 = BeautifulSoup(response3.content, 'html.parser')
            
            # Находим все элементы span с атрибутом data-toggle="tooltip", которые содержат информацию о серверах
            tooltip_elements_3 = soup3.find_all("span", {"data-toggle": "tooltip"})
            
            # Выводим информацию о серверах с misterlauncher.org
            print("\nСписок серверов на misterlauncher.org:")
            for tooltip_element_3 in tooltip_elements_3:
                # Проверяем, есть ли атрибут data-clipboard-text
                if "data-clipboard-text" in tooltip_element_3.attrs:
                    server_info_3 = tooltip_element_3["data-clipboard-text"]
                    print(server_info_3)
                    with open("done_filter.txt", "a") as file:
                        file.write(server_info_3 + "\n")
        else:
            print("Произошла ошибка при получении страницы", url3)
    except Exception as e:
        print("Произошла ошибка:", e)

def main():
    print("Starting...")

    # URL страницы со списком новых серверов Minecraft на monitoringminecraft.ru
    url1 = "https://monitoringminecraft.ru/novie-servera"

    # Отправляем GET запрос на страницу
    response1 = requests.get(url1)

    # Проверяем успешность запроса
    if response1.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup1 = BeautifulSoup(response1.content, 'html.parser')
        
        # Находим все элементы с классом "ip_serv", которые содержат IP-адреса серверов
        ip_elements1 = soup1.find_all(class_="ip_serv")
        
        # Выводим IP-адреса серверов
        print("Список серверов на monitoringminecraft.ru:")
        for ip_element1 in ip_elements1:
            ip_address1 = ip_element1.text.strip()
            print(ip_address1)
            with open("done_nofilter.txt", "a") as file:
                file.write(ip_address1 + "\n")
    else:
        print("Произошла ошибка при получении страницы", url1)

    ########################################################################
    print("Готово")

print("################################")
print("################################")
print("Добро пожаловать в MineParser!")
print("################################")
print("################################")
print("Давай начнем")

free_servers_input = input("Вы хотите искать сервера только на бесплатных хостингах? (y/n): ")
if free_servers_input == "y":
    print("Окей, я начинаю парсинг серверов с мониторингов")
    free_servers()
elif free_servers_input == "n":
    print("Окей, дальше")
    main()
else:
    print("Некорректный ввод.")

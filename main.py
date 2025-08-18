# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Основной метод для обработки входящих GET-запросов"""

        if self.path == "/css/bootstrap.min.css":
            self.do_GET_CSS()
        else:
            self.do_GET_HTML()


    def do_GET_CSS(self):
        """Метод для обработки входящих GET-запросов стилей"""
        with open("css/bootstrap.min.css", "rb") as file:
            page_content = file.read()

        self.send_response(200)  # Отправка кода ответа
        self.send_header(
            "Content-type", "text/css"
        )  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(page_content)  # Тело ответа


    def do_GET_HTML(self):
        """Метод для обработки остальных страниц"""
        with open("contacts.html", "rb") as file:
            page_content = file.read()

        self.send_response(200)  # Отправка кода ответа
        self.send_header(
            "Content-type", "text/html"
        )  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(page_content)  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")

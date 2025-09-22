# Импорт необходимых библиотек
import requests  # Для выполнения HTTP-запросов к API
from tkinter import *  # Для создания графического интерфейса
from tkinter import messagebox as mb  # Для показа всплывающих сообщений
from tkinter import ttk  # Для стилизованных виджетов

# Словарь для преобразования кодов криптовалют в идентификаторы API CoinGecko
crypto_ids = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'XRP': 'ripple',
    'BNB': 'binancecoin',
    'DOGE': 'dogecoin'
}

# Словарь с русскими названиями криптовалют и валют
cur = {
    'BTC': 'Биткоин',
    'ETH': 'Эфириум',
    'XRP': 'Риппл',
    'BNB': 'Бинанс коин',
    'DOGE': 'Догекоин',
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'USD': 'Американский доллар'
}


# Функция обновления метки базовой криптовалюты
def update_b_label(event):
    code = b_combobox.get()  # Получаем выбранный код из выпадающего списка
    name = cur[code]  # Получаем русское название по коду
    b_label.config(text=name)  # Обновляем текст метки


# Функция обновления метки целевой валюты
def update_t_label(event):
    code = t_combobox.get()  # Получаем выбранный код из выпадающего списка
    name = cur[code]  # Получаем русское название по коду
    t_label.config(text=name)  # Обновляем текст метки


# Основная функция для получения курса обмена
def exchange():
    crypto_code = b_combobox.get()  # Получаем код выбранной криптовалюты
    currency_code = t_combobox.get()  # Получаем код выбранной валюты

    # Проверяем, что оба значения выбраны
    if crypto_code and currency_code:
        try:
            # Получаем ID криптовалюты для API CoinGecko
            coin_id = crypto_ids.get(crypto_code)
            # Если криптовалюта не найдена в словаре
            if not coin_id:
                mb.showerror('Ошибка', f'Криптовалюта {crypto_code} не поддерживается')
                return  # Выходим из функции

            # Формируем URL для запроса к API CoinGecko
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency_code.lower()}'
            response = requests.get(url)  # Выполняем GET-запрос
            response.raise_for_status()  # Проверяем статус ответа (выбрасывает исключение при ошибке)
            data = response.json()  # Преобразуем полученные от API данные в формате JSON в работающую структуру данных

            # Проверяем, что данные получены и содержат нужную валюту
            if coin_id in data and currency_code.lower() in data[coin_id]:
                exchange_rate = data[coin_id][currency_code.lower()]  # Получаем курс обмена
                crypto_name = cur[crypto_code]  # Русское название криптовалюты
                currency_name = cur[currency_code]  # Русское название валюты

                # Показываем всплывающее окно с курсом
                mb.showinfo('Курс обмена',
                            f'Курс: 1 {crypto_name} = {exchange_rate:,.2f} {currency_name}')
            else:
                # Если данные не получены
                mb.showerror('Ошибка', f'Не удалось получить данные для {crypto_code}/{currency_code}')

        # Обработка ошибок сети
        except requests.exceptions.RequestException as e:
            mb.showerror('Ошибка сети', f'Не удалось подключиться к API: {e}')
        # Обработка всех остальных ошибок
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        # Если не все значения выбраны
        mb.showwarning('Внимание!', 'Выберите криптовалюту и валюту!')


# Создаем главное окно приложения
window = Tk()
window.title('Курс обмена криптовалюты')  # Устанавливаем заголовок окна
window.geometry('360x300')  # Устанавливаем размер окна

# Создаем и размещаем метку для выбора базовой криптовалюты
Label(text='Базовая криптовалюта').pack(padx=10, pady=10)

# Создаем выпадающий список для выбора криптовалюты
b_combobox = ttk.Combobox(values=['BTC', 'ETH', 'XRP', 'BNB', 'DOGE'])
b_combobox.pack(padx=10, pady=10)  # Размещаем список в окне
# Привязываем обработчик события выбора элемента
b_combobox.bind('<<ComboboxSelected>>', update_b_label)

# Создаем метку для отображения названия выбранной криптовалюты
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)  # Размещаем метку в окне

# Создаем и размещаем метку для выбора целевой валюты
Label(text='Целевая валюта').pack(padx=10, pady=10)

# Создаем выпадающий список для выбора валюты
t_combobox = ttk.Combobox(values=['USD', 'RUB', 'EUR'])
t_combobox.pack(padx=10, pady=10)  # Размещаем список в окне
# Привязываем обработчик события выбора элемента
t_combobox.bind('<<ComboboxSelected>>', update_t_label)

# Создаем метку для отображения названия выбранной валюты
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)  # Размещаем метку в окне

# Создаем кнопку для получения курса обмена
Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

# Запускаем главный цикл обработки событий GUI
window.mainloop()

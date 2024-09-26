# Загрузка фотографий космоса
Данный код - это скрипт для телеграмм бота, который должен автоматизировать выгружение фотографий, связанных с космо тематикой. С помощью индивидуального токена API с официального сайта [NASA](https://api.nasa.gov), программа находит фотографии космоса из разных API-интерфейсов NASA, используя ссылки на них всё с того же сайта, после чего загружает нужное количество фотографий в собственную папку. 

## Окружение
### Зависимости
Python3 должен быть уже установлен. После чего, используя `pip` (или `pip3`, есть конфликт с Python2), устанавливаем зависимости:

```
pip install -r requirements.txt
```
### Переменные окружения
- "NASA_TOKEN"

В данной переменной хранится личный API ключ, благодаря которому программа может активировать ссылки и достать из них нужные фотографии. Сам ключ можно получить на сайте [NASA](https://api.nasa.gov), для этого нужно зайти на сайт в раздел ***Generate API Key***, ввести требуемые данные и нажать ***Signup***, после чего на почту придёт письмо с вашим личным API ключом.

- "BOT_TOKEN"

В этой переменной хранится личный номер бота в телеграмме, он нужен для того, чтобы программа могла найти и использовать его.  

Сами переменные хранятся в файле `.env`.

## Запуск
После того как мы установили зависимости, вписали свой API ключ и личный номер бота в переменные **NASA_TOKEN** и **BOT_TOKEN**, можно приступить к запуску программы.
Прграмма разделена на несколько скриптов, каждый из которых запускается отдельно:

### main.py
Этот скрипт запускать не обязательно, в нём содержится важная функция `create_path`. Эта функция создаёт папку в которую далее будут загружаться все фотографии для выгрузки. Функция передаётся в коде остальных скриптов, поэтому запуск **main.py** не обязателен.

### fetch_spacex_images.py
В этом скрипте программа с загрузкой фото с запусками ракет. Запускается программа следующим образом:
```
python fetch_spacex_images.py
```
Также у этого скрипта есть один необязательный аргумент: `id`. Этот аргумент принимает в себя определённый id номер для *spacex API*. благодаря ему программа понимает из какой именно базы брать фотографии запусков ракет. По умолчанию этот аргумент принимает значение `5eb87d46ffd86e000604b388`, что выгружает фотографии запуска, id которого указан в официальной документации spaceX NASA.

```
python fetch_spacex_images.py --id 5eb87d46ffd86e000604b388
```
### apod_images.py
Этот скрипт также создан для загрузки фотографий, только уже из *APOD API*, куда NASA выгружает так называемые фото дня. Для запуска:

```
python apod_images.py
```
У скрипта также есть необязательный аргумент: `count_load`. Аргумент нужен для определения количества фотографий, которое нужно выгрузить в папку. По умолчанию выгружается 30 фотографий.
```
python apod_images.py --count_load 15
```
### epic_images.py
Скрипт как и прошлые загружает фото с API, на этот раз из *EPIC API*, сюда NASA загружают фотографии Земли, а точнее ее положений в течении суток:
```
python epic_images.py
```
### tg_bot.py
Последний скрипт в программе, он нужен для того, чтобы можно было подключить папку с фотографиями и запустить телеграмм бота в работу.
```
python tg_bot
```
У скрипта есть необязательный аргумент `time`, он определяет то, с какой переодичностью будут выкладываться фотографии ботом. Соответственно принимает он в себя число, обознаающее время паузы между фото ***в секундах***. По умолчанию пауза равна `4 часа`.
```
python tg_bot --time 40
```
## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

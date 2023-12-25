# Foodgram
[![Main Foodgram workflow](https://github.com/Kseniya2806/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/Kseniya2806/foodgram-project-react/actions/workflows/main.yml)

# "Продуктовый помощник" (Foodgram)

---
## О проекте <a id=1></a>

Проект "Продуктовый помошник" (Foodgram) предоставляет пользователям следующие возможности:
  - создавать свои рецепты и управлять ими
  - просматривать рецепты других пользователей
  - добавлять рецепты других пользователей в "Избранное" и в "Корзину"
  - подписываться на других пользователей
  - скачать список ингредиентов для рецептов, добавленных в "Корзину"

---

## Стек технологий <a id=6></a>

Стек технологий: Python 3, Django, Django Rest, React, Docker, PostgreSQL, nginx, gunicorn, Djoser.

---
##### Клонировать проект из репозитория <a id=2></a>
Клонируйте репозиторий отсюда https://github.com/Kseniya2806/foodgram-project-react

---

---

##### Настроить Docker <a id=2></a>

```bash
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```

##### Создать файл .env и указать переменные по примеру .env.example:
``` 
cd foodgram
sudo nano .env
```
##### Установить и запустить Nginx:
```
sudo apt install nginx -y
sudo systemctl start nginx
```
##### Настроить и включить firewall:
```
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```
##### Открыть файл Nginx и поменять настройкиб сохранить и закрыть:
```
sudo nano /etc/nginx/sites-enabled/default
```
```
server {
    listen 80;
    server_name your_domain_name.com;
    
    location / {
        proxy_set_header HOST $host;
        proxy_pass http://127.0.0.1:9000;

    }
}
```
##### Проверить корректность настроек и перезапустить Nginx: 
```
sudo nginx -t
sudo systemctl start nginx
```
##### Загрузить образы из DockerHub:
```
sudo docker compose -f docker-compose.production.yml pull
```
##### Остановить и удалить все контейнеры:
```
sudo docker compose -f docker-compose.production.yml down
```
##### Запустить контейнеры из образов в фоновом режиме: 
```
sudo docker compose -f docker-compose.production.yml up -d
```
##### Выполнить миграции: 
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate 
```
##### Собрать статику:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```
##### Создать суперпользователя (указать логин, e-mail, пароль):
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser 
```
##### Загрузить список ингредиентов в базу данных:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_data
``` 
##### Загрузить тестовые данные:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py demo_data

``` 
## Автор <a id=7></a>

Ксения Заболоцкая
https://github.com/Kseniya2806/


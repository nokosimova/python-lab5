Шаг 1. **Клонирование репозитория**:

   ```bash
   git clone [https://github.com/artcherenkov/itmo-flask-postgres.git](https://github.com/nokosimova/python-lab5.git)
   ```

Шаг 2. **Запустить сборку из docker-compose**:

   ```bash
   docker-compose up --build
   ```

   Flask-приложение будет доступно через:
   ```
   http://localhost:5050
   ```
В отдельном контейнере database будет поднята Postgres БД

Шаг 3. **Остановка контейнеров**:

   ```bash
   docker-compose down
   ```

# -Docker
# Практическое задание: Docker Compose + MySQL + FastAPI

**Статус:** ✅ Выполнено  
**Репозиторий:** [michaelkoch51/practicprim-Docker](https://github.com/michaelkoch51/practicprim-Docker)  

> **Коротко о сути:** Приложение на FastAPI при запросе к `/` пишет данные в MySQL. Из‑за прав в MySQL 8.x база, пользователь и таблица созданы вручную. Работа подтверждена: контейнеры `Up` (у БД статус `healthy`), API отдаёт JSON, в таблице `requests` есть записи.

«Задание выполнено: приложение на FastAPI и MySQL запущены через Docker Compose. База virtd, пользователь app_user и таблица requests созданы вручную из‑за ограничений прав в MySQL 8.x. При запросе к / приложение успешно пишет данные в таблицу — подтверждено выводом SELECT * FROM requests (4 записи). Репозиторий:

![]()
![]()
![]()
![]()
![]()
![]()

# Инструкция по развертыванию Render

1. Код должен быть размещён в GitHub-репозитории.
2. В корне проекта должны быть:
   - `main.py` — точка входа
   - `requirements.txt` — зависимости
   - Папка `templates/` с шаблоном Word
3. В `main.py` обязательно укажи:

```python
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

from flask import Flask, request, send_file
from docxtpl import DocxTemplate
import tempfile
import os

app = Flask(__name__)

@app.route("/report")
def generate_report():
    kad = request.args.get("kad")
    if not kad:
        return "Укажите кадастровый номер ?kad=", 400

    tpl = DocxTemplate("templates/object_report_template.docx")
    context = {
        "kadNumber": kad,
        "address": "г. Москва, ул. Примерная",
        "riskLevel": "🟡 Средний риск",
        "section_name_1": "1. Право собственности",
        "marker_1": "🟢",
        "report_summary_1": "Нет рисков",
        "recommendations_1": "Рекомендуем стандартную проверку документов"
    }
    tpl.render(context)

    tmp_path = tempfile.mktemp(suffix=".docx")
    tpl.save(tmp_path)

    return send_file(tmp_path, as_attachment=True, download_name=f"report_{kad}.docx")

# Важно: Render требует слушать переменную PORT
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


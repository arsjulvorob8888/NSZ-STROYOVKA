from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="NSZ-STROYOVKA")

CONTENT = {
    "welcome": "Добро пожаловать!",
    "главное": "Здесь вы найдете актуальную информацию о проекте и услугах.",
    "доставка": "Оформите заказ, и мы согласуем удобные дату, время и адрес доставки.",
    "отзывы": "Нам важно ваше мнение. Оставьте отзыв после получения заказа — это помогает нам становиться лучше.",
}


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api/content")
def content() -> dict[str, str]:
    return CONTENT


@app.get("/health", include_in_schema=False)
def health() -> dict[str, str]:
    return {"status": "ok"}

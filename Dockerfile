FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# Cloud Run 會注入 PORT；本機預設 8080
ENV PORT=8080
EXPOSE 8080

# shell form 讓 ${PORT} 能展開
CMD exec uvicorn server:app --host 0.0.0.0 --port ${PORT}

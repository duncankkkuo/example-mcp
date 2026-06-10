# example-mcp

KKday MCP Platform 的範例 MCP server，用來測試平台的「貼 repo → 自動部署」流程。

- 用官方 [`mcp`](https://pypi.org/project/mcp/) SDK 的 FastMCP，**streamable-http** transport
- 服務路徑 `/mcp`，監聽 `$PORT`（Cloud Run 注入，預設 8080）
- 無自帶驗證 —— 平台的 JWT 驗證在 Apigee 那層，這裡是被保護的後端

## Tools（14 個）
`echo` · `add` · `subtract` · `multiply` · `divide` · `current_time` ·
`random_number` · `reverse_text` · `word_count` · `to_uppercase` ·
`bmi` · `celsius_to_fahrenheit` · `fibonacci` · `generate_uuid`

## 本機跑
```bash
pip install -r requirements.txt
python server.py            # http://localhost:8080/mcp
# 或用 uv：uv run --with mcp --with "uvicorn[standard]" python server.py
```

## 上傳 GitHub
```bash
cd example-mcp
git init && git add -A && git commit -m "example mcp server"
gh repo create kkday/example-mcp --private --source=. --push
```

## 透過平台部署
在平台「① 部署 MCP」頁：
- Repo 網址：`https://github.com/<org>/example-mcp.git`
- MCP 名稱：`example-mcp`（小寫英數和 -）

平台會 `gcloud run deploy --source` 直接用這裡的 Dockerfile build。

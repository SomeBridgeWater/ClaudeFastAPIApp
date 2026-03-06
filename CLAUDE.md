# Claude Code Project Guidelines
- 全ての対話、説明、提案は日本語で行ってください。
- コード内のコメントやドキュメント(README等)も日本語で記述してください。
- 技術用語については、無理に訳さず一般的なカタカナ表記や英語表記を維持してください。
- プログラミング言語はPythonを使用すること。
- どうしてもシステム全体に必要なツールがある場合は、インストール前に必ずユーザーに確認を求めること。
- パッケージをインストールする際は、`pip install`は絶対に使わないこと。
- Macに最初から入っているシステム用のPython(/usr/bin/python3)は絶対に何もしてはならない。

# Build & Run Commands
- Install dependencies: `uv sync`
- Run development server: `uv run my-command`
- Add new dependency: `uv add <package>`

# Project Structure
- Source code: `src/my_package/`
- Entry point: `src/my_package/main.py` (defined as `my-command` in pyproject.toml)

# Coding Guidelines
- Framework: FastAPI
- Use Python 3.14+ features (Standard library, type hints)
- Follow `src` layout for imports (e.g., `from my_package.utils import ...`)
- Return JSON responses using standard Pydantic models

# ソース構造
- calude-fastapi-app (Root)
  └── src : ソース格納ディレクトリ
       └── my_package : パッケージ
              ├── __init__.py : 
              └── main.py : エントリーポイント

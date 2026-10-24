# News AI Agent

This repository contains a Flutter client and a small FastAPI backend. Both are
currently starter/prototype code: the Flutter screen is the default counter
demo, and the backend's news-fetch and digest endpoints are placeholders.

## Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs` for the API documentation and
`http://localhost:8000/health` for the health check. The local SQLite database
is created in `backend/` when the API starts.

## Flutter app

```bash
cd mobile/news_app
flutter pub get
flutter run
```

When wiring API calls, configure the backend URL with
`--dart-define=NEWS_API_BASE_URL=http://YOUR_COMPUTER_IP:8000`. Use `localhost`
for an iOS simulator, `10.0.2.2` for the standard Android emulator, or your
computer's LAN address for a physical device. The current demo screen does not
yet call the backend.

## Repository notes

- `backend/` contains the FastAPI entry point, its dependencies, and the
  runtime-created local SQLite database.
- `mobile/news_app/lib/main.dart` is the Flutter entry point.
- `mobile/news_app/lib/core/` holds app-wide configuration; `features/` groups
  UI and behavior by product feature.
- `mobile/news_app/android/`, `ios/`, `linux/`, `macos/`, `web/`, and `windows/`
  are the standard Flutter platform runners.
- Keep each source file focused. About 150 lines is a useful review guideline,
  not a hard limit; split code when a file has multiple responsibilities rather
  than to satisfy an exact line count.
- Keep local `.env` files and SQLite databases out of Git. If a credential was
  committed previously, rotate it; ignoring or deleting the file in a later
  commit does not erase it from Git history.

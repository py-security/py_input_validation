# Beispiel: Sichere FastAPI-API

Dieses Projekt zeigt eine kleine **FastAPI**-Anwendung mit:

- Eingabevalidierung (Pydantic / FastAPI)
- strukturierter Fehlerbehandlung (`HTTPException`)
- sicherer Konfiguration über Umgebungsvariablen (`API_KEY` in `.env`)

## Voraussetzungen

- Python 3.10+ (oder ähnlich aktuelle Version)
- `pip` installiert

Optional, aber empfohlen:

- Virtuelle Umgebung (z. B. `venv`)

---

## 1. Repository / Projektstruktur

Beispielhafte Struktur:

```text
projekt-ordner/
├─ main.py
├─ requirements.txt
└─ .env         # wird gleich angelegt, NICHT in Git einchecken
```

## 2. Setup

```shell
# virtuelle Umgebung anlegen
python -m venv .venv

# aktivieren (Windows)
.venv\Scripts\activate

# aktivieren (macOS / Linux)
source .venv/bin/activate
```

## 3. Dependencies

```shell
pip install -r requirements.txt
```

## 4. Setup .env

Set the `API_KEY` variable in the env file

Wichtig:

*.env* NIE in Git einchecken (enthalten in `.gitignore`)

API-Keys und Passwörter nicht im Code hardcoden

## 5. Start the App

```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Erklärung:

- `main` = Dateiname main.py (ohne .py)
- `app` = Name des FastAPI-Objekts in main.py
- `--reload` = automatischer Neustart bei Codeänderungen (für Entwicklung)

## 6. API testen
### 6.1 Root-Endpoint
curl http://127.0.0.1:8000/

Antwort (Beispiel):

{"message":"Sichere API laeuft"}

### 6.2 GET /items/{item_id}
curl http://127.0.0.1:8000/items/1


Fehlerbeispiel (item_id < 1):

curl http://127.0.0.1:8000/items/0


Antwort (Beispiel):

{"detail":"Item-ID muss positiv sein"}

### 6.3 POST /items/ mit API-Key
```sh
curl -X POST "http://127.0.0.1:8000/items/?api_key=mein-geheimer-api-key-123" -H "Content-Type: application/json" -d '{"name": "Buch", "price": 9.99}'
```

Hinweis: mein-geheimer-api-key-123 muss zum Wert in deiner .env passen.

## 7. Interaktive API-Dokumentation (Swagger UI)

FastAPI bringt automatisch eine interaktive API-Doku mit:

Swagger UI: http://127.0.0.1:8000/docs

Alternative Docs: http://127.0.0.1:8000/redoc

Hier kannst du Endpunkte testen, Requests ausprobieren und die Schemas ansehen.

## 8. Nächste Schritte

Logging ergänzen (ohne Secrets zu loggen)

Weitere Endpunkte mit Validierung hinzufügen

Fehler-Handling zentralisieren (Custom-Exception-Handler)
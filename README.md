# Muzejski Chatbot - RBA Zadatak

Ovo je minimalistički API koji implementira chatbot za generičke informacije o muzeju.
Služi kandidatima za **automatizirano testiranje (REST)** i/ili **end-to-end testiranje (Selenium)**.

Chatbot pokriva ograničen skup **namjera** (radno vrijeme, ulaznice, adresa, izložbe, kafić, toaleti, pristupačnost, parking, članstvo, kontakt) i vraća **determinističke kanonske odgovore**.

---

## 🚀 Kako pokrenuti

### 1. Lokalno (Python venv)

Ako želite pokretati lokalno, potrebno je napraviti **.env** datoteku na temelju [`.env.example`](./.env.example) datoteke.  
U `.env` upišite tajni ključ koji ćete dobiti od nas (npr. `API_KEY_VALUE=TAJNI_KLJUC`) *Možete upisati bilo što lokalno nije bitno koji je ključ.

```bash
git clone <ovaj-repo>
cd chatbot-qa-api

# kreirajte .env na temelju .env.example
cp .env.example .env
# uredite .env i upišite API_KEY_VALUE

python -m venv .venv
source .venv/bin/activate   # na Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

### 2. Docker

```bash
docker build -t muzejski-bot:latest .
docker run -p 8000:8000 -e API_KEY_VALUE=TAJNI_KLJUC muzejski-bot:latest
```

Aplikacija će biti dostupna na [http://localhost:8000](http://localhost:8000) za oba slučaja.

---

## 🌐 Endpointi

* `GET /health`
  Provjera zdravlja API-ja.
  Ako je sve u redu vraća `{"status":"ok"}`

* `POST /prompt` *(zahtijeva API ključ)*
  Pošaljete poruku i dobijete odgovor:

  POST Request Body:
  ```json
  {
    "message": "Koliko košta ulaznica?"
  }
  ```

  Response:
  ```json
  {
    "intent": "ulaznice",
    "confidence": 0.91,
    "reply": "Opća ulaznica iznosi 12 € ...",
    "probs": { "ulaznice": 0.91, "radno_vrijeme": 0.06, ... },
    "trace": { "vectorizer": "tfidf(word 1-2gram)", "classifier": "logreg(multinomial)" }
  }
  ```

* `GET /` (index stranica)
  **GUI za chat** - Ako se odlučite na Selenium testiranje.
  Elementi imaju definirane HTML atribute kako biste ih lako pronašli.

* `GET /intents`
  Statička HTML stranica s pregledom **namjera, kanonskih odgovora i primjera**.

* `GET /static/intents.json`
  Isti podaci o namjerama, ali u JSON obliku (ako je zgodnije za skripte).

---

## 🔐 Autentikacija

Za `POST /prompt` potrebno je poslati header:

```
X-API-KEY: { TAJNI_KLJUC_IZ_ZADATKA }
```

---

## 🧪 Kako testirati

Kandidati mogu birati pristup:

1. **REST testovi**

   * direktno zvati `/prompt` s očekivanim ulazima i validirati `intent`, `reply` i `confidence`.
   * generirati izvještaje po volji

2. **Selenium testovi**

   * otvoriti `http://localhost:8000/` i koristiti GUI:

     * upisati API ključ (`#api-key-input`),
     * slati poruke (`#chat-input` + `#chat-send`),
     * čitati odgovore (`#chat-messages`).
   * generirati izvještaje po volji

---

## 📚 Swagger / OpenAPI

Swagger dokumentacija dostupna je na:

* [http://localhost:8000/docs](http://localhost:8000/docs)
* OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

Sretno u testiranju i razvoju skripti! 🧪🤖

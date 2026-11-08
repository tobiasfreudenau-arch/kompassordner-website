# kompassordner.de

Statische Website des Vorlagen-Shops **Kompassordner** (Notfall-, Vorsorge- und Pflegeordner als PDF).

- `build.py` erzeugt alle HTML-Seiten aus einer Vorlage (`python3 build.py`). Texte und Schalter (`SHOP_LIVE`, `ETSY`) stehen oben im Skript.
- `DESIGN.md` beschreibt Farben, Typografie, Abstände und Komponenten; `assets/style.css` setzt sie um.
- `assets/img/` enthält Logo (Logo-Paket V1.0) und echte Produktseiten (WebP), `assets/fonts/` die selbst gehostete Schrift Inter.
- Hosting: GitHub Pages, Branch `main`. Eigene Domain über `CNAME` (`www.kompassordner.de`), sobald das DNS bei IONOS umgestellt ist. Kein Tracking, keine Cookies.

Änderung: Text in `build.py` anpassen → `python3 build.py` → committen → Pages veröffentlicht automatisch.

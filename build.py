# -*- coding: utf-8 -*-
"""Baut kompassordner.de als statische Seiten (HTML) nach DESIGN.md und Markenprofil."""
import os, datetime

SITE = "https://www.kompassordner.de"
SHOP_LIVE = False                       # auf True setzen, sobald der Etsy-Shop online ist
ETSY = "https://www.etsy.com/de/shop/Kompassordner"
PINTEREST = "https://www.pinterest.com/kompassordner"
MAIL_SHOP = "shop@kompassordner.de"
MAIL_POST = "post@kompassordner.de"
MAIL_LIZENZ = "lizenz@kompassordner.de"
STAND = "11/2026"
ASSET_V = "3"   # bei Asset-Änderungen hochzählen (umgeht Browser-Cache)
YEAR = "2026"

NAV = [("produkte.html", "Produkte"), ("so-funktioniert-es.html", "So funktioniert es"), ("ueber.html", "Über"), ("kontakt.html", "Kontakt")]


def farbreihe():
    items = "".join(f'<li><img src="assets/img/farben/{k}.webp?v={ASSET_V}" alt="Deckblatt in {t["name"]}" width="373" height="527" loading="lazy"><span>{t["name"]}</span></li>' for k, t in THEMES.items())
    return f'<ul class="farben">{items}</ul>'
THEMES = {'navy': {'name': 'Navy', 'primary': '#1F3A5F'}, 'salbei': {'name': 'Salbei', 'primary': '#3F5A4A'}, 'bordeaux': {'name': 'Bordeaux', 'primary': '#5B1F2E'}, 'tanne': {'name': 'Tannengrün', 'primary': '#1F4A3A'}, 'petrol': {'name': 'Petrol', 'primary': '#1B4F5C'}, 'schiefer': {'name': 'Schiefer', 'primary': '#3B4350'}, 'pflaume': {'name': 'Pflaume', 'primary': '#4A2C4F'}, 'terrakotta': {'name': 'Terrakotta', 'primary': '#8A3B2E'}, 'ozean': {'name': 'Ozeanblau', 'primary': '#1F4E79'}, 'mokka': {'name': 'Mokka', 'primary': '#4A3728'}, 'olive': {'name': 'Olive', 'primary': '#4F5A2A'}, 'anthrazit': {'name': 'Anthrazit', 'primary': '#2A2A2A'}, 'beere': {'name': 'Beere', 'primary': '#7A1F4A'}, 'rauchblau': {'name': 'Rauchblau', 'primary': '#4A6274'}}

def shop_button(label="Zum Shop auf Etsy", cls="btn btn--primary"):
    if SHOP_LIVE:
        return f'<a class="{cls}" href="{ETSY}" rel="noopener">{label}</a>'
    return f'<a class="{cls}" href="kontakt.html#start">Shop öffnet in Kürze – Bescheid bekommen</a>'

def page(path, title, desc, body, current=None, h1_in_body=True):
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a></li>'
        for href, label in NAV)
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kompassordner">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="assets/img/icon.svg?v={ASSET_V}" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png?v={ASSET_V}">
<link rel="preload" href="assets/fonts/Inter-Regular.woff2?v={ASSET_V}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/Inter-SemiBold.woff2?v={ASSET_V}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css?v={ASSET_V}">
<meta name="theme-color" content="#1F3A5F">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/img/icon.svg?v={ASSET_V}" alt="" width="48" height="48"><span class="word">Kompass<span>ordner</span></span></a>
    <nav class="nav" aria-label="Hauptnavigation"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="inhalt">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html"><img src="assets/img/icon.svg?v={ASSET_V}" alt="" width="40" height="40"><span class="word">Kompass<span>ordner</span></span></a>
        <p style="max-width:34ch;margin-top:16px">Ordner zum Ausfüllen und Ausdrucken für Notfall, Pflege, Rente und Nachlass. Für Familien, die vorbereitet sein wollen.</p>
      </div>
      <div>
        <h2>Seiten</h2>
        <ul>
          <li><a href="produkte.html">Produkte</a></li>
          <li><a href="so-funktioniert-es.html">So funktioniert es</a></li>
          <li><a href="ueber.html">Über Kompassordner</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <h2>Rechtliches</h2>
        <ul>
          <li><a href="impressum.html">Impressum</a></li>
          <li><a href="datenschutz.html">Datenschutz</a></li>
          <li><a href="widerruf-agb.html">Widerruf und AGB</a></li>
        </ul>
      </div>
      <div>
        <h2>Kontakt</h2>
        <ul>
          <li><a href="mailto:{MAIL_SHOP}">{MAIL_SHOP}</a></li>
          <li><a href="{PINTEREST}" rel="noopener">Pinterest</a></li>
          {"<li><a href=\"" + ETSY + "\" rel=\"noopener\">Etsy-Shop</a></li>" if SHOP_LIVE else ""}
        </ul>
      </div>
    </div>
    <p class="legal">© {YEAR} Kompassordner · Tobias Freudenau, Schkeuditz · Die Vorlagen dienen der Dokumentation und Organisation und ersetzen keine Rechts-, Steuer- oder medizinische Beratung.</p>
  </div>
</footer>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

# ---------------------------------------------------------------- Startseite
index_body = f"""
<section class="section--navy hero">
  <div class="wrap grid grid--7-5">
    <div>
      <h1>Wenn morgen etwas passiert – weiß deine Familie, wo alles liegt?</h1>
      <p class="lead">Kompassordner sind Ordner zum Ausfüllen und Ausdrucken. Für den Notfall, die Pflege zu Hause, die Rente und den Nachlass. Jede Seite löst eine Frage, die sich im Ernstfall stellt – ohne Fachsprache, ohne Berater.</p>
      <div class="actions">
        {shop_button()}
        <a class="btn btn--secondary" href="produkte.html">Die Ordner ansehen</a>
      </div>
    </div>
    <div class="hero-doc">
      <div class="doc-stack">
        <img class="doc" src="assets/img/notfall-cover.webp?v={ASSET_V}" alt="Deckblatt des Notfall- und Vorsorgeordners: dunkelblaue Fläche mit dem Titel „Mein Notfall- und Vorsorgeordner“" width="910" height="1287" fetchpriority="high">
        <img class="doc" src="assets/img/notfall-s04.webp?v={ASSET_V}" alt="" width="910" height="1287" aria-hidden="true" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid--5-7">
    <div>
      <h2>Ein Ordner, den jeder in der Familie findet und versteht</h2>
    </div>
    <div>
      <p class="lead">Die meisten Dinge sind irgendwo geregelt – im Kopf, in einer Schublade, in einem Online-Konto. Im Ernstfall hilft das niemandem. Ein Kompassordner bringt alles an einen Ort: auf Papier, zum Anfassen, für die Menschen, die dann handeln müssen.</p>
      <ul class="check check--big">
        <li><strong>Zum Ausfüllen oder Ausdrucken</strong></li>
        <li><strong>14 Farbwelten im Download</strong></li>
        <li><strong>Der Sofort-Teil kommt zuerst</strong></li>
        <li><strong>Jede Angabe mit Quelle und Stand</strong></li>
        <li><strong>Keine Passwörter im Ordner</strong></li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Zwei Ordner zum Start</h2>
    <p class="lead">Weitere folgen: Rentenstart, Todesfall-Checkliste, Widerspruchs-Kits für Pflegegrad und Schwerbehinderung.</p>
    <div class="grid grid--2" style="margin-top:32px">
      <article>
        <a class="shelf" style="display:block;max-width:420px" href="produkte.html#notfallordner" aria-label="Zum Notfall- und Vorsorgeordner"><img class="doc" src="assets/img/notfall-cover.webp?v={ASSET_V}" alt="Deckblatt „Mein Notfall- und Vorsorgeordner“" width="910" height="1287" loading="lazy" style="max-width:340px;margin-inline:auto"></a>
        <h3 style="margin-top:24px"><a href="produkte.html#notfallordner">Notfall- und Vorsorgeordner</a></h3>
        <p>36 Seiten in 9 Teilen: Notfallblatt, Vollmachten, Finanzen, Verträge, digitaler Nachlass, Checklisten für den Todesfall, persönliche Botschaft.</p>
        <p class="tnum"><strong>19,90 €</strong> <span class="soft">Einführungspreis · regulär 24,90 €</span></p>
      </article>
      <article>
        <a class="shelf" style="display:block;max-width:420px" href="produkte.html#pflegeordner" aria-label="Zum Pflegeordner"><img class="doc" src="assets/img/pflege-cover.webp?v={ASSET_V}" alt="Deckblatt „Mein Pflegeordner“" width="910" height="1287" loading="lazy" style="max-width:340px;margin-inline:auto"></a>
        <h3 style="margin-top:24px"><a href="produkte.html#pflegeordner">Pflegeordner für Angehörige</a></h3>
        <p>44 Seiten in 8 Teilen: Pflegegrad beantragen, Pflegetagebuch, Leistungen der Pflegekasse 2026, Wochenplan, Übergabeblatt, Protokolle, Finanzen.</p>
        <p class="tnum"><strong>12,90 €</strong> <span class="soft">Einführungspreis · regulär 14,90 €</span></p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Deine Farbe, dein Ordner</h2>
    <p class="lead">Jeder Kauf enthält alle 14 Farbwelten – von Navy bis Terrakotta. Das Papier bleibt immer ruhig im Sandton, die Deckel- und Überschriftenfarbe wählst du selbst. Einfach im Download den Ordner mit deiner Farbe öffnen.</p>
    {farbreihe()}
  </div>
</section>

<section class="section section--deep">
  <div class="wrap grid grid--5-7">
    <div><h2>So funktioniert es</h2></div>
    <div>
      <ol class="steps" style="grid-template-columns:1fr">
        <li><h3>Kaufen und herunterladen</h3><p>Du bekommst drei Dateien sofort nach dem Kauf: die ausfüllbare Fassung, die Druckfassung und ein Blatt „Lesen zuerst“, das alles in zwei Minuten erklärt.</p></li>
        <li><h3>Ausfüllen – am Bildschirm oder mit Stift</h3><p>Die ausfüllbare PDF öffnest du im kostenlosen Adobe Acrobat Reader und speicherst sie. Oder du druckst die Fassung mit Linien aus und schreibst von Hand.</p></li>
        <li><h3>Abheften und Bescheid sagen</h3><p>In einen Aktenordner, an einen Ort, den die Familie kennt. Einmal im Jahr durchblättern – die letzte Seite erinnert dich daran.</p></li>
      </ol>
      <p style="margin-top:24px"><a href="so-funktioniert-es.html">Alle Details und häufige Fragen</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid--7-5">
    <div>
      <h2>Für dich, für deine Eltern, für die, die bleiben</h2>
      <p>Für erwachsene Kinder, die sich um ihre Eltern kümmern und den Überblick behalten müssen – zwischen Pflegeantrag, Vollmachten und Beruf. Für Menschen vor und im Ruhestand, die niemandem zur Last fallen wollen. Für alle, die lieber einen halb ausgefüllten Ordner haben als den perfekten Plan im Kopf.</p>
      <div class="note">
        <p><strong>Was ein Kompassordner nicht ist:</strong> keine Rechts-, Steuer- oder medizinische Beratung und kein Ersatz für notariell beurkundete Dokumente. Er hilft beim Sammeln, Ordnen und Vorbereiten – damit die Gespräche mit Ärztin, Pflegekasse oder Notar leichter werden.</p>
      </div>
    </div>
    <div>
      <div class="actions" style="margin-top:0">
        {shop_button()}
      </div>
      <p class="small soft" style="margin-top:16px">Digitale Produkte, kein Versand. Kauf und Download über Etsy. Fragen? <a href="mailto:{MAIL_SHOP}">{MAIL_SHOP}</a></p>
    </div>
  </div>
</section>
"""
page("index.html", "Kompassordner – Ordner für Notfall, Pflege, Rente und Nachlass zum Ausfüllen",
     "Ordner zum Ausfüllen und Ausdrucken (PDF): Notfall- und Vorsorgeordner, Pflegeordner für Angehörige. Jede Angabe mit Quelle und Stand, Updates kostenlos.",
     index_body, current=None)

# ---------------------------------------------------------------- Produkte
def register(items):
    return '<ol class="register">' + "".join(
        f'<li><span class="tab">{t}</span><span>{name}</span><span class="pages">{pages}</span></li>' for t, name, pages in items) + "</ol>"

notfall_reg = register([
    ("A", "Im Notfall – Notfallblatt, Medikamentenplan, „Wo finde ich was?“, wer zu informieren ist", "S. 4–8"),
    ("B", "Meine Person – persönliche Daten, Familie und Haushalt, Haustiere", "S. 9–11"),
    ("C", "Vorsorgedokumente – Vollmachten und Verfügungen, bevollmächtigte Personen, Wünsche zu Behandlung und Pflege", "S. 12–14"),
    ("D", "Finanzen – Konten und Karten, Einnahmen, Ausgaben, Kredite, Geldanlagen, Immobilien", "S. 15–20"),
    ("E", "Versicherungen", "S. 21–22"),
    ("F", "Verträge und Fahrzeuge", "S. 23–25"),
    ("G", "Digitaler Nachlass – Geräte, Online-Konten, Passwort-Hinweise, digitale Wünsche", "S. 26–28"),
    ("H", "Im Todesfall – Checklisten erste Tage und Wochen, Bestattungswünsche, Benachrichtigungsliste, Testament und Nachlass", "S. 29–34"),
    ("I", "Persönliches – persönliche Botschaft, jährliche Prüfung", "S. 35–36"),
])
pflege_reg = register([
    ("A", "Sofort – Pflege-Notfallblatt, Pflegegrad beantragen, Pflegetagebuch zu den 6 Modulen der Begutachtung, Bescheid prüfen, Widerspruch", ""),
    ("B", "Die Person – Gewohnheiten und Biografie, Gesundheit und Ärzte, Medikamentenplan, Hilfsmittel, Essen und Trinken", ""),
    ("C", "Leistungen 2026 – alle Beträge der Pflegekasse nach Pflegegrad, Leistungs-Check, Entlastungsbetrag, Verhinderungs- und Kurzzeitpflege, Fristen", ""),
    ("D", "Alltag organisieren – Wochenplan, Aufgabenverteilung, Pflegedienst, Übergabeblatt, Wohnung sicher machen", ""),
    ("E", "Dokumentation – Vitalwerte, Pflegeprotokoll, Sturzprotokoll, Arztbesuche, Fragen an den Arzt", ""),
    ("F", "Finanzen – Kosten und Erstattungen, Vereinbarung zum Pflegegeld, Belege für die Steuer", ""),
    ("G", "Für die Pflegeperson – Beruf und Pflege vereinbaren, Entlastungs-Check, Notfallplan", ""),
    ("H", "Vorsorge und Übergang – Vollmachten im Überblick, Vergleich Tagespflege, Kurzzeitpflege, Heim", ""),
])

produkte_body = f"""
<section class="section">
  <div class="wrap">
    <h1>Die Ordner</h1>
    <p class="lead">Jeder Ordner kommt als ausfüllbare PDF, als Druckfassung mit Linien und mit einem Blatt „Lesen zuerst“. Dazu dieselben Dateien in allen 14 Farbwelten – du wählst im Download die Farbe, die zu dir passt. Digitale Produkte, kein Versand – Kauf und Download über Etsy.</p>

    <article class="product" id="notfallordner">
      <div class="grid grid--5-7">
        <figure class="shelf">
          <img class="doc" src="assets/img/notfall-cover.webp?v={ASSET_V}" alt="Deckblatt „Mein Notfall- und Vorsorgeordner“" width="910" height="1287">
          <div class="thumbs">
            <img src="assets/img/notfall-s04.webp?v={ASSET_V}" alt="Seite 4: Notfallblatt mit Feldern für Kontakte, Medikamente und Vorsorgedokumente" width="910" height="1287" loading="lazy">
            <img src="assets/img/notfall-s06.webp?v={ASSET_V}" alt="Seite 6: Medikamentenplan als Tabelle" width="910" height="1287" loading="lazy">
            <img src="assets/img/notfall-s26.webp?v={ASSET_V}" alt="Seite 26: Digitaler Nachlass – Geräte und Online-Konten" width="910" height="1287" loading="lazy">
          </div>
          <figcaption>Echte Seiten aus der Druckfassung. Die ausfüllbare Fassung hat an denselben Stellen Formularfelder.</figcaption>
        </figure>
        <div>
          <h2 style="font-size:2rem">Notfall- und Vorsorgeordner</h2>
          <p class="price">19,90 € <s>24,90 €</s><small>Einführungspreis bis zu den ersten Bewertungen · 36 Seiten · A4 · PDF · Deutsch · Stand {STAND}</small></p>
          <p>Wenn etwas passiert, suchen Angehörige als Erstes: Wen rufe ich an? Welche Medikamente? Wo liegt die Vollmacht? Welche Verträge laufen? Dieser Ordner beantwortet das auf 36 Seiten – an einem Ort, ohne Suchen.</p>
          <h3>Das ist enthalten</h3>
          {notfall_reg}
          <ul class="check" style="margin-top:24px">
            <li>Ausfüllbare PDF mit über 1.500 Formularfeldern, speicherbar</li>
            <li>Druckfassung mit Linien, auch in Schwarz-Weiß ruhig</li>
            <li>„Lesen zuerst“ – eine Seite, die alles erklärt</li>
            <li>Alle 14 Farbwelten als ZIP (Navy, Salbei, Bordeaux, Tannengrün, Petrol, Schiefer, Pflaume, Terrakotta, Ozeanblau, Mokka, Olive, Anthrazit, Beere, Rauchblau)</li>
            <li>Updates kostenlos im Download-Bereich</li>
          </ul>
          <div class="actions">{shop_button("Notfallordner auf Etsy ansehen")}</div>
        </div>
      </div>
    </article>

    <article class="product" id="pflegeordner">
      <div class="grid grid--5-7">
        <figure class="shelf">
          <img class="doc" src="assets/img/pflege-cover.webp?v={ASSET_V}" alt="Deckblatt „Mein Pflegeordner“" width="910" height="1287" loading="lazy">
          <div class="thumbs">
            <img src="assets/img/pflege-s04.webp?v={ASSET_V}" alt="Seite 4: Pflege-Notfallblatt mit Kontakten und Hauptpflegeperson" width="910" height="1287" loading="lazy">
            <img src="assets/img/pflege-s06.webp?v={ASSET_V}" alt="Seite 6: Checkliste „Erste Schritte: Pflegegrad beantragen“" width="910" height="1287" loading="lazy">
            <img src="assets/img/pflege-s17.webp?v={ASSET_V}" alt="Seite 17: Leistungen der Pflegekasse nach Pflegegrad" width="910" height="1287" loading="lazy">
          </div>
          <figcaption>Echte Seiten aus der Druckfassung.</figcaption>
        </figure>
        <div>
          <h2 style="font-size:2rem">Pflegeordner für Angehörige</h2>
          <p class="price">12,90 € <s>14,90 €</s><small>Einführungspreis bis zu den ersten Bewertungen · 44 Seiten · A4 · PDF · Deutsch · Beträge Stand 01/2026</small></p>
          <p>Wenn Mutter oder Vater plötzlich Hilfe brauchen, kommt alles gleichzeitig: Antrag bei der Pflegekasse, Begutachtung, Leistungen, Pflegedienst, Familie, Beruf. Dieser Ordner bringt Ordnung in die ersten Wochen – und bleibt danach das Nachschlagewerk für alle, die mithelfen.</p>
          <h3>Das ist enthalten</h3>
          {pflege_reg}
          <ul class="check" style="margin-top:24px">
            <li>Ausfüllbare PDF mit über 2.500 Formularfeldern, speicherbar</li>
            <li>Druckfassung mit Linien</li>
            <li>„Lesen zuerst“ – eine Seite, die alles erklärt</li>
            <li>Alle 14 Farbwelten als ZIP (Navy, Salbei, Bordeaux, Tannengrün, Petrol, Schiefer, Pflaume, Terrakotta, Ozeanblau, Mokka, Olive, Anthrazit, Beere, Rauchblau)</li>
            <li>Alle Beträge und Fristen mit Stand 01/2026 und Quelle; Updates kostenlos</li>
          </ul>
          <div class="actions">{shop_button("Pflegeordner auf Etsy ansehen")}</div>
        </div>
      </div>
    </article>

    <hr>
    <div class="grid grid--2">
      <div>
        <h2>Name auf dem Deckblatt</h2>
        <p>Jeden Ordner gibt es auch personalisiert: mit deinem Namen oder dem Namen deiner Eltern auf dem Deckblatt, in der Farbwelt deiner Wahl. 29,90 € je Ordner, als eigenes Angebot im Shop.</p>
        <h2 style="margin-top:32px">Besondere Situation? Schreib uns.</h2>
        <p>Patchwork-Familie, eigener Betrieb, Haus im Ausland, Pflege durch mehrere Angehörige – wenn dein Fall nicht ins Raster passt, stellen wir dir den Ordner aus allen vorhandenen Seiten passend zusammen: eigene Rubriken, angepasste Bezeichnungen, dein Name, deine Farbe. Ab 49 € inklusive einer Korrekturrunde, fertig in drei Werktagen. Schreib kurz, worum es geht, an <a href="mailto:{MAIL_SHOP}?subject=Besondere%20Situation">{MAIL_SHOP}</a> – du bekommst einen Festpreis, bevor du etwas kaufst.</p>
      </div>
      <div>
        <h2>Für Pflegedienste, Bestatter, Berater</h2>
        <p>Mit der Firmenlizenz bekommst du den Ordner mit deinem Logo und deinen Farben und darfst ihn an eigene Kunden, Mandanten oder Patienten weitergeben – gedruckt oder als PDF. 199 € je Ordner, 399 € für drei. Anfragen an <a href="mailto:{MAIL_LIZENZ}">{MAIL_LIZENZ}</a>.</p>
      </div>
    </div>
    <div class="note">
      <p>Die Vorlagen dienen der Dokumentation und Organisation. Sie ersetzen keine Rechts-, Steuer- oder medizinische Beratung. Fristen und Zuständigkeiten bitte mit der zuständigen Stelle abgleichen. Lizenz für den privaten Gebrauch; Weitergabe und Weiterverkauf sind nicht gestattet. Preise sind Endpreise; Kleinunternehmer nach § 19 UStG, bei Sofort-Downloads erhebt Etsy die Umsatzsteuer.</p>
    </div>
  </div>
</section>
"""
page("produkte.html", "Produkte – Notfallordner und Pflegeordner zum Ausfüllen | Kompassordner",
     "Notfall- und Vorsorgeordner (36 Seiten) und Pflegeordner für Angehörige (44 Seiten) als ausfüllbare PDF und Druckfassung. Inhalt, Preise, Lizenzen.",
     produkte_body, current="produkte.html")

# ---------------------------------------------------------------- So funktioniert es
sfe_body = f"""
<section class="section">
  <div class="wrap">
    <h1>So funktioniert es</h1>
    <p class="lead">Vom Kauf bis zum fertigen Ordner im Regal – drei Schritte, kein Konto, kein Abo, kein Versand.</p>
    <ol class="steps">
      <li><h3>Kaufen und herunterladen</h3><p>Der Kauf läuft über Etsy. Direkt danach findest du die Dateien unter „Käufe und Bewertungen“ und über den Link in der Bestellbestätigung: die ausfüllbare Fassung, die Druckfassung und „Lesen zuerst“.</p></li>
      <li><h3>Ausfüllen</h3><p>Am Bildschirm: die ausfüllbare PDF im kostenlosen Adobe Acrobat Reader öffnen (nicht im Browser), ausfüllen, speichern. Mit Stift: die Druckfassung ausdrucken – sie hat Linien statt Felder und ist auch in Schwarz-Weiß ruhig.</p></li>
      <li><h3>Abheften und Bescheid sagen</h3><p>In einen Aktenordner, an einen Ort, den die Familie kennt. Sag den Menschen, die im Ernstfall handeln, wo er steht. Einmal im Jahr durchblättern – die letzte Seite erinnert dich.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid--5-7">
    <div><h2>Häufige Fragen</h2></div>
    <div>
      <details><summary>Brauche ich ein bestimmtes Programm?</summary><p>Für die ausfüllbare Fassung den kostenlosen Adobe Acrobat Reader (Windows, Mac, iPad, Android). Browser und manche Vorschau-Programme zeigen Formularfelder nicht vollständig an oder speichern Eingaben nicht. Die Druckfassung öffnet jedes PDF-Programm.</p></details>
      <details><summary>Kann ich die Seiten mehrfach drucken?</summary><p>Ja, so oft du willst – für dich und deine Familie im eigenen Haushalt. Nicht erlaubt sind Weitergabe, Verkauf oder gewerbliche Nutzung; dafür gibt es die Firmenlizenz.</p></details>
      <details><summary>Was passiert, wenn sich Fristen oder Beträge ändern?</summary><p>Jede Angabe trägt „Stand MM/JJJJ“. Ändert sich etwas, aktualisieren wir die Datei, und du lädst die neue Fassung kostenlos in deinem Etsy-Download-Bereich herunter.</p></details>
      <details><summary>Stehen in dem Ordner Passwörter oder Kontonummern?</summary><p>Nein, und das ist Absicht. Im Ordner steht nur, <em>wo</em> Zugänge und Unterlagen hinterlegt sind (zum Beispiel „Passwortliste im Safe“) – nie die Zugänge selbst. So kann der Ordner offen im Regal stehen.</p></details>
      <details><summary>Ist das Rechtsberatung?</summary><p>Nein. Die Ordner helfen beim Sammeln, Ordnen und Vorbereiten. Für Vollmachten, Verfügungen, Testament oder Widersprüche sind Notar, Anwältin, Pflegestützpunkt oder Verbraucherzentrale die richtigen Stellen – der Ordner macht diese Gespräche leichter.</p></details>
      <details><summary>Kann ich den Ordner verschenken?</summary><p>Ja. Viele Käufer füllen ihn gemeinsam mit den Eltern aus oder verschenken ihn zum Ruhestand. Wenn das Deckblatt einen Namen tragen soll, gibt es die personalisierte Fassung.</p></details>
      <details><summary>Wie bekomme ich Hilfe, wenn etwas nicht klappt?</summary><p>Schreib an <a href="mailto:{MAIL_SHOP}">{MAIL_SHOP}</a> oder über Etsy. Lässt sich eine Datei nicht öffnen oder fehlt eine Seite, bekommst du schnell eine funktionierende Fassung.</p></details>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap grid grid--7-5">
    <div>
      <h2>Bereit, Ordnung zu machen?</h2>
      <p class="lead" style="color:#E7E1D6">Der Notfallordner ist der beste Anfang – er deckt die Fragen ab, die sich in jeder Familie irgendwann stellen.</p>
    </div>
    <div class="actions" style="margin-top:0;align-self:center">{shop_button()}</div>
  </div>
</section>
"""
page("so-funktioniert-es.html", "So funktioniert es – Kaufen, ausfüllen, abheften | Kompassordner",
     "Kauf über Etsy, ausfüllbare PDF im Acrobat Reader oder Druckfassung mit Stift, Updates kostenlos. Antworten auf häufige Fragen.",
     sfe_body, current="so-funktioniert-es.html")

# ---------------------------------------------------------------- Über
ueber_body = f"""
<section class="section">
  <div class="wrap grid grid--5-7">
    <div>
      <h1>Über Kompassordner</h1>
    </div>
    <div>
      <p class="lead">Kompassordner ist ein kleines Unternehmen aus Schkeuditz bei Leipzig. Es macht Ordner, mit denen Familien die Dinge regeln, die man gern aufschiebt: Was ist im Notfall zu tun, wer darf entscheiden, wo liegt was, wie organisieren wir die Pflege.</p>
      <h2>Warum ein Kompass auf einem Ordner</h2>
      <p>Weil es im Ernstfall nicht an gutem Willen fehlt, sondern an Orientierung. Fristen, Formulare, Zuständigkeiten – das ist der Weg durch unbekanntes Gelände. Ein Kompass zeigt die Richtung. Ein Ordner hält fest, was man unterwegs braucht. Beides zusammen ist das, was Angehörige in einer schweren Woche am meisten brauchen: einen Ort, an dem alles steht.</p>
      <h2>Drei Dinge, an die wir uns halten</h2>
      <ul class="check">
        <li><strong>Vorsorge ist Fürsorge für die, die bleiben.</strong> Kein Grusel-Thema, sondern ein Akt der Ordnung.</li>
        <li><strong>Ordnung schlägt Perfektion.</strong> Ein halb ausgefüllter Ordner hilft im Ernstfall mehr als der perfekte Plan im Kopf.</li>
        <li><strong>Niemand braucht Fachsprache,</strong> um seine Angelegenheiten zu regeln. Jede Seite ist so geschrieben, dass man sie ohne Vorwissen ausfüllen kann.</li>
      </ul>
      <h2>Wie die Ordner entstehen</h2>
      <p>Jede Seite löst ein Problem, das der Käufer am Kauftag hat – sonst fliegt sie raus. Jede veränderliche Angabe (Frist, Betrag, Zuständigkeit) wird gegen eine Primärquelle geprüft: Gesetzestext, Deutsche Rentenversicherung, Pflegekassen, Ministerien. Sie trägt Quelle und Stand. Vor der Veröffentlichung füllt ein Testleser den Ordner aus, der ihn nicht gebaut hat. Und wenn sich etwas ändert, bekommen alle Käufer die neue Fassung kostenlos.</p>
      <h2>Was wir nicht tun</h2>
      <p>Keine Rechts-, Steuer- oder medizinische Beratung. Keine Versprechen, wie eine Behörde entscheidet. Keine Angstmache. Und keine Passwörter oder Kontonummern im Ordner – nur Hinweise, wo sie liegen.</p>
      <p>Inhaber: Tobias Freudenau. Kontakt: <a href="mailto:{MAIL_SHOP}">{MAIL_SHOP}</a> · <a href="impressum.html">Impressum</a></p>
    </div>
  </div>
</section>
"""
page("ueber.html", "Über Kompassordner – wer dahinter steht und wie die Ordner entstehen",
     "Kompassordner aus Schkeuditz bei Leipzig: Ordner für Notfall, Pflege, Rente und Nachlass. Haltung, Arbeitsweise, was wir nicht tun.",
     ueber_body, current="ueber.html")

# ---------------------------------------------------------------- Kontakt
kontakt_body = f"""
<section class="section">
  <div class="wrap grid grid--5-7">
    <div>
      <h1>Kontakt</h1>
      <p class="lead">Eine Frage zu einem Ordner, ein Problem mit einer Datei, eine Idee für eine fehlende Seite – schreib einfach.</p>
    </div>
    <div>
      <div class="contact-card">
        <p class="mail"><a href="mailto:{MAIL_SHOP}">{MAIL_SHOP}</a></p>
        <p>Für Fragen zu Produkten, Dateien und Bestellungen. Antwort in der Regel innerhalb von zwei Werktagen. Käufer erreichen uns auch direkt über die Nachrichtenfunktion bei Etsy.</p>
        <p class="mb-0"><a class="btn btn--primary" href="mailto:{MAIL_SHOP}?subject=Frage%20zu%20Kompassordner">E-Mail schreiben</a></p>
      </div>
      <h2 id="start" style="margin-top:48px">Bescheid bekommen, wenn der Shop öffnet</h2>
      <p>Der Etsy-Shop öffnet in Kürze. Wenn du eine kurze Nachricht an <a href="mailto:{MAIL_SHOP}?subject=Bescheid%20geben%2C%20wenn%20der%20Shop%20%C3%B6ffnet">{MAIL_SHOP}</a> schickst, melden wir uns einmal, sobald die Ordner verfügbar sind – keine weiteren Mails, kein Newsletter. Oder folge <a href="{PINTEREST}" rel="noopener">Kompassordner auf Pinterest</a>.</p>
      <h2 style="margin-top:48px">Besondere Situation?</h2>
      <p>Wenn dein Fall nicht ins Raster passt, stellen wir dir einen Ordner aus allen vorhandenen Seiten passend zusammen – eigene Rubriken, angepasste Bezeichnungen, dein Name, deine Farbe. Ab 49 € inklusive einer Korrekturrunde, fertig in drei Werktagen. Schreib kurz, worum es geht, an <a href="mailto:{MAIL_SHOP}?subject=Besondere%20Situation">{MAIL_SHOP}</a>; du bekommst einen Festpreis, bevor du etwas kaufst. Keine Rechtstexte – wir ordnen, wir beraten nicht.</p>
      <h2 style="margin-top:48px">Firmenlizenzen</h2>
      <p>Pflegedienste, Bestatter, Steuerberater, Makler: Für Ordner mit eigenem Logo und eigenen Farben zur Weitergabe an Kunden schreib an <a href="mailto:{MAIL_LIZENZ}">{MAIL_LIZENZ}</a>. Du bekommst innerhalb von zwei Werktagen eine Vorschau mit deinem Logo.</p>
      <h2 style="margin-top:48px">Postanschrift</h2>
      <address class="prose">Kompassordner · Tobias Freudenau<br>Hauptstraße 5<br>04435 Schkeuditz</address>
      <p class="small soft" style="margin-top:16px">Wir verschicken keine gedruckten Ordner – alle Produkte sind digitale Downloads.</p>
    </div>
  </div>
</section>
"""
page("kontakt.html", "Kontakt | Kompassordner",
     "Fragen zu Ordnern, Dateien oder Firmenlizenzen: shop@kompassordner.de. Antwort innerhalb von zwei Werktagen.",
     kontakt_body, current="kontakt.html")

# ---------------------------------------------------------------- Impressum
impressum_body = f"""
<section class="section">
  <div class="wrap prose">
    <h1>Impressum</h1>
    <h2 style="margin-top:24px">Angaben gemäß § 5 DDG</h2>
    <address>
      Tobias Freudenau<br>
      Kompassordner<br>
      Hauptstraße 5<br>
      04435 Schkeuditz<br>
      Deutschland
    </address>
    <h2>Kontakt</h2>
    <p>E-Mail: <a href="mailto:{MAIL_POST}">{MAIL_POST}</a></p>
    <h2>Umsatzsteuer</h2>
    <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: wird nach Erteilung nachgetragen.</p>
    <p>Kleinunternehmer im Sinne von § 19 UStG; Umsatzsteuer wird nicht ausgewiesen.</p>
    <h2>Verantwortlich für den Inhalt</h2>
    <p>Tobias Freudenau, Anschrift wie oben.</p>
    <h2>Verbraucherstreitbeilegung</h2>
    <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen (§ 36 VSBG).</p>
    <h2>Verkauf</h2>
    <p>Der Verkauf der Produkte erfolgt über die Plattform Etsy (Etsy Ireland UC). Für Käufe gelten zusätzlich die Bedingungen von Etsy sowie unsere <a href="widerruf-agb.html">Widerrufsbelehrung und AGB</a>.</p>
    <h2>Urheberrecht</h2>
    <p>Alle Inhalte dieser Website und der angebotenen Vorlagen (Texte, Gestaltung, Logo) sind urheberrechtlich geschützt. Vervielfältigung, Bearbeitung und Verbreitung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung.</p>
    <h2>Haftung für Links</h2>
    <p>Diese Website enthält Links zu externen Websites (Etsy, Pinterest), auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist der jeweilige Anbieter verantwortlich.</p>
  </div>
</section>
"""
page("impressum.html", "Impressum | Kompassordner", "Impressum von Kompassordner, Tobias Freudenau, Schkeuditz – Angaben gemäß § 5 DDG.", impressum_body)

# ---------------------------------------------------------------- Datenschutz
datenschutz_body = f"""
<section class="section">
  <div class="wrap prose">
    <h1>Datenschutzerklärung</h1>
    <p class="lead">Kurz gesagt: Diese Website setzt keine Cookies, nutzt kein Tracking und keine Analyse-Dienste und bindet keine Inhalte von Dritten ein. Beim Aufruf fallen technisch notwendige Server-Protokolle an. Wenn du uns eine E-Mail schreibst, verarbeiten wir sie, um dir zu antworten.</p>
    <p class="small soft">Stand: 08.11.2026</p>

    <h2>1. Verantwortlicher</h2>
    <address>Tobias Freudenau · Kompassordner<br>Hauptstraße 5 · 04435 Schkeuditz<br>E-Mail: <a href="mailto:{MAIL_POST}">{MAIL_POST}</a></address>

    <h2>2. Aufruf der Website (Hosting)</h2>
    <p>Diese Website wird als statische Seite über <strong>GitHub Pages</strong> bereitgestellt, einen Dienst der GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA (eine Tochtergesellschaft der Microsoft Corporation). Beim Aufruf einer Seite verarbeitet GitHub technisch notwendig deine IP-Adresse, Datum und Uhrzeit, die aufgerufene Seite, den verwendeten Browser und das Betriebssystem sowie die zuvor besuchte Seite (Referrer), um die Seite auszuliefern und die Sicherheit des Dienstes zu gewährleisten.</p>
    <p>Rechtsgrundlage ist unser berechtigtes Interesse an einer sicheren und effizienten Bereitstellung der Website (Art. 6 Abs. 1 lit. f DSGVO). GitHub ist nach dem EU-US Data Privacy Framework zertifiziert; die Übermittlung in die USA stützt sich auf den Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO). Weitere Informationen: <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>. Wir selbst haben keinen Zugriff auf diese Protokolldaten.</p>

    <h2>3. Cookies, Tracking, Schriften</h2>
    <p>Wir setzen keine Cookies, keine Analyse- oder Marketing-Werkzeuge und keine Social-Media-Plugins ein. Die verwendete Schrift (Inter) wird von unserem eigenen Webspace geladen; es findet keine Verbindung zu Google Fonts oder anderen Schriftanbietern statt.</p>

    <h2>4. Kontakt per E-Mail</h2>
    <p>Wenn du uns eine E-Mail schreibst, verarbeiten wir deine E-Mail-Adresse, deinen Namen (soweit angegeben) und den Inhalt deiner Nachricht, um deine Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Anbahnung oder Durchführung eines Vertrags) oder Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der Beantwortung von Anfragen). Unsere Postfächer werden bei Microsoft (Exchange Online, Microsoft Ireland Operations Ltd.) auf Servern in der EU betrieben. Wir löschen Anfragen, sobald sie erledigt sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>
    <p>Wenn du uns bittest, dich über die Eröffnung des Shops zu informieren, speichern wir deine E-Mail-Adresse zu diesem Zweck (Art. 6 Abs. 1 lit. a DSGVO), schreiben dir einmal und löschen sie danach. Du kannst die Einwilligung jederzeit per E-Mail widerrufen.</p>

    <h2>5. Käufe über Etsy</h2>
    <p>Unsere Produkte werden über die Plattform Etsy (Etsy Ireland UC, 66/67 Great Strand Street, Dublin 1, Irland) verkauft. Für den Kaufvorgang, dein Etsy-Konto, Zahlungen und Cookies auf Etsy ist Etsy als eigener Verantwortlicher zuständig; es gilt die <a href="https://www.etsy.com/de/legal/privacy" rel="noopener">Datenschutzerklärung von Etsy</a>. Welche Daten wir als Verkäufer von Etsy erhalten und wie wir sie verarbeiten, erläutern wir in unserem Datenschutzhinweis im Etsy-Shop und unter <a href="widerruf-agb.html#datenschutz-shop">Widerruf und AGB</a>.</p>

    <h2>6. Links zu anderen Websites</h2>
    <p>Diese Website verlinkt auf Etsy und Pinterest. Beim Klick auf einen solchen Link verlässt du unsere Website; es gelten die Datenschutzbestimmungen des jeweiligen Anbieters. Wir binden keine Inhalte dieser Dienste direkt ein.</p>

    <h2>7. Deine Rechte</h2>
    <p>Du hast das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch gegen Verarbeitungen auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (Art. 21). Eine erteilte Einwilligung kannst du jederzeit mit Wirkung für die Zukunft widerrufen. Wende dich dafür an <a href="mailto:{MAIL_POST}">{MAIL_POST}</a>.</p>
    <p>Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Für uns zuständig: Sächsische Datenschutz- und Transparenzbeauftragte, Devrientstraße 5, 01067 Dresden.</p>

    <h2>8. Änderungen</h2>
    <p>Wir passen diese Erklärung an, wenn sich die Website oder die Rechtslage ändert. Es gilt die jeweils hier veröffentlichte Fassung.</p>
  </div>
</section>
"""
page("datenschutz.html", "Datenschutzerklärung | Kompassordner", "Datenschutz auf kompassordner.de: keine Cookies, kein Tracking, Hosting über GitHub Pages, Kontakt per E-Mail, Käufe über Etsy.", datenschutz_body)

# ---------------------------------------------------------------- Widerruf & AGB
widerruf_body = f"""
<section class="section">
  <div class="wrap prose">
    <h1>Widerrufsbelehrung und AGB</h1>
    <p class="lead">Unsere Produkte werden über Etsy verkauft. Diese Texte gelten für Käufe im Etsy-Shop „Kompassordner“ und sind dort ebenfalls hinterlegt. Stand: 07.11.2026.</p>

    <h2 id="widerruf">Widerrufsbelehrung für digitale Inhalte</h2>
    <h3>Widerrufsrecht</h3>
    <p>Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gründen diesen Vertrag zu widerrufen. Die Widerrufsfrist beträgt vierzehn Tage ab dem Tag des Vertragsschlusses.</p>
    <p>Um Ihr Widerrufsrecht auszuüben, müssen Sie uns (Tobias Freudenau, Kompassordner, Hauptstraße 5, 04435 Schkeuditz, E-Mail {MAIL_POST}) mittels einer eindeutigen Erklärung (z. B. ein mit der Post versandter Brief oder eine E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen, informieren. Sie können dafür das unten stehende Muster-Widerrufsformular verwenden, das jedoch nicht vorgeschrieben ist. Zur Wahrung der Widerrufsfrist reicht es aus, dass Sie die Mitteilung über die Ausübung des Widerrufsrechts vor Ablauf der Widerrufsfrist absenden.</p>
    <h3>Folgen des Widerrufs</h3>
    <p>Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, unverzüglich und spätestens binnen vierzehn Tagen ab dem Tag zurückzuzahlen, an dem die Mitteilung über Ihren Widerruf dieses Vertrags bei uns eingegangen ist. Für diese Rückzahlung verwenden wir dasselbe Zahlungsmittel, das Sie bei der ursprünglichen Transaktion eingesetzt haben, es sei denn, mit Ihnen wurde ausdrücklich etwas anderes vereinbart; in keinem Fall werden Ihnen wegen dieser Rückzahlung Entgelte berechnet.</p>
    <h3>Vorzeitiges Erlöschen des Widerrufsrechts</h3>
    <p>Bei einem Vertrag über die Lieferung von nicht auf einem körperlichen Datenträger befindlichen digitalen Inhalten erlischt das Widerrufsrecht gemäß § 356 Abs. 5 BGB, wenn wir mit der Ausführung des Vertrags begonnen haben, nachdem Sie ausdrücklich zugestimmt haben, dass wir vor Ablauf der Widerrufsfrist mit der Ausführung beginnen, und Sie Ihre Kenntnis davon bestätigt haben, dass Sie durch Ihre Zustimmung mit Beginn der Ausführung Ihr Widerrufsrecht verlieren. Die Zustimmung und Bestätigung erfolgen über die von Etsy vor Abschluss der Bestellung bereitgestellte Checkbox. Wir bestätigen Ihnen das Erlöschen in der Bestellbestätigung.</p>
    <h3>Muster-Widerrufsformular</h3>
    <p>(Wenn Sie den Vertrag widerrufen wollen, füllen Sie bitte dieses Formular aus und senden Sie es zurück.)</p>
    <p>An: Tobias Freudenau, Kompassordner, Hauptstraße 5, 04435 Schkeuditz, {MAIL_POST}<br>
    Hiermit widerrufe(n) ich/wir (*) den von mir/uns (*) abgeschlossenen Vertrag über den Kauf der folgenden Waren (*)/die Erbringung der folgenden Dienstleistung (*)<br>
    Bestellt am (*)/erhalten am (*): ______<br>
    Name des/der Verbraucher(s): ______<br>
    Anschrift des/der Verbraucher(s): ______<br>
    Unterschrift des/der Verbraucher(s) (nur bei Mitteilung auf Papier): ______<br>
    Datum: ______<br>
    (*) Unzutreffendes streichen.</p>

    <h2 id="agb">Allgemeine Geschäftsbedingungen</h2>
    <h3>1. Geltungsbereich</h3>
    <p>Diese AGB gelten für alle Verträge über digitale Inhalte (PDF-Vorlagen, Ordner, Checklisten), die Tobias Freudenau, Kompassordner, Hauptstraße 5, 04435 Schkeuditz (nachfolgend „Anbieter“), über die Plattform Etsy mit Verbrauchern und Unternehmern (nachfolgend „Kunde“) schließt. Ergänzend gelten die Nutzungsbedingungen von Etsy.</p>
    <h3>2. Vertragsschluss</h3>
    <p>Die Produktdarstellungen im Shop sind kein verbindliches Angebot, sondern eine Aufforderung zur Bestellung. Mit dem Abschluss des Bestellvorgangs über den Button „Kaufen“ bzw. „Bezahlen“ gibt der Kunde ein verbindliches Angebot ab. Der Vertrag kommt mit der Bestellbestätigung von Etsy bzw. der Bereitstellung des Downloads zustande. Vertragssprache ist Deutsch.</p>
    <h3>3. Lieferung digitaler Inhalte</h3>
    <p>Die Lieferung erfolgt ausschließlich als Download über Etsy. Nach Zahlungseingang stehen die Dateien im Etsy-Konto des Kunden unter „Käufe und Bewertungen“ sowie über den Link in der Bestellbestätigung zur Verfügung. Es wird kein körperlicher Datenträger und kein gedrucktes Exemplar versandt. Für die Nutzung der ausfüllbaren PDF-Dateien wird ein aktueller PDF-Reader (z. B. Adobe Acrobat Reader) benötigt; Browser zeigen Formularfelder nicht immer vollständig an.</p>
    <h3>4. Nutzungsrecht</h3>
    <p>Der Kunde erhält ein einfaches, nicht übertragbares, zeitlich unbegrenztes Recht, die erworbenen Dateien für private Zwecke zu nutzen, auszudrucken und auszufüllen – auch mehrfach und für Angehörige im eigenen Haushalt. Nicht gestattet sind Weiterverkauf, Weitergabe, Veröffentlichung, Vermietung, das Anbieten als Download sowie die gewerbliche Nutzung (z. B. Weitergabe an Kunden, Mandanten oder Patienten). Für die gewerbliche Nutzung bietet der Anbieter gesonderte Firmenlizenzen an. Urheberrechtsvermerke dürfen nicht entfernt werden.</p>
    <h3>5. Preise und Zahlung</h3>
    <p>Es gelten die im Shop angegebenen Preise. Der Anbieter ist Kleinunternehmer im Sinne von § 19 UStG und weist keine Umsatzsteuer aus. Bei digitalen Sofort-Downloads tritt Etsy als Verkäufer gegenüber dem Kunden auf und erhebt und führt die im Land des Kunden geltende Umsatzsteuer ab; der angezeigte Endpreis enthält diese. Die Zahlung erfolgt über die von Etsy angebotenen Zahlungsarten.</p>
    <h3>6. Widerrufsrecht</h3>
    <p>Verbrauchern steht ein Widerrufsrecht nach Maßgabe der Widerrufsbelehrung zu. Bei digitalen Inhalten erlischt das Widerrufsrecht mit Beginn der Bereitstellung, wenn der Kunde dem vor dem Kauf ausdrücklich zugestimmt und seine Kenntnis vom Verlust des Widerrufsrechts bestätigt hat.</p>
    <h3>7. Gewährleistung und Aktualisierungen</h3>
    <p>Es gelten die gesetzlichen Gewährleistungsrechte für digitale Produkte (§§ 327 ff. BGB). Lässt sich eine Datei nicht öffnen oder ist sie fehlerhaft, stellt der Anbieter nach Mitteilung unverzüglich eine funktionsfähige Fassung bereit. Aktualisierungen der Vorlagen (z. B. bei geänderten Fristen oder Zuständigkeiten) werden über den Etsy-Downloadbereich kostenlos bereitgestellt, solange das Produkt angeboten wird.</p>
    <h3>8. Haftung und Hinweis zum Inhalt</h3>
    <p>Die Vorlagen dienen der Dokumentation und Organisation. Sie ersetzen keine Rechts-, Steuer- oder medizinische Beratung und keine notariell beurkundeten Dokumente. Angaben zu Fristen, Beträgen und Zuständigkeiten sind mit Stand der jeweiligen Version zusammengestellt und können sich ändern. Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit sowie bei Verletzung von Leben, Körper und Gesundheit. Bei leicht fahrlässiger Verletzung wesentlicher Vertragspflichten ist die Haftung auf den vertragstypischen, vorhersehbaren Schaden begrenzt; im Übrigen ist die Haftung für leichte Fahrlässigkeit ausgeschlossen. Die Haftung nach dem Produkthaftungsgesetz bleibt unberührt.</p>
    <h3>9. Streitbeilegung und Schlussbestimmungen</h3>
    <p>Der Anbieter ist nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen (§ 36 VSBG). Es gilt deutsches Recht unter Ausschluss des UN-Kaufrechts; für Verbraucher mit gewöhnlichem Aufenthalt im Ausland bleiben zwingende Verbraucherschutzvorschriften ihres Aufenthaltsstaats unberührt. Sollte eine Bestimmung unwirksam sein, bleibt der übrige Vertrag wirksam.</p>

    <h2 id="datenschutz-shop">Datenschutzhinweis für Käufe über Etsy</h2>
    <p>Verantwortlicher: Tobias Freudenau, Kompassordner, Hauptstraße 5, 04435 Schkeuditz, {MAIL_POST}.</p>
    <p><strong>Welche Daten wir erhalten:</strong> Bei einer Bestellung übermittelt Etsy uns Ihren Namen, Ihren Etsy-Nutzernamen, Ihre Bestelldaten und – soweit angegeben – Ihre Nachricht. Für personalisierte Produkte verarbeiten wir zusätzlich die von Ihnen angegebenen Personalisierungsdaten (z. B. Name, Firmenname, Logo, Farbangaben).</p>
    <p><strong>Zwecke und Rechtsgrundlagen:</strong> Vertragserfüllung und Lieferung der digitalen Inhalte, Kundenservice und Beantwortung von Anfragen (Art. 6 Abs. 1 lit. b DSGVO); Erfüllung steuer- und handelsrechtlicher Aufbewahrungspflichten (Art. 6 Abs. 1 lit. c DSGVO); Verteidigung von Rechtsansprüchen (Art. 6 Abs. 1 lit. f DSGVO).</p>
    <p><strong>Empfänger:</strong> Etsy Ireland UC (Plattform und Zahlungsabwicklung), unser Steuerberater und – bei Zahlungsabwicklung – unsere Bank. Eine darüber hinausgehende Weitergabe findet nicht statt; eine Nutzung für Werbung erfolgt nicht.</p>
    <p><strong>Speicherdauer:</strong> Bestell- und Rechnungsdaten werden nach den gesetzlichen Fristen (derzeit 8 Jahre für Buchungsbelege, 10 Jahre für Handels- und Geschäftsbriefe) aufbewahrt; Personalisierungsdaten löschen wir spätestens 3 Monate nach Lieferung, Nachrichten nach Abschluss der Anfrage, soweit keine Aufbewahrungspflicht besteht.</p>
    <p><strong>Ihre Rechte:</strong> Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit, Widerspruch gegen Verarbeitungen auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO sowie Beschwerde bei einer Datenschutzaufsichtsbehörde, für uns zuständig: Sächsische Datenschutz- und Transparenzbeauftragte, Dresden.</p>
    <p>Für die Datenverarbeitung durch Etsy selbst (Konto, Zahlung, Cookies) gilt die Datenschutzerklärung von Etsy.</p>

    <h2 id="lizenz">Lizenzbedingungen</h2>
    <p><strong>Privatlizenz (Standard und Personalisiert):</strong> Nutzung, Ausdruck und Ausfüllen für den eigenen privaten Gebrauch und innerhalb der eigenen Familie, unbegrenzt oft. Keine Weitergabe der Dateien an Dritte, kein Verkauf, keine Veröffentlichung, keine Nutzung in gewerblichen Zusammenhängen.</p>
    <p><strong>Firmenlizenz Basis (ein Standort):</strong> Nutzung der mit Ihrem Logo und Ihren Farben personalisierten Fassung durch Ihr Unternehmen zur Weitergabe an eigene Kunden, Mandanten, Patienten oder Mitarbeitende, gedruckt oder als PDF, unbegrenzte Stückzahl, am genannten Standort. Kein Weiterverkauf als eigenständiges Produkt, keine Unterlizenzierung, keine Bearbeitung des Inhalts über die vereinbarte Personalisierung hinaus. Der Urhebervermerk „Vorlage: Kompassordner“ bleibt in der Fußzeile.</p>
    <p><strong>Firmenlizenz Plus (alle Standorte / Verbund):</strong> wie Basis, zusätzlich für alle Standorte, Niederlassungen oder Mitgliedseinrichtungen eines Unternehmens bzw. Verbands.</p>
    <p><strong>Für alle Lizenzen:</strong> Die Lizenz ist zeitlich unbegrenzt und gilt für die gelieferte Version einschließlich kostenloser Aktualisierungen. Urheberrecht und alle nicht ausdrücklich eingeräumten Rechte verbleiben bei Tobias Freudenau, Kompassordner. Bei Verstoß erlischt die Lizenz; weitergehende Ansprüche bleiben vorbehalten.</p>
  </div>
</section>
"""
page("widerruf-agb.html", "Widerrufsbelehrung und AGB | Kompassordner", "Widerrufsbelehrung für digitale Inhalte, Allgemeine Geschäftsbedingungen, Datenschutzhinweis für Käufe über Etsy und Lizenzbedingungen von Kompassordner.", widerruf_body)

# ---------------------------------------------------------------- 404
page("404.html", "Seite nicht gefunden | Kompassordner", "Diese Seite gibt es nicht.", """
<section class="section center">
  <div class="wrap">
    <h1>Diese Seite gibt es nicht</h1>
    <p class="lead" style="margin-inline:auto">Vielleicht ist der Link alt oder vertippt. Hier geht es weiter:</p>
    <div class="actions" style="justify-content:center"><a class="btn btn--primary" href="index.html">Zur Startseite</a><a class="btn btn--secondary" href="produkte.html">Zu den Ordnern</a></div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Technik
open("CNAME", "w").write("www.kompassordner.de\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
today = datetime.date.today().isoformat()
pages = ["", "produkte.html", "so-funktioniert-es.html", "ueber.html", "kontakt.html", "impressum.html", "datenschutz.html", "widerruf-agb.html"]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{SITE}/{p}</loc><lastmod>{today}</lastmod></url>\n" for p in pages) + "</urlset>\n")
open(".nojekyll", "w").write("")
print("ok", len(pages), "Seiten")

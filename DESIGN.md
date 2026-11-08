# DESIGN.md — kompassordner.de

Version 1.0 · 08.11.2026 · Grundlage: Markenprofil Kompassordner V1.0, Logo-Paket V1.0.
Hinweis: Richtung ohne UXKIN-Vergleich festgelegt (nicht verbunden); sie beruht auf dem bestehenden Markensystem der Produkte (PDF-Ordner) und dem Logo.

## Idee

Die Seite ist der Ordner. Alles, was Besucher sehen, kommt aus der Welt des Aktenordners:
der dunkelblaue Deckel (Navy-Flächen), das Rückenschild aus Kupfer (dünne Kupferlinie als
Strukturelement), das Papier (Sand). Das eine mutige Element ist das **Register**: Inhalte,
die wirklich eine Reihenfolge haben (Teile A–I eines Ordners, die drei Schritte), werden als
Registerkarten mit Buchstaben/Seitenzahlen gezeigt – wie die Trennblätter im echten Ordner.
Alles andere bleibt ruhig: keine Verläufe, keine Glas-Effekte, keine drei gleichen Karten,
keine Icons als Dekoration, keine Animation beim Laden.

Zielgruppe 50+: Grundschrift 18 px, Zeilenlänge ≤ 70 Zeichen, Kontrast ≥ 7:1 im Fließtext,
Klickflächen ≥ 48 px, Links unterstrichen, Fokus deutlich sichtbar, keine Hamburger-Menüs
(die Navigation bleibt immer sichtbar und bricht auf dem Handy in zwei Zeilen um).

## Farben (Rollen)

| Token | Wert | Rolle |
|---|---|---|
| `--navy` | #1F3A5F | Primärfläche (Hero, Fußzeile), Überschriften, primäre Buttons |
| `--navy-deep` | #17304F | Deckel-Abstufung: Hover auf Navy, Registerkanten |
| `--copper` | #B86B45 | Akzent: Kupferlinie, Registerbuchstaben, Link-Hover, Fokusring |
| `--copper-deep` | #8F4F30 | Hover des Akzents, Text in Kupfer auf Sand (Kontrast 5,1:1) |
| `--sand` | #F3EDE3 | Seitenhintergrund (Papier) |
| `--sand-deep` | #E6DCCB | Flächen auf Sand (Produktkarten-Hintergrund, Tabellenzeilen) |
| `--paper` | #FFFFFF | Dokumentfläche hinter Produktseiten-Bildern |
| `--ink` | #2A2A2A | Fließtext |
| `--ink-soft` | #4F5560 | Nebentext, Bildunterschriften (Kontrast 6,9:1 auf Sand) |
| `--line` | #D6CBB8 | Trennlinien auf Sand |
| `--ok` | #2E6B4F | Häkchen „enthalten“, Erfolg |
| `--warn` | #8A5A00 | Hinweise (Rechtsstand) |
| `--error` | #9B2C2C | Fehler |

Kein Dark Mode (Druck-/Papier-Metapher; die Zielgruppe liest helle Seiten besser).

## Typografie

Eine Familie: **Inter** (selbst gehostet, woff2, Regular 400 / Medium 500 / SemiBold 600),
Fallback system-ui. Ziffern tabellarisch (`tnum`) in Preisen und Tabellen.

| Stufe | Größe / Zeilenhöhe | Gewicht | Einsatz |
|---|---|---|---|
| display | clamp(2.25rem, 1.5rem + 3vw, 3.5rem) / 1.08 | 600, -0.02em | H1 im Hero |
| h2 | clamp(1.75rem, 1.3rem + 1.6vw, 2.5rem) / 1.15 | 600, -0.015em | Abschnittstitel |
| h3 | 1.375rem / 1.25 | 600 | Produktnamen, Unterabschnitte |
| lead | 1.25rem / 1.5 | 400 | Einleitungssatz unter H1/H2 |
| body | 1.125rem (18 px) / 1.6 | 400 | Fließtext |
| small | 1rem / 1.5 | 400 | Bildunterschriften, Fußzeile |
| tab | 0.9375rem / 1.2 | 600, +0.04em | Registerbuchstaben, Preisschilder |

Keine Versalien-Labels über Überschriften, kein eingefärbtes Einzelwort in Überschriften
(Ausnahme: die Wortmarke selbst, in der „ordner“ kupferfarben ist – das ist das Logo).

## Abstände und Raster

8-px-Skala: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128.
Inhaltsbreite 1120 px, Textspalte 68ch. Abschnittsabstand 96 px (Handy 64 px).
Links ausgerichtet; nichts zentriert außer der 404-Seite.

## Form und Tiefe

Radius: 4 px (Buttons, Register), 8 px (Bild-Rahmen). Keine Schatten außer dem
Kontaktschatten unter Produktbildern (`0 24px 40px -28px rgba(31,58,95,.35)`), der die
Perspektive des Logos aufnimmt.

## Komponenten

- **Kopf**: Wortmarke links (SVG), Navigation rechts: Produkte · So funktioniert es · Über · Kontakt. Auf dem Handy unter der Wortmarke, zweizeilig, immer sichtbar.
- **Kupferlinie**: 4 px Kupfer am oberen Seitenrand (das Rückenschild) – einziges Dekor.
- **Button primär**: Navy-Fläche, Sand-Text, 16/28 px Innenabstand, min. 48 px hoch, Hover navy-deep, Fokus 3 px Kupferring mit 2 px Abstand. Text sagt, was passiert: „Zum Shop auf Etsy“, „Schreib uns eine E-Mail“.
- **Button sekundär**: Navy-Rahmen 2 px, Navy-Text, gleicher Hover-Ring.
- **Links im Text**: Navy, unterstrichen (2 px Offset), Hover Kupfer.
- **Register**: Liste aus Zeilen `A │ Im Notfall │ S. 4–8`, Buchstabe in Kupfer auf Sand-deep-Kärtchen, Linien dazwischen. Nur für echte Reihenfolgen.
- **Produktblock**: zweispaltig ab 768 px (Bild 5/12, Text 7/12), auf dem Handy Bild zuerst. Preis als Zeile „19,90 € (Einführungspreis, regulär 24,90 €)“ in Tabellenziffern.
- **Hinweisbox**: Sand-deep-Fläche, 4 px Kupferlinie links; für Rechtsstand/„keine Beratung“.
- **Fußzeile**: Navy, Sand-Text; Spalten: Wortmarke + Satz, Seiten, Rechtliches, Kontakt.

## Bilder

Nur echte Produktseiten (PNG aus den PDFs, 110 dpi), auf Papierfläche mit 8-px-Radius
und Kontaktschatten; alt-Text beschreibt die gezeigte Seite. Keine Stockfotos, keine
KI-Personen. Logo nur aus dem Logo-Paket, nie verzerrt.

## Bewegung

Keine automatische Bewegung. Hover/Fokus-Übergänge 120 ms; `prefers-reduced-motion` schaltet sie ab.

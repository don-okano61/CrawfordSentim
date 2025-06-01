Super, dass es jetzt funktioniert! 😊 Hier ist eine **README-Datei**, die das Projekt beschreibt und auch die Fehlerbehebungen berücksichtigt.

---

### 📄 **README.md für dein Web-Crawler-NLP-Projekt**

```md
# Web Crawler & NLP mit spaCy & Hugging Face

## 📌 Projektbeschreibung
Dieses Python-Projekt implementiert einen **Web-Crawler**, der Box-News von `Boxing News 24` extrahiert und mit **spaCy** oder **Hugging Face** **Named Entity Recognition (NER)** durchführt. Zusätzlich simuliert es einen Kampf zwischen **Terence Crawford und Canelo Alvarez** basierend auf Statistiken.

## 🚀 Features
- **Web-Crawling**: Extrahiert Box-Artikel von `https://www.boxingnews24.com/`
- **Named Entity Recognition (NER)**:
  - **spaCy**: Erkennung von Namen, Organisationen, Events
  - **Hugging Face**: Tiefere NLP-Analyse mit BERT-Modellen
- **Kampfsimulation**: Berechnung der Sieg-Wahrscheinlichkeit von Crawford vs. Canelo

## 🛠️ Installation
1. **Python 3.x installieren**
2. Benötigte Bibliotheken installieren:
   ```bash
   pip install requests beautifulsoup4 spacy torch transformers pandas
   ```

3. **spaCy-Modell herunterladen**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🔧 Fehlerbehebungen
Falls Fehler auftreten, hier einige Korrekturen:
- **spaCy-Modell kann nicht geladen werden**:
  ```bash
  python -m spacy validate
  python -m spacy download en_core_web_sm
  ```
- **Hugging Face NER funktioniert nicht**:
  ```bash
  pip install torch torchvision torchaudio
  pip install tensorflow>=2.0
  ```

## 📝 Code-Beispiel
```python
import requests
from bs4 import BeautifulSoup
import spacy
from transformers import pipeline

nlp_spacy = spacy.load("en_core_web_sm")
ner_huggingface = pipeline("ner", model="dslim/bert-base-NER")

url = "https://www.boxingnews24.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = " ".join([p.text for p in soup.find_all("p")])

# Named Entity Recognition mit spaCy
doc = nlp_spacy(text)
print("NER mit spaCy:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Named Entity Recognition mit Hugging Face
entities = ner_huggingface(text)
print("NER mit Hugging Face:")
for ent in entities:
    print(f"{ent['word']} - {ent['entity']}")
```

## 📊 Kampf-Simulation: Crawford vs. Canelo
Das Skript berechnet eine Wahrscheinlichkeitsverteilung basierend auf:
- **Geschwindigkeit**
- **Power**
- **Verteidigung**

Die Simulation bestimmt den Sieger basierend auf diesen Werten.

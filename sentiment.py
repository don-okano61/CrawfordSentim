import requests
from bs4 import BeautifulSoup
import spacy
from transformers import pipeline
import random

# NLP-Modelle laden
nlp_spacy = spacy.load("en_core_web_sm")
ner_huggingface = pipeline("ner", model="dslim/bert-base-NER")

# Webseite crawlen
url = "https://www.boxingnews24.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Text extrahieren
text = " ".join([p.text for p in soup.find_all("p")])

# Named Entity Recognition mit spaCy
doc = nlp_spacy(text)
entities_spacy = [(ent.text, ent.label_) for ent in doc.ents]

# Named Entity Recognition mit Hugging Face
entities_huggingface = ner_huggingface(text)

# Erkannte Entitäten anzeigen
print("\n🔍 Erkannte Entitäten mit spaCy:")
for ent in entities_spacy:
    print(f"{ent[0]} - {ent[1]}")

print("\n🔍 Erkannte Entitäten mit Hugging Face:")
for ent in entities_huggingface:
    print(f"{ent['word']} - {ent['entity']}")

# Kampf-Simulation: Crawford vs. Canelo
crawford_stats = {"name": "Terence Crawford", "speed": 9.5, "power": 8.9, "defense": 9.2}
canelo_stats = {"name": "Canelo Alvarez", "speed": 8.7, "power": 9.5, "defense": 9.0}

# Wahrscheinlichkeit berechnen
crawford_chance = (crawford_stats["speed"] + crawford_stats["defense"]) / (canelo_stats["speed"] + canelo_stats["defense"])
canelo_chance = 1 - crawford_chance

winner = random.choices(["Terence Crawford", "Canelo Alvarez"], weights=[crawford_chance, canelo_chance])[0]

print(f"\n🏆 Vorhersage: Der Sieger wird voraussichtlich **{winner}** sein!")

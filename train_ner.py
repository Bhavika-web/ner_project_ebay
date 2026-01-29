import spacy
from spacy.training import Example
import random
from spacy.util import minibatch, compounding

# Expanded training data to fix mislabeling from your images
TRAIN_DATA = [
    ("BMW 320d DPF Touring", {"entities": [(0, 3, "BRAND"), (4, 8, "MODEL"), (9, 12, "FEATURE"), (13, 20, "BODY_TYPE")]}),
    ("Audi A4 1.9 TDI quattro", {"entities": [(0, 4, "BRAND"), (5, 7, "MODEL"), (8, 11, "ENGINE"), (12, 15, "FUEL"), (16, 23, "DRIVE")]}),
    ("Opel Astra G Cabrio Turbo 235 PS", {"entities": [(0, 4, "BRAND"), (5, 10, "MODEL"), (11, 12, "MODEL"), (13, 19, "BODY_TYPE"), (20, 25, "FEATURE"), (26, 29, "POWER"), (30, 32, "POWER")]}),
    ("Honda Civic 2016 Front Bumper", {"entities": [(0, 5, "BRAND"), (6, 11, "MODEL"), (12, 16, "YEAR"), (17, 22, "PART"), (23, 29, "PART")]}),
    ("ABS Plastic Black OEM", {"entities": [(0, 3, "MATERIAL"), (4, 11, "MATERIAL"), (12, 17, "COLOR"), (18, 21, "TYPE")]}),
    # Negative examples: Tell the model what NOT to label as a car brand
    ("Fast shipping worldwide", {"entities": []}),
    ("Available in all colors", {"entities": []})
]

def train_model():
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")

    # Auto-add all labels from TRAIN_DATA
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    optimizer = nlp.begin_training()
    
    print("🚀 Step 2: Training AI (100 epochs)...")
    for epoch in range(100):
        random.shuffle(TRAIN_DATA)
        losses = {}
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            for text, ann in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, ann)
                nlp.update([example], drop=0.2, losses=losses)
    
    nlp.to_disk("ner_model")
    print("✅ Step 2: Model saved as 'ner_model'")

if __name__ == "__main__":
    train_model()
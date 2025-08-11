from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "SophieTr/xlm-roberta-base-claim-detection-clef21-24"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, force_download=True)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, force_download=True)

print("Model and tokenizer loaded successfully!")

import streamlit as st
import spacy
import os

# Load model safely
if os.path.exists("ner_model"):
    nlp = spacy.load("ner_model")
else:
    st.error("⚠️ Model not found! Run 'python train_ner.py' first.")
    st.stop()

st.set_page_config(page_title="eBay Car NER", layout="centered")

# Visual Styling for all labels
st.markdown("""
<style>
.entity { display:inline-block; padding:5px 12px; border-radius:18px; margin:4px; font-weight:bold; color:white; }
.BRAND{background:#2563eb;} .MODEL{background:#7c3aed;} .FEATURE{background:#dc2626;}
.BODY_TYPE{background:#059669;} .POWER{background:#f59e0b;} .YEAR{background:#64748b;}
.PART{background:#0ea5e9;} .MATERIAL{background:#94a3b8;} .COLOR{background:#1e293b;}
</style>
""", unsafe_allow_html=True)

st.title("🚗 eBay Car Title Analyzer")
text = st.text_input("Enter eBay car title:")

if text:
    # THE FIX: Replace underscores so the model recognizes separate words
    clean_text = text.replace("_", " ") 
    
    doc = nlp(clean_text)
    
    if not doc.ents:
        st.info("No entities detected in this specific text.")
    
    for ent in doc.ents:
        st.markdown(
            f"<span class='entity {ent.label_}'>{ent.text} ({ent.label_})</span>",
            unsafe_allow_html=True
        )
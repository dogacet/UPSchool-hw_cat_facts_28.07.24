import streamlit as st
import requests
import sqlite3

# 1. Streamlit Başlığı
st.title("Cat Facts")

# 2. API İsteği Gönderme ve JSON Verisini Alma Fonksiyonu
def get_cat_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    return response.json()

# 3. SQLite Veritabanı Oluşturma ve Veri Kaydetme Fonksiyonu
def save_cat_facts_to_db(cat_facts):
    conn = sqlite3.connect('cat_facts.db')
    c = conn.cursor()

    # Cat facts tablosunu oluşturma
    c.execute('''
              CREATE TABLE IF NOT EXISTS cat_facts
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              text TEXT)
              ''')

    conn.commit()

    # Alınan veriyi veritabanına ekleme
    for fact in cat_facts:
        c.execute("INSERT INTO cat_facts (text) VALUES (?)", (fact['text'],))

    conn.commit()
    conn.close()

# 4. Veritabanındaki Verileri Görüntüleme Fonksiyonu
def get_cat_facts_from_db():
    conn = sqlite3.connect('cat_facts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cat_facts")
    rows = c.fetchall()
    conn.close()
    return rows

# 5. Kullanıcı Arayüzü Elemanları
if st.button("Fetch Cat Facts"):
    cat_facts = get_cat_facts()
    save_cat_facts_to_db(cat_facts)
    st.success("Cat facts fetched and saved to database!")

if st.button("Show Cat Facts"):
    rows = get_cat_facts_from_db()
    for row in rows:
        st.write(row[1])


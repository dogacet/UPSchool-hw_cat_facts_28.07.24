import requests
import sqlite3

# 1. API İsteği Gönderme ve JSON Verisini Alma
url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(url)
cat_facts = response.json()

# API yanıtının yapısını kontrol etme
print(cat_facts)  # Bu satırı çalıştırarak yanıt yapısını kontrol edin

# 2. SQLite Veritabanı Oluşturma
conn = sqlite3.connect('cat_facts.db')
c = conn.cursor()

# Cat facts tablosunu oluşturma
c.execute('''
          CREATE TABLE IF NOT EXISTS cat_facts
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT)
          ''')

conn.commit()

# 3. API'den Alınan Veriyi SQLite Veritabanına Kaydetme
# Alınan veriyi veritabanına ekleme
for fact in cat_facts:
    c.execute("INSERT INTO cat_facts (text) VALUES (?)", (fact['text'],))

conn.commit()

# 4. Veritabanına Kaydedilen Kedi Fact'lerini Görüntüleme
# Veritabanındaki tüm kedi fact'lerini görüntüleme
c.execute("SELECT * FROM cat_facts")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()

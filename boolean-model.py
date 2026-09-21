import random

# Rastgele ama kontrollü bir kelime havuzu (Boolean aramalar için idealdir)
kategori_havuzu = {
    "ir": ["bilgi", "erişimi", "arama", "motoru", "indeks", "sorgu"],
    "ai": ["yapay", "zeka", "makine", "öğrenmesi", "derin", "model"],
    "dev": ["python", "programlama", "veri", "bilimi", "kod", "algoritma"],
    "web": ["web", "teknolojileri", "internet", "tasarım", "sayfa", "sunucu"],
    "spor": ["spor", "futbol", "basketbol", "maç", "takım", "lig"]
}

# 100 Dokümanlık Veri Setini Otomatik Oluşturma
documents = {}
random.seed(42)  # Her çalıştırmada aynı 100 dokümanı üretmek için

for doc_id in range(1, 101):
    # Rastgele bir kategori seç
    kat_key = random.choice(list(kategori_havuzu.keys()))
    kelimeler = kategori_havuzu[kat_key]

    # O kategoriden rastgele 2 ila 4 kelime alıp bir metin (doküman) oluşturalım
    secilen_kelimeler = random.sample(kelimeler, k=random.randint(2, 4))
    documents[doc_id] = " ".join(secilen_kelimeler)

# Üretilen veri setinden ilk 5 örneği görelim:
print("Örnek Dokümanlar (İlk 5 tanesi):")
for doc_id in list(documents.keys())[:5]:
    print(f"Doc {doc_id}: {documents[doc_id]}")

print(f"\nToplam Doküman Sayısı: {len(documents)}")


# Örnek Doküman Koleksiyonu
documents_ = {
    1: "bilgi erişimi ve arama motorları",
    2: "doğal dil işleme ve bilgi erişimi",
    3: "makine öğrenmesi ve yapay zeka",
    4: "arama motorları ve web teknolojileri"
}

# 1. Koleksiyondaki tüm benzersiz kelimelerden oluşan Sözlük (Vocabulary)
all_terms = sorted(list(set(text for doc in documents.values() for text in doc.lower().split())))
print("Sözlük (Vocabulary):", all_terms)

# Doküman ID'lerini sıralı bir liste olarak tutalım
doc_ids = sorted(list(documents.keys()))

# 2. Boolean Vektör Matrisi (Term-Document Incidence Matrix) Oluşturma
# Her kelime için, tüm belgeleri temsil eden bir 0 ve 1 vektörü oluşturuyoruz.
term_vectors = {}
for term in all_terms:
    vector = []
    for doc_id in doc_ids:
        doc_text = documents[doc_id].lower()
        # Kelime bu belgede geçiyorsa 1, geçmiyorsa 0 ekle
        if term in doc_text.split():
            vector.append(1)
        else:
            vector.append(0)
    term_vectors[term] = vector

print("\nBoolean Vektörler Matrisi:")
for term, vec in term_vectors.items():
    print(f"{term:12}: {vec}")

# 3. Vektör Tabanlı Boolean Arama Fonksiyonları
def vector_and(term1, term2):
    """İki kelimenin vektörleri arasında eleman bazlı AND (ve) işlemi yapar."""
    v1 = term_vectors.get(term1, [0] * len(doc_ids))
    v2 = term_vectors.get(term2, [0] * len(doc_ids))
    # zip() ile aynı indeksteki elemanları eşleyip bitwise AND (&) yapıyoruz
    return [a & b for a, b in zip(v1, v2)]

def vector_or(term1, term2):
    """İki kelimenin vektörleri arasında eleman bazlı OR (veya) işlemi yapar."""
    v1 = term_vectors.get(term1, [0] * len(doc_ids))
    v2 = term_vectors.get(term2, [0] * len(doc_ids))
    return [a | b for a, b in zip(v1, v2)]

# Sonuç vektörünü (örn: [1, 0, 0]) Doküman ID'lerine (örn: [1]) çeviren yardımcı fonksiyon
def get_matching_docs(result_vector):
    return [doc_ids[i] for i, val in enumerate(result_vector) if val == 1]

# --- TEST KÖŞESİ ---
print("\n--- Vektör Tabanlı Arama Örnekleri ---")

# Örnek 1: "bilgi" AND "arama"
res_and = vector_and("bilgi", "arama")
matching_docs_and = get_matching_docs(res_and)
print(f"'bilgi' AND 'arama' sonuç vektörü: {res_and} -> Eşleşen Dokümanlar: {matching_docs_and}")

# Örnek 2: "doğal" OR "makine"
res_or = vector_or("doğal", "makine")
matching_docs_or = get_matching_docs(res_or)
print(f"'doğal' OR 'makine' sonuç vektörü: {res_or} -> Eşleşen Dokümanlar: {matching_docs_or}")

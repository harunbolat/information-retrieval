import numpy as np

# 1. Corpus (Derlem) Tanımı
documents = [
    "bilgi erişim ve arama motoru",
    "arama motoru verimli çalışır",
]

# 2. Stopwords (Durdurma kelimeleri) hariç Vocabulary (Sözlük) Oluşturma
stopwords = {"ve"}
vocabulary = sorted(
    list(
        set(
            word
            for doc in documents
            for word in doc.lower().split()
            if word not in stopwords
        )
    )
)


# 3. Bag-of-Words (BoW) / Vektörleştirme Fonksiyonu
def text_to_vector(text, vocab):
  words = text.lower().split()
  # Her kelimenin sözlükteki frekansını (TF) hesapla
  return np.array([words.count(term) for term in vocab])


# Dokümanları vektör uzayına dönüştürme
doc_vectors = [text_to_vector(doc, vocabulary) for doc in documents]

# 4. Sorgu (Query) Tanımlama ve Vektörleştirme
query = "arama bilgi"
query_vector = text_to_vector(query, vocabulary)


# 5. Kosinüs Benzerliği (Cosine Similarity) Hesabı
# Cosine Similarity = (A . B) / (||A|| * ||B||)
def cosine_similarity(v1, v2):
  dot_product = np.dot(v1, v2)
  norm_v1 = np.linalg.norm(v1)
  norm_v2 = np.linalg.norm(v2)
  if norm_v1 == 0 or norm_v2 == 0:
    return 0.0
  return dot_product / (norm_v1 * norm_v2)


# --- ÇIKTILARI GÖRÜNTÜLEME ---
print(f"Sözlük (Vocabulary, |V|={len(vocabulary)}):", vocabulary)
print("-" * 50)

for i, vec in enumerate(doc_vectors):
  print(f"Doküman d{i+1} vektörü : {vec}")

print(f"Sorgu ('{query}') vektörü  : {query_vector}")
print("-" * 50)

# Sıralama (Ranking)
similarities = []
for i, vec in enumerate(doc_vectors):
  sim = cosine_similarity(query_vector, vec)
  similarities.append((f"d{i+1}", sim))
  print(f"Sorgu ile d{i+1} Kosinüs Benzerliği: {sim:.4f}")

# Benzerliğe göre azalan şekilde sırala
ranked_docs = sorted(similarities, key=lambda x: x, reverse=True)
print("\nSıralanmış Sonuçlar (Ranking):", ranked_docs)

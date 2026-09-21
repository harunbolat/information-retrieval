# 1. Örnek Doküman Koleksiyonu
documents = {
    1: "bilgi erişimi ve arama motorları",
    2: "doğal dil işleme ve bilgi erişimi",
    3: "makine öğrenmesi ve yapay zeka",
    4: "arama motorları ve web teknolojileri"
}

# 2. Metinleri temizleme ve Ters Dizin (Inverted Index) oluşturma
def build_inverted_index(docs):
    inverted_index = {}
    for doc_id, text in docs.items():
        # Kelimeleri küçük harfe çevir ve boşluklara göre ayır
        terms = text.lower().split()
        for term in terms:
            if term not in inverted_index:
                inverted_index[term] = set()
            inverted_index[term].add(doc_id)
    return inverted_index

index = build_inverted_index(documents)

# 3. Boolean Arama Fonksiyonları
def search_and(term1, term2):
    """VE (AND) Operatörü: Her iki kelimenin de geçtiği belgeleri bulur."""
    set1 = index.get(term1, set())
    set2 = index.get(term2, set())
    return set1.intersection(set2)

def search_or(term1, term2):
    """VEYA (OR) Operatörü: Kelimelerden en az birinin geçtiği belgeleri bulur."""
    set1 = index.get(term1, set())
    set2 = index.get(term2, set())
    return set1.union(set2)

def search_not(term1, term2, all_docs_count):
    """DEĞİL (NOT) Operatörü: term1'in geçip term2'nin geçmediği belgeleri bulur."""
    set1 = index.get(term1, set())
    set2 = index.get(term2, set())
    return set1.difference(set2)

# --- TEST KÖŞESİ ---

print("Ters Dizin (Inverted Index) Yapısı:")
for term, doc_ids in index.items():
    print(f"'{term}': {doc_ids}")

print("\n--- Arama Örnekleri ---")

# Örnek 1: "bilgi" VE "erişimi" geçen dokümanlar
result_and = search_and("bilgi", "erişimi")
print(f"'bilgi' AND 'erişimi' sonuçları (Doküman ID): {result_and}")

# Örnek 2: "yapay" VEYA "web" geçen dokümanlar
result_or = search_or("yapay", "web")
print(f"'yapay' OR 'web' sonuçları (Doküman ID): {result_or}")
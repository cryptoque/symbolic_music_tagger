import json
from emotional_map import EMOTION_TO_SYMBOLIC

def expand_query_terms(terms):
    expanded = set()
    for term in terms:
        term = term.lower()
        if term in EMOTION_TO_SYMBOLIC:
            expanded.update(EMOTION_TO_SYMBOLIC[term])
        expanded.add(term)
    print(expanded)
    return list(expanded)

def match_query(piece, query_main, query_feelings_terms):
    query_feelings_terms = expand_query_terms(query_feelings_terms)
    text_fields = [
        piece.get("title", ""),
        piece.get("composer", ""),
        piece.get("performer", ""),
        " ".join(piece.get("tags", []))
    ]
    searchable_text = " ".join(text_fields).lower()
    print(searchable_text)
    #for term in searchable_text:
    #    print("tagged: ", term)
    for term in query_feelings_terms:
        print("search: ", term)
    print(term in searchable_text for term in query_feelings_terms)
    return all(term in searchable_text for term in query_feelings_terms)

def main():
    with open("tagged.json", "r", encoding="utf-8") as f:
        pieces = json.load(f)

    query_main = input("[INFO] Search for composer, performer or title: ").strip()
    query_feelings = input("[INFO] Filter for feelings: ").strip()
    if not query_main:
        print("[INFO] Empty query.")
        return

    query_feelings_terms = query_feelings.split()
    results = [p for p in pieces if match_query(p, query_main, query_feelings_terms)]

    print(f"[INFO] Found {len(results)} result(s):")
    for piece in results:
        print(f"[DATA] {piece.get('title')} — {piece.get('composer')}")
        print(f"[DATA] Performer: {piece.get('performer')}")
        print(f"[DATA] Tags: {', '.join(piece.get('tags', []))}")

if __name__ == "__main__":
    main()

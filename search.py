import json
from emotional_map import EMOTION_TO_SYMBOLIC

def expand_query_terms(terms):
    """Expand feeling words to their symbolic tag equivalents."""
    expanded = set()
    for term in terms:
        term = term.lower()
        if term in EMOTION_TO_SYMBOLIC:
            expanded.update(tag.lower() for tag in EMOTION_TO_SYMBOLIC[term])
        expanded.add(term.lower())
    return list(expanded)

def match_query(piece, query_main, query_feelings_terms):
    """Match piece against main query and feelings."""
    matched = True
    
    # Match main query if provided
    if query_main:
        main_query_lower = query_main.lower()
        metadata_fields = [
            piece.get("title", "").lower(),
            piece.get("composer", "").lower(),
            piece.get("performer", "").lower()
        ]
        if not any(main_query_lower in field for field in metadata_fields):
            matched = False
    
    # Match feelings if provided
    if query_feelings_terms:
        piece_tags = [tag.lower() for tag in piece.get("tags", [])]
        expanded_feelings = expand_query_terms(query_feelings_terms)
        for feeling in expanded_feelings:
            print("Search: ", feeling)
        for feeling in piece_tags:
            print("Tags: ", feeling)
        if not any(feeling in piece_tags for feeling in expanded_feelings):
            matched = False

    return matched

def main():
    with open("tagged.json", "r", encoding="utf-8") as f:
        pieces = json.load(f)

    query_main = input("[INFO] Search for composer, performer or title: ").strip()
    query_feelings = input("[INFO] Filter for feelings: ").strip()
    query_feelings_terms = query_feelings.split() if query_feelings else []
    
    if not query_main and not query_feelings_terms:
        print("[INFO] No query entered. Please enter at least one search parameter.")
        return

    results = [p for p in pieces if match_query(p, query_main, query_feelings_terms)]

    print(f"[INFO] Found {len(results)} result(s):")
    print(f"[DATA] *****************************************")
    for piece in results:
        print(f"[DATA] Title: {piece.get('title')}")
        print(f"[DATA] Composer: {piece.get('composer')}")
        print(f"[DATA] Performer: {piece.get('performer')}")
        print(f"[DATA] Tags: {', '.join(piece.get('tags', []))}")
        print(f"[DATA] *****************************************")

if __name__ == "__main__":
    main()

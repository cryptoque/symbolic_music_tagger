import asyncio
from loader import load_all_files
from symbolic_tags import get_tags
import json

async def main():
    pieces = await load_all_files()
    print(f"[INFO] Loaded {len(pieces)} valid files.")

    print("[INFO] Tagging pieces...")
    for piece in pieces:
        piece["tags"] = get_tags(piece)
        print(f"[DATA] {piece['title']} → {piece['tags']}")
    
    print("[INFO] Sample tagged output:")
    for piece in pieces[:5]:
        print(f"[DATA] {piece.get('title', 'Untitled')} — {piece.get('composer', 'Unknown')}")
        print(f"[DATA] Performer: {piece.get('performer', 'Unknown')}")
        print(f"[DATA] Tags: {', '.join(piece.get('tags', []))}")
    
    with open("tagged.json", "w", encoding="utf-8") as f:
        json.dump(pieces, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(main())
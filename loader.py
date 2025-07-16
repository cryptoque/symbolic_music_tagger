import json
import asyncio
from pathlib import Path


REQUIRED_FIELDS = {"title", "composer", "performer", "form", "duration_min", "key", "structure"}

def read_json_async(path) -> dict:
    """Reads and parses a JSON file synchronously."""
    with path.open("r", encoding='utf-8') as f:
        print("[INFO] opening: ", path)
        return json.load(f)

def validate_piece(data: dict, path: Path) -> bool:
    """Validate the structure of a music metadata JSON object."""
    missing = REQUIRED_FIELDS - data.keys()
    if missing:
        print(f"[ERROR] {path.name}: Missing fields: {sorted(missing)}")
        return False
    return True

async def load_file(path: Path) -> dict | None:
    """Load and validate a single JSON metadata file asynchronously."""
    try:
        data = await asyncio.to_thread(read_json_async, path)
        if validate_piece(data, path):
            print(f"[INFO] Loaded: ", {path.name})
            return data
    except json.JSONDecodeError as e:
        print(f"[ERROR] {path.name}: JSON parse error → {e}")
        return None
    except Exception as e:
        print(f"[ERROR] {path.name}: Unexpected error → {e}")
        return None
async def load_all_files(data_dir= "data") -> list[dict]:
    """Load and validate all .json files under a given directory."""
    paths = list(Path(data_dir).glob("*.json"))
    if not paths:
        print("[ERROR] No JSON files found in 'data/'")
        return []
    tasks = [load_file(p) for p in paths]
    results = await asyncio.gather(*tasks)

    return [r for r in results if r is not None]
    
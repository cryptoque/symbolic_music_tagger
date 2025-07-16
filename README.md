# Symbolic Classical Music Tagger

**What if we could search classical music not by genre, but by feelings it evoked based on its keys, structure, and interpretive style?**

It’s a tool for enriching classical piano metadata with **symbolic tags** e.g. “Tender & Personal”, “Tragic Grandeur”, “Structured Complexity”, to make emotional and intellectual browsing possible. 

This tool also helps translate the feelings you are looking for to symbolic tags, e.g.

```
    "romantic": [
        "Joyful & Open",
        "Tender & Personal",
        "Spontaneous Nostalgia"
    ],
```

---

## How to Use

### Add your classical pieces, or use the existing library inside data folder
- Place `.json` files describing pieces in the `data/` folder. For example:

```json
  {
    "title": "Piano Sonata No. 32 in C minor, Op. 111",
    "composer": "Beethoven",
    "performer": "Sviatoslav Richter",
    "form": "sonata",
    "duration_min": 27,
    "key": "C minor",
    "structure": ["Maestoso", "Arietta"]
  }
```

### Tag all pieces

Run the following to tag all pieces inside data folder:

```python
python3 main.py
```

### Search with emotional filter

Start an interactive search:

```python
python3 search.py
```
You will be prompted for the following:

> Enter a composer/title/performer (optional).

> Select from a list of feelings (optional).

Example query:

```
[INFO] Search for composer, performer or title (optional): schubert
[INFO] Filter for feelings (comma-separated, optional): sad, reverent
```
---

## Why This Exists

Classical metadata is poor at expressing why we listen. Even specialized classical music streaming platforms like Apple music classical only offer keys, durations, composer, performer...But they don’t let us find “Schubert, sad but tender” or “Beethoven, existential with volcanic drive.”

This tool builds a symbolic layer bridging music’s emotional, structural, and interpretive dimensions.


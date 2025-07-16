# Symbolic Classical Music Tagger

**What if we could search classical music not by genre or composer, but by the feelings it evokes - drawn from its keys, forms, structure, and interpretive style?**

Most classical metadata today fails to capture why we listen. Even platforms like Apple Music Classical stop at keys, durations, composer, performer…

But they don’t let us find “Schubert, sad but tender” or “Beethoven, existential with volcanic drive.”

This tool builds a symbolic layer over traditional metadata—bridging emotional, structural, and interpretive dimensions.

## What it does
It enriches classical music metadata with symbolic tags like:

- Tender & Personal
- Tragic Grandeur
- Structured Complexity

This makes emotional and intellectual browsing possible in a way no existing platform offers.

## Example: Translating Feelings Into Symbols

When you search for “melancholy”, it maps to:

```
    "melancholy": [
        "Clear & Somber",
        "Calm & Slow",
        "Tragic Grandeur"
    ],
```
So you’ll surface pieces across composers and eras that share this emotional landscape.

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
[INFO] Search for composer, performer or title (optional): richter
[INFO] Filter for feelings (comma-separated, optional): slow, introspective
```

Example result in CLI:

<img width="618" height="446" alt="Screenshot 2025-07-16 at 4 11 57 PM" src="https://github.com/user-attachments/assets/d201c995-7c56-436e-af7d-1288bdc430a8" />


*requires python 3.8+, no external dependencies*

--- 

## Note

This is a hobby project and not intended for production use.

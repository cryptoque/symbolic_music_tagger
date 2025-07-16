FORM_TAGS = {
    "sonata": "Long Emotional Journey",
    "intermezzo": "Tender & Personal",
    "fugue": "Structured Complexity",
    "prelude": "Focused Miniature",
    "etude": "Technical Emotion",
    "nocturne": "Intimate & Dreamlike",
    "impromptu": "Spontaneous Nostalgia",
    "fantasy": "Freely Shifting Emotion",
    "ballade": "Storytelling Intensity",
    "toccata": "Relentless Motion",
    "rondo": "Repeating Spirals",
    "scherzo": "Dark Playfulness",
    "variation": "Transformative Flow",
    "waltz": "Light & Elegant",
    "polonaise": "Majestic Rhythm",
    "mazurka": "Earthy Grace",
    "bagatelle": "Playful Fragment",
    "capriccio": "Impulsive Whimsy",
}

KEY_TAGS = {
    # Major Keys
    "c major": "Pure & Noble",
    "c sharp major": "Radiant Construct",
    "d major": "Triumphant & Bright",
    "e major": "Radiant Warmth",
    "e flat major": "Inner Majesty",
    "f major": "Pastoral Calm",
    "f sharp major": "Dazzling Structure",
    "g major": "Peaceful Confidence",
    "a major": "Joyful & Open",
    "a flat major": "Lyrical Stained Glass",
    "b major": "Luminous & Unstable",
    "b flat major": "Earthy Nobility",

    # Minor Keys
    "a minor": "Melancholy Simplicity",
    "b minor": "Dark & Devotional",
    "b flat minor": "Twilight Density",
    "c minor": "Clear & Somber",
    "c sharp minor": "Hidden Tension",
    "d minor": "Tragic Grandeur",
    "e minor": "Restless Sadness",
    "e flat minor": "Funeral Labyrinth",
    "f minor": "Fatalistic Depth",
    "f sharp minor": "Mournful Precision",
    "g minor": "Solemn Intensity",
    "g sharp minor": "Ghosted Motion",
}

TEMPO_TAGS = {
    "largo": "Spacious Stillness",
    "lento": "Calm & Slow",
    "adagio": "Reflective Tempo",
    "andante": "Flowing Motion",
    "moderato": "Steady Walk",
    "allegro": "Energetic Pulse",
    "vivace": "Lively Drive",
    "presto": "Frenzied Momentum",
    "scherzo": "Rhythmic Instability",
    "fugue": "Structured Complexity",
}

PERFORMER_TAGS = {
    "richter": [
        "Structural Depth",
        "Emotional Conviction",
        "Stylistic Chameleon",
        "Spiritual Restraint"
    ],
    "brendel": [
        "Intellectual Clarity",
        "Austere Restraint",
        "Philosophical Nuance",
        "Understated Irony"
    ],
    "lupu": [
        "Reverent Softness",
        "Inward Intensity",
        "Transparent Warmth",
        "Dreamlike Simplicity"
    ],
    "gilels": [
        "Golden Tone",
        "Balanced Nobility",
        "Romantic Authority",
        "Refined Strength"
    ],
    "gould": [
        "Detached Intelligence",
        "Mechanical Purity",
        "Analytical Boldness",
        "Idiosyncratic Pulse"
    ],
    "argenrich": [
        "Explosive Virtuosity",
        "Impulsive Passion",
        "Volcanic Drive",
        "Elemental Energy"
    ],
    "pollini": [
        "Cool Precision",
        "Architectural Brilliance",
        "Motoric Control",
        "Steel Under Elegance"
    ],
    "barenboim": [
        "Philosophical Weight",
        "Broad Gesture",
        "Deliberate Intellect",
        "Romantic Grandeur"
    ],
    "zimmerman": [
        "Controlled Emotion",
        "Crystal Technique",
        "Spiritual Modernity",
        "Coloristic Insight"
    ],
    "pogorelich": [
        "Theatrical Distortion",
        "Extreme Rubato",
        "Disrupted Elegance",
        "Psychological Drama"
    ],
    "kissin": [
        "Heroic Force",
        "Clean Brilliance",
        "Youthful Momentum",
        "Technical Radiance"
    ],
    "trifonov": [
        "Whirlwind Artistry",
        "Transparent Frenzy",
        "Textural Fantasy",
        "Narrative Fluctuation"
    ]
}



def get_tags(piece: dict) -> list[str]:
    """
    Generate symbolic tags for a classical music piece based on its metadata.
    """
    tags = []

    form = piece.get("form", "").lower()
    composer = piece.get("composer", "").lower()
    performer = piece.get("performer", "").lower()
    structure = piece.get("structure", [])
    duration = piece.get("duration", 0)
    key = piece.get("key", "").lower()

    # --- FORM-based rules ---
    if form in FORM_TAGS:
        tags.append(FORM_TAGS[form])

    # --- KEY-based rules ---
    if key in KEY_TAGS:
        tags.append(KEY_TAGS[key])

    # --- Dueation-based rules ---
    if duration < 3:
        tags.append("Miniature Form")
    elif duration <= 8:
        tags.append("Compact Expression")
    elif duration <= 18:
        tags.append("Full Narrative")
    else:
        tags.append("Long Emotional Journey")

    # --- Structure-based rules ---
    structure = [s.lower() for s in piece.get("structure", [])]
    for item in structure:
        for tempo, tag in TEMPO_TAGS.items():
            if tempo in item.lower():
                tags.append(tag)
    
    # --- Performer-based rules ---
    for name, tags_list in PERFORMER_TAGS.items():
        if name in performer:
            tags.append(tag)
    
    return list(set(tags))

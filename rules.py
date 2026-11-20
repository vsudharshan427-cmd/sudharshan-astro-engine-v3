LAGNAMS = ["Mesham", "Rishabam", "Medhunam", "Kadagam", "Simham", "Kanni",
           "Thulam", "Viruchagam", "Dhanusu", "Magaram", "Kumbam", "Meenam"]
SIGNS = LAGNAMS[:]
PLANETS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]

# User-supplied sign-specific risk rules: (planet, houses)
SIGN_RISK = {
    "Mesham": ("Mars", [2, 7, 3, 6, 11]),
    "Rishabam": ("Venus", [3, 4, 7, 8, 12]),
    "Medhunam": ("Mercury", [2, 6, 7, 10, 11]),
    "Kadagam": ("Moon", [2, 3, 7, 8]),
    "Simham": ("Sun", [3, 8, 12]),
    "Kanni": ("Mercury", [3, 4, 7, 8, 11]),
    "Thulam": ("Venus", [2, 3, 7, 10, 11]),
    "Viruchagam": ("Mars", [3, 7, 8, 11, 12]),
    "Dhanusu": ("Jupiter", [2, 6, 7, 8, 10, 11]),
    "Magaram": ("Saturn", [1, 2, 3, 4, 7, 11]),
    "Kumbam": ("Jupiter", [1, 2, 3, 6, 8, 10, 12]),
    "Meenam": ("Jupiter", [3, 4, 6, 7, 8, 11]),
}

MAARAGAM_HOUSES = {
    "Mesham": [2, 7], "Rishabam": [3, 8], "Medhunam": [7, 11],
    "Kadagam": [2, 7], "Simham": [3, 8], "Kanni": [7, 11],
    "Thulam": [2, 7], "Viruchagam": [3, 8], "Dhanusu": [7, 11],
    "Magaram": [2, 7], "Kumbam": [3, 8], "Meenam": [7, 11],
}

# User-confirmed two-Maaragam lord pairs. Some Lagnams have an additional
# Jupiter-Mercury pair, as explicitly specified by the user.
TWO_MARAGAM_PAIRS = {
    "Mesham": [("Mars", "Venus")],
    "Rishabam": [("Moon", "Jupiter")],
    "Medhunam": [("Jupiter", "Mars"), ("Jupiter", "Mercury")],
    "Kadagam": [("Sun", "Saturn")],
    "Simham": [("Jupiter", "Venus")],
    "Kanni": [("Jupiter", "Moon"), ("Jupiter", "Mercury")],
    "Thulam": [("Mars", "Venus")],
    "Viruchagam": [("Mercury", "Saturn")],
    "Dhanusu": [("Mercury", "Venus"), ("Jupiter", "Mercury")],
    "Magaram": [("Saturn", "Moon")],
    "Kumbam": [("Mars", "Mercury")],
    "Meenam": [("Mercury", "Saturn"), ("Jupiter", "Mercury")],
}
BAATHAGAM_HOUSE = {
    "Mesham": 11, "Rishabam": 9, "Medhunam": 7, "Kadagam": 11,
    "Simham": 9, "Kanni": 7, "Thulam": 11, "Viruchagam": 9,
    "Dhanusu": 7, "Magaram": 11, "Kumbam": 9, "Meenam": 7,
}
BAATHAGAM_RISK = {
    "Mesham": ("Mars", [2, 7, 11]),
    "Rishabam": ("Venus", [3, 8, 9]),
    "Medhunam": ("Mercury", [7, 11]),
    "Kadagam": ("Moon", [2, 7, 11]),
    "Simham": ("Sun", [3, 8, 9]),
    "Kanni": ("Mercury", [7, 11]),
    "Thulam": ("Venus", [2, 7, 11]),
    "Viruchagam": ("Mars", [3, 8, 9]),
    "Dhanusu": ("Jupiter", [7, 11]),
    "Magaram": ("Saturn", [2, 7, 11]),
    "Kumbam": ("Saturn", [3, 8, 9]),
    "Meenam": ("Jupiter", [7, 11]),
}

ASPECTS = {
    "Mars": [4, 7, 8], "Venus": [7], "Sun": [7], "Mercury": [7],
    "Moon": [7], "Jupiter": [5, 7, 9], "Saturn": [3, 7, 10],
}
# Only this mutual aspect was explicitly identified as a GOOD aspect.
GOOD_MUTUAL_ASPECTS = {tuple(sorted(("Moon", "Jupiter")))}

DHESAI_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
                "Jupiter", "Saturn", "Mercury"]

# Aatchi signs
AATCHI = {
    "Sun": ["Simham"], "Moon": ["Kadagam"],
    "Mars": ["Mesham", "Viruchagam"],
    "Mercury": ["Medhunam", "Kanni"],
    "Jupiter": ["Dhanusu", "Meenam"],
    "Venus": ["Rishabam", "Thulam"],
    "Saturn": ["Kumbam", "Magaram"],
}
# Each pair is (Ucham sign, Neecham sign), in the order supplied by the user.
UCHAM_NEECHAM = {
    "Sun": ("Mesham", "Thulam"),
    "Moon": ("Rishabam", "Viruchagam"),
    "Venus": ("Meenam", "Kanni"),
    "Mercury": ("Kanni", "Meenam"),
    "Jupiter": ("Kadagam", "Magaram"),
    "Mars": ("Magaram", "Kadagam"),
    "Rahu": ("Viruchagam", "Rishabam"),
    "Ketu": ("Viruchagam", "Rishabam"),
}

# Planet-pair opponent rules; Mars-Jupiter conjunction is explicitly good,
# so it is not treated as an opponent conjunction.
OPPONENTS = {
    "Mars": {"Venus", "Rahu", "Ketu", "Mercury", "Saturn"},
    "Jupiter": {"Mercury", "Rahu", "Venus"},
    "Sun": {"Rahu"},
    "Moon": {"Mercury", "Rahu", "Ketu", "Saturn"},
    "Venus": {"Mars", "Rahu", "Ketu", "Jupiter"},
    "Mercury": {"Ketu", "Jupiter", "Mars", "Moon"},
    "Saturn": {"Mars", "Moon"},
}
OPPONENT_PAIRS = {tuple(sorted((p, q))) for p, qs in OPPONENTS.items() for q in qs}
OPPONENT_PAIRS.discard(tuple(sorted(("Mars", "Jupiter"))))

# Good conjunctions supplied by the user (kept as a separate result from strength).
GOOD_JOINS = {
    "Sun": {"Mercury", "Venus", "Saturn", "Moon", "Jupiter", "Mars"},
    "Moon": {"Jupiter", "Mars", "Venus", "Sun"},
    "Mercury": {"Venus", "Saturn", "Rahu", "Sun"},
    "Venus": {"Mercury", "Moon", "Sun"},
    "Mars": {"Jupiter", "Sun", "Moon"},
    "Jupiter": {"Moon", "Mars", "Ketu", "Sun"},
    "Saturn": {"Venus", "Mercury", "Rahu", "Sun"},
}
GOOD_PAIRS = {tuple(sorted((p, q))) for p, qs in GOOD_JOINS.items() for q in qs}

def house_sign_map(lagnam):
    start = SIGNS.index(lagnam)
    return {h: SIGNS[(start + h - 1) % 12] for h in range(1, 13)}

def sign_house_map(lagnam):
    return {sign: house for house, sign in house_sign_map(lagnam).items()}

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def aspects_house(planet, from_house, target_house):
    return any(((from_house + offset - 2) % 12) + 1 == target_house
               for offset in ASPECTS.get(planet, []))

def analyze_chart(lagnam, raw_positions, active_dhesai):
    if lagnam not in LAGNAMS:
        raise ValueError("Select a valid Lagnam.")
    if active_dhesai not in DHESAI_ORDER:
        raise ValueError("Select a valid Dhesai planet.")

    positions = {}
    for p in PLANETS:
        value = raw_positions.get(p, "")
        if value in ("", None):
            continue
        try:
            h = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"Enter a valid house number for {p}.")
        if not 1 <= h <= 12:
            raise ValueError(f"{p}: house must be between 1 and 12.")
        positions[p] = h
    if not positions:
        raise ValueError("Enter at least one planetary position.")

    current_map = house_sign_map(lagnam)
    planet_signs = {p: current_map[h] for p, h in positions.items()}
    house_planets = {h: [] for h in range(1, 13)}
    for p, h in positions.items():
        house_planets[h].append(p)

    strengths = []
    for p, sign in planet_signs.items():
        tags = []
        if sign in AATCHI.get(p, []):
            tags.append("Aatchi")
        pair = UCHAM_NEECHAM.get(p)
        if pair:
            if sign == pair[0]:
                tags.append("Ucham")
            elif sign == pair[1]:
                tags.append("Neecham")
        if p == "Mercury" and sign == "Kanni":
            tags.append("Special note: very strong Mercury in Kanni")
        if tags:
            strengths.append({"planet": p, "sign": sign, "tags": tags})

    good_joins, opponent_risks, good_aspects = [], [], []
    present = list(positions.items())
    for i, (p1, h1) in enumerate(present):
        for p2, h2 in present[i+1:]:
            pair = tuple(sorted((p1, p2)))
            if h1 == h2:
                if pair in GOOD_PAIRS:
                    good_joins.append(f"{p1} + {p2} join in House {h1} ({current_map[h1]}).")
                if pair in OPPONENT_PAIRS:
                    opponent_risks.append(f"{p1} + {p2} join in House {h1} ({current_map[h1]}).")
            if aspects_house(p1, h1, h2) and aspects_house(p2, h2, h1):
                if pair in GOOD_MUTUAL_ASPECTS:
                    good_aspects.append(f"{p1} and {p2} mutually aspect each other.")
                if pair in OPPONENT_PAIRS:
                    opponent_risks.append(f"{p1} and {p2} mutually aspect each other.")

    alerts = []
    sign_risk_planet, sign_risk_houses = SIGN_RISK[lagnam]
    for h in sign_risk_houses:
        if positions.get(sign_risk_planet) == h:
            alerts.append(f"{sign_risk_planet} in House {h} ({current_map[h]}) matches the {lagnam} sign-specific risk rule.")
    bplanet, bhouses = BAATHAGAM_RISK[lagnam]
    for h in bhouses:
        if positions.get(bplanet) == h:
            alerts.append(f"{bplanet} in House {h} ({current_map[h]}) matches the {lagnam} Baathagam risk rule.")
    for msg in opponent_risks:
        alerts.append("Opponent rule: " + msg)

    # Global Two Maragams Issue: check all 12 Lagnams, regardless of the
    # horoscope's selected Lagnam. Each pair is checked for conjunction or
    # mutual aspect. Display house Rasi names as well as house numbers.
    two_maragam_issues = []
    for asc in LAGNAMS:
        asc_map = house_sign_map(asc)
        asc_house_map = sign_house_map(asc)
        for p1, p2 in TWO_MARAGAM_PAIRS[asc]:
            if p1 not in positions or p2 not in positions:
                continue
            h1, h2 = positions[p1], positions[p2]
            joined = h1 == h2
            mutual = aspects_house(p1, h1, h2) and aspects_house(p2, h2, h1)
            if joined or mutual:
                relation = "joined" if joined else "mutually aspect each other"
                house1, house2 = MAARAGAM_HOUSES[asc]
                two_maragam_issues.append({
                    "lagnam": asc,
                    "planet1": p1,
                    "planet2": p2,
                    "relation": relation,
                    "house1_number": house1,
                    "house1_label": ordinal(house1),
                    "house1_sign": asc_map[house1],
                    "house2_number": house2,
                    "house2_label": ordinal(house2),
                    "house2_sign": asc_map[house2],
                    "detail": (
                        f"{asc} Lagnam: {ordinal(house1)} house ({asc_map[house1]}) "
                        f"and {ordinal(house2)} house ({asc_map[house2]}) are the two "
                        f"Maaragam houses. Their lords {p1} and {p2} {relation}."
                    )
                })

    # Period/Dhesai: current + next two planets, checked against all 12 Lagnams.
    start = DHESAI_ORDER.index(active_dhesai)
    period_planets = [DHESAI_ORDER[(start + i) % len(DHESAI_ORDER)] for i in range(3)]
    period_results = []
    for period_planet in period_planets:
        if period_planet not in planet_signs:
            period_results.append({
                "planet": period_planet, "sign": None, "matches": [],
                "missing": True
            })
            continue
        sign = planet_signs[period_planet]
        matches = []
        for asc in LAGNAMS:
            h = sign_house_map(asc)[sign]
            reasons = []
            if h in MAARAGAM_HOUSES[asc]:
                reasons.append("Maaragam")
            if h == BAATHAGAM_HOUSE[asc]:
                reasons.append("Baathagam")
            # Also apply the user's planet-specific Baathagam position rules.
            b_p, b_hs = BAATHAGAM_RISK[asc]
            if period_planet == b_p and h in b_hs and "Baathagam" not in reasons:
                reasons.append("Baathagam planet-position rule")
            if reasons:
                matches.append({"lagnam": asc, "house": h, "reasons": reasons})
        period_results.append({
            "planet": period_planet, "sign": sign, "matches": matches,
            "missing": False
        })

    return {
        "lagnam": lagnam, "positions": positions, "planet_signs": planet_signs,
        "sign_map": current_map, "house_planets": house_planets,
        "strengths": strengths, "good_joins": good_joins,
        "good_aspects": good_aspects, "alerts": alerts,
        "two_maragam_issues": two_maragam_issues,
        "period_planets": period_planets, "period_results": period_results,
        "notes": [
            "Dhesai checks the selected planet and the next two planets in the cyclic sequence.",
            "Dhesai checks the entered planetary sign positions across all 12 Lagnams.",
            "Good aspects, strengths, and risk alerts are separate results; one does not cancel another.",
            "Rahu/Ketu aspects are not calculated because no aspect offsets were supplied.",
            "Two Maragams Issue checks all 12 Lagnams using the user-confirmed planet pairs.",
            "Two Maragams results are separate from good combinations and other risk checks.",
            "Ratings are intentionally reserved for Project 4.",
            "This app checks the custom rules entered by the user; it does not establish factual predictions."
        ]
    }

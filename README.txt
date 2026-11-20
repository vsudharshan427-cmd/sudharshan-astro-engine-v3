SUDHARSHAN'S ASTRO ENGINE — PROJECT 3

Project 3 carries forward Project 2 and adds a dedicated Two Maragams Issue section.

Two Maragams pairs supplied by the user:
- Mesham: Mars + Venus
- Rishabam: Moon + Jupiter
- Medhunam: Jupiter + Mars; additional Jupiter + Mercury
- Kadagam: Sun + Saturn
- Simham: Jupiter + Venus
- Kanni: Jupiter + Moon; additional Jupiter + Mercury
- Thulam: Mars + Venus
- Viruchagam: Mercury + Saturn
- Dhanusu: Mercury + Venus; additional Jupiter + Mercury
- Magaram: Saturn + Moon
- Kumbam: Mars + Mercury
- Meenam: Mercury + Saturn; additional Jupiter + Mercury

How Two Maragams Issue works:
- Checks all 12 Lagnams, not only the selected chart Lagnam.
- For each configured pair, checks whether the two planets are in the same house (joined) or mutually aspect each other, using the aspect rules already supplied.
- When a match occurs, reports the affected Lagnam, its two Maaragam house numbers, the Rasi names occupying those houses, the two planet lords, and whether they are joined or mutually aspecting.
- If no pair matches, displays: There is no two Maragams in this horoscope.
- The extra Jupiter + Mercury pair is included for Medhunam, Kanni, Dhanusu and Meenam as instructed.

Project 2 features retained:
- House-to-sign mapping from selected Lagnam.
- Aatchi, Ucham and Neecham strength tags.
- Good joins and the specified Moon-Jupiter good mutual aspect.
- Sign-specific, Baathagam and opponent risk checks.
- Dhesai: selected planet plus the next two planets in the cyclic sequence.
- Dhesai checks entered planet signs across all 12 Lagnams.

Project 4 will add the rating section. No rating is included here.

Important notes:
- Enter planetary positions as house numbers counted from the selected horoscope Lagnam.
- A pair can appear as a good combination and also trigger a Two Maragams Issue; the sections are kept separate.
- Rahu/Ketu aspects are not calculated because no aspect offsets were supplied.
- This is a custom rule-checking tool, not a factual prediction system.

Run:
1. Open Command Prompt in this folder.
2. Activate the environment if present: .venv\Scripts\activate
3. Install Flask if needed: python -m pip install flask
4. Run: python app.py
5. Open http://127.0.0.1:5000

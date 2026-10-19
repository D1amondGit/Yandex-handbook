text = 'Мама мыла раму!'
print({s: c for s, c in sorted(set((s.lower(), text.lower().count(s.lower())) for s in text if s.isalpha()))})

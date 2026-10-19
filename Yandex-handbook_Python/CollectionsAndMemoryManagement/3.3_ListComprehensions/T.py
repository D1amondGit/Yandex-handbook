text = 'ехали медведи на велосипеде'
print({(w, v) for w in text.split() for v in text.split() if len(set(w) & set(v)) > 2 and w < v})
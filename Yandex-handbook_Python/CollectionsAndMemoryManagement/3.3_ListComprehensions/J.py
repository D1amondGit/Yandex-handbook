words = 'My homework is too difficult!'
print([word for word in words.split() if sum(1 for char in word.lower() if char in "аяуюоёэеиыaeiouy") >= 3])
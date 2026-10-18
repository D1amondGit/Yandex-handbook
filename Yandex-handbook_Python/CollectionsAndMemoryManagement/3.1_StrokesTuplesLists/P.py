L = int(input())
N = int(input())

lines = [input() for _ in range(N)]

total_text_len = sum(len(line) for line in lines)

if total_text_len <= L:
    print("\n".join(lines))
else:
    full_text = "\n".join(lines)

    result = ""
    chars_taken = 0

    for char in full_text:
        if char != '\n':
            if chars_taken < L - 3:
                result += char
                chars_taken += 1
            else:
                break
        else:
            if chars_taken < L - 3:
                result += char

    print(result + "...")
def calculate_max_experience(pyramid):
    if not pyramid:
        return 0

    dp = [row[:] for row in pyramid]

    for i in range (len(dp) - 2, -1, -1):
        for j in range (len(dp[i])):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]

def main():
    try:
        with open("career.in", "r", encoding="utf=8") as f:
            lines = f.read().strip().split("\n")

            if not lines or not lines[0]:
                return

            l = int(lines[0].strip())
            pyramid = []

            for i in range (1, l + 1):
                row = list(map(int, lines[i].strip().split()))
                pyramid.append(row)

            result = calculate_max_experience(pyramid)

            with open ("career.out", "w", encoding="utf=8") as f:
                f.write(str(result) + "\n")

            print(f"Максимальний досвід: {result}")

    except FileNotFoundError:
        print("Помилка: Файл career.in не найдено")

if __name__ == "__main__":
    main()
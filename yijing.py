import json
import random
import os

class Line:
    def __init__(self, line_number, is_yang, is_changing):
        self.line_number = line_number
        self.is_yang = is_yang
        self.is_changing = is_changing

class HexagramInfoFull:
    def __init__(self, data):
        self.number = data["Number"]
        self.name = data["Name"]
        self.chinese_name = data["ChineseName"]
        self.upper_trigram = data["UpperTrigram"]
        self.lower_trigram = data["LowerTrigram"]
        self.judgment_cn = data["JudgmentCN"]
        self.judgment_en = data["JudgmentEN"]
        self.image_cn = data["ImageCN"]
        self.image_en = data["ImageEN"]
        self.sample_use = data["SampleUse"]

class YiJing:
    def __init__(self, json_path):
        self.rng = random.Random()
        self.data = self.load(json_path)
        self.king_wen_lookup = [
            [1, 43, 14, 34, 9, 5, 26, 11],
            [10, 58, 38, 54, 61, 60, 41, 19],
            [13, 49, 30, 55, 37, 63, 22, 36],
            [25, 17, 21, 51, 42, 3, 27, 24],
            [44, 28, 50, 32, 57, 48, 18, 46],
            [6, 47, 64, 40, 59, 29, 4, 7],
            [33, 31, 56, 62, 53, 39, 52, 15],
            [12, 45, 35, 16, 20, 8, 23, 2]
        ]

    def cast_hexagram(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Focus on your question. Press Enter to cast...")

        lines = []
        changing_positions = []

        for i in range(6):
            sum_ = self.throw_coins()
            is_yang = sum_ in [7, 9]
            is_changing = sum_ in [6, 9]
            lines.append(Line(i + 1, is_yang, is_changing))
            symbol = self.get_line_symbol(is_yang, is_changing)
            print(f"Line {i + 1}: {symbol} ({sum_})")
            if is_changing:
                changing_positions.append(i + 1)

        original_number = self.calculate_hexagram_number(lines)
        original = self.data[original_number]
        print("\n===== Original Hexagram 本卦 =====")
        self.display_hexagram(original, lines)

        if changing_positions:
            print(f"\nChanging lines 變爻: {', '.join(map(str, changing_positions))}")
            changed_lines = [
                Line(line.line_number, not line.is_yang if line.is_changing else line.is_yang, False)
                for line in lines
            ]
            changed_number = self.calculate_hexagram_number(changed_lines)
            transformed = self.data[changed_number]
            print("\n===== Transformed Hexagram 之卦 =====")
            self.display_hexagram(transformed, changed_lines)

    def lookup_hexagram(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            n = int(input("Enter hexagram number (1-64): "))
            if 1 <= n <= 64:
                info = self.data[n]
                lines = self.generate_lines_from_number(n)
                self.display_hexagram(info, lines)
            else:
                print("Invalid.")
        except ValueError:
            print("Invalid.")

    def throw_coins(self):
        return sum(2 if self.rng.randint(0, 1) == 0 else 3 for _ in range(3))

    def get_line_symbol(self, yang, changing):
        if yang and changing: return "━━━━━━ ○ (old Yang 9)"
        if yang: return "━━━━━━   (young Yang 7)"
        if not yang and changing: return "━━  ━━ × (old Yin 6)"
        return "━━  ━━   (young Yin 8)"

    def calculate_hexagram_number(self, lines):
        lower = self.trigram_index(lines[0], lines[1], lines[2])
        upper = self.trigram_index(lines[3], lines[4], lines[5])
        return self.king_wen_lookup[lower][upper]

    def trigram_index(self, l1, l2, l3):
        val = 0
        if l1.is_yang: val |= 1
        if l2.is_yang: val |= 2
        if l3.is_yang: val |= 4
        return {
            7: 0, 6: 4, 5: 2, 4: 6,
            3: 1, 2: 5, 1: 3, 0: 7
        }.get(val, 7)

    def generate_lines_from_number(self, hexagram_number):
        for upper in range(8):
            for lower in range(8):
                if self.king_wen_lookup[upper][lower] == hexagram_number:
                    return [
                        Line(1, bool(lower & 1), False),
                        Line(2, bool(lower & 2), False),
                        Line(3, bool(lower & 4), False),
                        Line(4, bool(lower & 1), False),
                        Line(5, bool(lower & 2), False),
                        Line(6, bool(lower & 4), False),
                    ]
        return [Line(i, True, False) for i in range(1, 7)]

    def display_hexagram(self, info, lines):
        print(f"No.{info.number} {info.chinese_name} {info.name}")
        print(f"Upper 上卦: {info.upper_trigram}   Lower 下卦: {info.lower_trigram}\n")
        for line_num in range(6, 0, -1):
            line = next(l for l in lines if l.line_number == line_num)
            symbol = "━━━━━━" if line.is_yang else "━━  ━━"
            print(f"{symbol}  (Line {line.line_number})")
        print("\nJudgment 卦辭:")
        print(f"  {info.judgment_cn}")
        print(f"  {info.judgment_en}")
        print("\nImage 象曰:")
        print(f"  {info.image_cn}")
        print(f"  {info.image_en}")
        print("\nSample Use 應用示例:")
        print(f"  {info.sample_use}")

    def load(self, path):
        with open(path, encoding='utf-8') as f:
            raw = json.load(f)
        return {h["Number"]: HexagramInfoFull(h) for h in raw}

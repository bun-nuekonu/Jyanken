# GitHub PR画面での不可視文字検出テスト
# このファイルには意図的に不可視文字が埋め込まれています

# ===========================================
# 1. Zero Width Space (U+200B) - 変数名に潜む
# ===========================================
price​_total = 100
order​_count = 5

# ===========================================
# 2. Zero Width Non-Joiner (U+200C)
# ===========================================
user‌name = "admin"
pass‌word = "secret123"

# ===========================================
# 3. Zero Width Joiner (U+200D)
# ===========================================
access‍_token = "abc123"

# ===========================================
# 4. Right-to-Left Override (U+202E) - 最も危険
# ===========================================
# ‮ access_granted = True
is_admin = False  # ‮ ;eurT = nimda_si

# ===========================================
# 5. BOM (U+FEFF) - 行頭に潜む
# ===========================================
﻿config_value = "production"

# ===========================================
# 6. Soft Hyphen (U+00AD) - 見えないハイフン
# ===========================================
check­_permission = True
vali­date_input = False

# ===========================================
# 7. Left-to-Right Mark (U+200E)
# ===========================================
file‎_path = "/etc/passwd"

# ===========================================
# 8. Word Joiner (U+2060)
# ===========================================
secret⁠_key = "do_not_expose"

# ===========================================
# 9. Variation Selector - 異体字セレクタ
# ===========================================

# 9-1. VS16 (U+FE0F) - 絵文字の異体字セレクタ
warning_icon = "⚠️"      # U+26A0 + U+FE0F
star_icon = "☆️"           # U+2606 + U+FE0F
check_icon = "✓️"          # U+2713 + U+FE0F

# 9-2. VS1-VS3 (U+FE00-U+FE02) - 標準異体字セレクタ
cjk_var1 = "邊︀"          # 邊 + VS1 (U+FE00)
cjk_var2 = "邊︁"          # 邊 + VS2 (U+FE01)
cjk_var3 = "邊︂"          # 邊 + VS3 (U+FE02)

# 9-3. IVS (U+E0100-U+E0103) - 漢字異体字セレクタ（SVSよりこちらが多用される）
ivs_tsuji1 = "辻󠄀"       # 辻 + VS17 (U+E0100) - 一点しんにょう
ivs_tsuji2 = "辻󠄁"       # 辻 + VS18 (U+E0101) - 二点しんにょう
ivs_watanabe1 = "渡󠄀"    # 渡 + VS17 (U+E0100)
ivs_watanabe2 = "渡󠄁"    # 渡 + VS18 (U+E0101)
ivs_saitou1 = "齋󠄀"      # 齋 + VS17 (U+E0100)
ivs_saitou2 = "齋󠄁"      # 齋 + VS18 (U+E0101)
ivs_takahashi = "髙󠄀"    # 髙 + VS17 (U+E0100) - はしごだか

# 9-4. 異体字セレクタが変数名に紛れ込むケース
# 見た目は同じだが異なる変数になる可能性
name_a = "葛飾区"          # 通常の「葛」
name_b = "葛󠄀飾区"        # 「葛」+ VS17 - 見た目ほぼ同じだが別の文字列

# ===========================================
# 10. 正常なコード（比較用）
# ===========================================
normal_variable = "this is clean"
clean_function_name = True
regular_price = 200


def calculate_total():
    """正常に見えるが不可視文字が含まれる"""
    total = price​_total * order​_count
    if check­_permission:
        return total
    return 0


def authenticate(user, pw):
    """認証関数 - 変数名に不可視文字"""
    if user == user‌name and pw == pass‌word:
        token = access‍_token
        return token
    return None


# 正常な関数（比較用）
def clean_function(x, y):
    return x + y

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
# 9. Variation Selector (U+FE0F, U+E0100)
# ===========================================
warning_icon = "⚠️"
kanji_variant = "辻󠄀"

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

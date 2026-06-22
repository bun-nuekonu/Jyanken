# GitHub PR画面での不可視文字検出テスト
# このファイルには意図的に不可視文字が埋め込まれています

# 1. Zero Width Space (U+200B)
price​_total = 100

# 2. Zero Width Non-Joiner (U+200C)
user‌name = "admin"

# 3. Zero Width Joiner (U+200D)
access‍_token = "abc123"

# 4. Right-to-Left Override (U+202E) - 最も危険
is_admin = False  # ‮ ;eurT = nimda_si

# 5. BOM (U+FEFF)
﻿config_value = "production"

# 6. Soft Hyphen (U+00AD)
pass­word = "secret"

# 7. Left-to-Right Mark (U+200E)
file‎_path = "/etc/passwd"

# 8. Word Joiner (U+2060)
secret⁠_key = "do_not_expose"

# 9. Variation Selector - 異体字セレクタ
warning_icon = "⚠️"        # VS16 (U+FE0F) - 絵文字
cjk_var = "邊︀"             # VS1 (U+FE00) - 標準異体字セレクタ
ivs_tsuji = "辻󠄀"          # VS17 (U+E0100) - 漢字異体字セレクタ(IVS)

# 10. 正常なコード（比較用）
normal_variable = "this is clean"
regular_price = 200

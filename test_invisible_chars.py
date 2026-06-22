# GitHub PR画面での不可視文字検出テスト
# このファイルには意図的に不可視文字が埋め込まれています

# 1. ゼロ幅スペース (U+200B)
price​_total = 100

# 2. ゼロ幅非接合子 (U+200C)
user‌name = "admin"

# 3. ゼロ幅接合子 (U+200D)
access‍_token = "abc123"

# 4. 右から左への上書き (U+202E) - 以降の文字が逆順表示される
print("Hello")‮  # 実際にはprint("Hello")と書いてあるが逆順に表示される

# 5. バイトオーダーマーク (U+FEFF)
﻿config_value = "production"

# 6. ソフトハイフン (U+00AD)
pass­word = "secret"

# 7. 左から右へのマーク (U+200E)
file‎_path = "/etc/passwd"

# 8. 単語結合子 (U+2060)
secret⁠_key = "do_not_expose"

# 9. 異体字セレクタ
warning_icon = "⚠️"        # 絵文字用 (U+FE0F)
cjk_var = "邊︀"             # 標準異体字セレクタ (U+FE00)
ivs_tsuji = "辻󠄀"          # 漢字異体字セレクタ (U+E0100)

# 10. 正常なコード（比較用）
normal_variable = "this is clean"
regular_price = 200

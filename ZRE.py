import re
# ---------------------------------------------------------
m = re.match(r'\d+', '123abc')
if m:
    print(m.group())  # '123'

# ---------------------------------------------------------
s = 'abc123def'
m = re.search(r'\d+', s)
if m:
    print(m.group())  # '123'

# ---------------------------------------------------------
s = 'abc 123 def 456'
numbers = re.findall(r'\d+', s)  # ['123', '456']

# ---------------------------------------------------------
s = 'abc 123 def 456'
for m in re.finditer(r'\d+', s):
    print(m.group())  # '123', '456'

# ---------------------------------------------------------
s = 'abc 123 def 456'
s2 = re.sub(r'\d+', 'X', s)  # 'abc X def X'

# ---------------------------------------------------------
s2, n = re.subn(r'\d+', 'X', s)
# s2 = 'abc X def X', n = 2

# ---------------------------------------------------------
s = 'a,b;c d'
parts = re.split(r'[ ,;]+', s)  # ['a', 'b', 'c', 'd']

# ---------------------------------------------------------
pattern = re.compile(r'\d+')
pattern.findall('123 abc 456')  # ['123', '456']

# ---------------------------------------------------------
m = re.search(r'\d+', 'abc123def')
m.group()  # '123'
m.start()  # 3
m.end()    # 6
m.span()   # (3,6)

# | Ký tự   | Ý nghĩa                      |    |
# | ------- | ---------------------------- | -- |
# | `.`     | 1 ký tự bất kỳ (trừ newline) |    |
# | `^`     | Bắt đầu chuỗi                |    |
# | `$`     | Kết thúc chuỗi               |    |
# | `*`     | 0 hoặc nhiều lần lặp         |    |
# | `+`     | 1 hoặc nhiều lần lặp         |    |
# | `?`     | 0 hoặc 1 lần                 |    |
# | `{n}`   | đúng n lần                   |    |
# | `{n,m}` | từ n đến m lần               |    |
# | `[]`    | tập ký tự, `[a-z]`           |    |
# | `\d`    | chữ số `[0-9]`               |    |
# | `\D`    | không phải chữ số            |    |
# | `\w`    | chữ cái, số, `_`             |    |
# | `\W`    | không phải chữ cái, số, `_`  |    |
# | `\s`    | khoảng trắng                 |    |
# | `\S`    | không phải khoảng trắng      |    |
# | `       | `                            | OR |
# | `()`    | nhóm, dùng trong `group()`   |    |



# ---------------------------------------------------------
re.IGNORECASE   # i: không phân biệt hoa thường
re.MULTILINE    # m: ^ $ áp dụng cho nhiều dòng
re.DOTALL       # s: . match cả newline
re.VERBOSE      # x: regex dễ đọc, cho phép comment

re.search(r'abc', s, re.IGNORECASE)

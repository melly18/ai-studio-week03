def read_text_safely(path):
    for enc in ("utf-8", "cp949"):
        try:
            with open(path, "r", encoding=enc) as f:
                f.read()
                return enc
        except UnicodeDecodeError:
            continue
    raise ValueError(f"지원하지 않는 인코딩: {path}")

import pandas as pd

enc = read_text_safely("RAW_DATA.csv")
df = pd.read_csv("RAW_DATA.csv", encoding=enc)
"""
pd.set_option("display.width", 180)
print(df.shape)
(500, 5)

print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 5 columns):
  #  Column  Non-Null Count  Dtype
 --- ------  --------------  -----
  0  주문일자     500 non-null    str
  1  상품명     500 non-null    str
  2  카테고리     500 non-null    str
  3  단가      500 non-null    str
  4  수량      500 non-null    int64
dtypes: int64(1), str(4)
memory usage: 19.7 KB
None
"""
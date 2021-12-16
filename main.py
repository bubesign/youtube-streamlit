from pandas._config.config import option_context
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 入門')

st.write(' progress barの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ')

text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味：',text
'コンディション：',condition



if st.checkbox('Show Image'):

    img = Image.open('sample.jpg')
    st.image(img, caption = 'takugymnastics',use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df)


# st.dataframe(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""


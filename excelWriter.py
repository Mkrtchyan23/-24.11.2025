import pandas as pd
df1 = pd.DataFrame = input("Введите ваше имя: ", )
df2 = pd.DataFrame = str("Введите ваш возраст: ")
with pd.ExcelWriter('мкртчянэксель.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Лист1', index=False)
    df2.to_excel(writer, sheet_name='Лист2', index=False)


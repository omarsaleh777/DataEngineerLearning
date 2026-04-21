import pandas as pd

data = {
    'Component': ['CPU', 'GPU', 'RAM', 'Motherboard', 'SSD'],
    'Name': ['Ryzen 5 7600', 'RTX 4060', 'Corsair 32GB', 'B650 Tomahawk', 'Samsung 1TB'],
    'Price_SR': [850, 1200, 450, 800, 350]
}
df=pd.DataFrame(data)
print(df)
print(df.iloc[1,2])
x=df[['Component']]
print(x)
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') &
        (products['recyclable'] ==  'Y')].loc[:,['product_id']]
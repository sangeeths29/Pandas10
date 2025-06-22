# Problem 1 - Group Sold Products by the Date (https://leetcode.com/problems/group-sold-products-by-the-date/)
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        product = ('product', lambda x : ','.join(sorted(set(x))))
    ).reset_index()

    return groups.sort_values(by = ['sell_date']).rename(columns = {'product' : 'products'})
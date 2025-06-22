# Problem 2 - Daily Leads and Partners ( https://leetcode.com/problems/daily-leads-and-partners/ )
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    salegroups = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique')
    ).reset_index()

    return salegroups.sort_values(by = ['date_id'])
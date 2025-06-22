# Problem 3 - Actors and Directors who Cooperated At Least Three Times (https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    freq_pairs = counts[counts['count'] >= 3]
    return freq_pairs[['actor_id', 'director_id']]
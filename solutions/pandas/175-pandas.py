"""175). Combine Two Tables
- Problem description: https://leetcode.com/problems/combine-two-tables/description/
"""
import pandas as pd
import numpy as np


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, how='left', on='personId')[['firstName', 'lastName', 'city', 'state']]


if __name__ == "__main__":
    # Prepare data
    person_type = {'personId': 'Int64', 'firstName': 'object', 'lastName': 'object'}
    person = pd.DataFrame([[1, 'Allen', 'Wang'], [2, 'Bob', 'Alice']],
                          columns=['personId', 'firstName', 'lastName']).astype(person_type)

    address_type = {'addressId': 'Int64', 'personId': 'Int64', 'city': 'object', 'state': 'object'}
    address = pd.DataFrame([[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']],
                           columns=['addressId', 'personId', 'city', 'state']).astype(address_type)

    expected_result = [['Allen', 'Wang', np.nan, np.nan], ['Bob', 'Alice', 'New York City', 'New York']]

    result = combine_two_tables(person, address)
    print(result)
    assert result.values.tolist() == expected_result

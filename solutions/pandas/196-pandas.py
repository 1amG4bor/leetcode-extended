"""196). Delete Duplicate Emails
- Problem description> https://leetcode.com/problems/delete-duplicate-emails/description/
"""
import pandas as pd
import numpy as np


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person['rank'] = person.sort_values('id').groupby('email').rank(method='first').astype(int)
    person.drop(person[person['rank'] > 1].index, inplace=True)
    person.drop(columns=['rank'], inplace=True)


if __name__ == '__main__':
    data_columns = ['id', 'email']
    data_types = {'id': 'Int64', 'email': 'object'}
    data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]

    # Run tests
    person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'int64', 'email': 'object'})
    expected_result = [[1, 'john@example.com'], [2, 'bob@example.com']]

    delete_duplicate_emails(person)
    print(person)
    assert person.values.tolist() == expected_result

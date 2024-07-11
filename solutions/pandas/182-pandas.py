"""182). Duplicate Emails
- Problem description> https://leetcode.com/problems/duplicate-emails/description/
"""
import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = (person.groupby('email')['email']
                .agg(email_count='count', email='min')
                .reset_index(drop=True))
    return df[df.email_count > 1][['email']]


if __name__ == '__main__':
    data_columns = ['id', 'email']
    data_types = {'id': 'Int64', 'email': 'object'}
    data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
    expected_result = [['a@b.com']]

    # Run tests
    test_data = pd.DataFrame(data, columns=data_columns).astype(data_types)
    result = duplicate_emails(test_data)
    print(result)
    assert result.values.tolist() == expected_result

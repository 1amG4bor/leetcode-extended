"""176). Second Highest Salary
- Problem description> https://leetcode.com/problems/second-highest-salary/description/
"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.sort_values('salary', ascending=False)[['salary']].drop_duplicates()
    df = df.iloc[[1]] if len(df) > 1 else pd.DataFrame({'salary': [None]})
    return df.rename(columns={'salary': 'SecondHighestSalary'}).reset_index(drop=True)


if __name__ == '__main__':
    data_columns = ['id', 'salary']
    data_types = {'id': 'int64', 'salary': 'int64'}

    test_data = [
        [[1, 100], [2, 200], [3, 300]],
        [[1, 100]],
        [[1, 100], [2, 100]],
        [[1, 100], [2, 200]],
    ]

    expected_results = [
        [[200]], [[None]], [[None]], [[100]]
    ]

    # Run tests
    for idx, data in enumerate(test_data):
        print(f'{idx+1}. test:')
        employee = pd.DataFrame(data, columns=data_columns).astype(data_types)
        result = second_highest_salary(employee)
        print(result)
        assert result.values.tolist() == expected_results[idx]
        print(25 * "-", '\n')

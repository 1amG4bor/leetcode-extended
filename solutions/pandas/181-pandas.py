"""181). Employees Earning More Than Their Managers
- Problem description> https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
"""
import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee.drop(['managerId', 'name'], axis=1).add_prefix('mgr_'),
                  left_on='managerId', right_on='mgr_id')
    df = df[df.salary > df.mgr_salary][['name']]
    return df.rename(columns={'name': 'Employee'})


if __name__ == '__main__':
    data_columns = ['id', 'name', 'salary', 'managerId']
    data_types = {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'}
    data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
    expected_result = [['Joe']]

    # Run tests
    test_data = pd.DataFrame(data, columns=data_columns).astype(data_types)
    result = find_employees(test_data)
    print(result)
    assert result.values.tolist() == expected_result

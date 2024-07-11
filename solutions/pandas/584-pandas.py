"""584. Find Customer Referee"""
import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer.referee_id.isnull()) | (customer.referee_id != 2)][['name']]


if __name__ == '__main__':
    data_columns = ['id', 'name', 'referee_id']
    data_types = {'id': 'Int64', 'name': 'object', 'referee_id': 'Int64'}

    test_data = [1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]

    # Run test
    customer = pd.DataFrame(test_data, columns=data_columns).astype(data_types)
    print(find_customer_referee(customer))

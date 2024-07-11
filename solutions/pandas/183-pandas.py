"""183). Customers Who Never Order
- Problem description> https://leetcode.com/problems/customers-who-never-order/description/
"""
import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', left_on='id', right_on='customerId').drop(columns=['customerId'])
    return (df[df['id_y'].isnull()]
                .drop(columns=['id_x', 'id_y'])
                .reset_index(drop=True))


if __name__ == '__main__':
    customer_columns = ['id', 'name']
    customer_types = {'id': 'Int64', 'name': 'object'}
    customer_data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]

    order_columns = ['id', 'customerId']
    order_types = {'id': 'Int64', 'customerId': 'Int64'}
    order_data = [[1, 3], [2, 1]]

    # Run tests
    customers = pd.DataFrame(customer_data, columns=customer_columns).astype(customer_types)
    orders = pd.DataFrame(order_data, columns=order_columns).astype(order_types)
    expected_result = [['Henry'], ['Max']]

    result = find_customers(customers, orders)
    print(result)
    assert result.values.tolist() == expected_result

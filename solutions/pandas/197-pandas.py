"""197). Rising Temperature
- Problem description> https://leetcode.com/problems/rising-temperature/description/
"""
import pandas as pd

# pd.set_option('display.max_rows', 1000);
pd.set_option('display.max_columns', 1000);
pd.set_option('display.width', 1000)


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.copy(deep=True)
    df['prevDay'] = weather.recordDate + pd.Timedelta(days=-1)
    final = (df.merge(weather[['recordDate', 'temperature']],
                   left_on=df.prevDay, right_on=weather.recordDate,
                   suffixes=('', '_prev')))

    return final[final.temperature > final.temperature_prev][['id']].reset_index(drop=True)


if __name__ == '__main__':
    data_columns = ['id', 'recordDate', 'temperature']
    data_types = {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'}

    data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
    expected_result = [[2], [4]]

    # Run tests
    weather = pd.DataFrame(data, columns=data_columns).astype(data_types)
    result = rising_temperature(weather)
    print(result)
    assert result.values.tolist() == expected_result

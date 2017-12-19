# vis.py
# analysis of FDI vs. Oil Prices
# written by Nicholas Poet, 2017

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def main():
    import_fdi_me()
    # print(import_oil_price())
    return


def import_fdi_sa():
    with open('data/fdi_inflows.csv') as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            r.append(line)
        f.close()

    data = {}
    for i in r:
        if i['Country Name'] == 'Brazil':
            data.update({'Brazil': i})
        elif i['Country Name'] == 'Colombia':
            data.update({'Colombia': i})
        elif i['Country Name'] == 'Venezuela':
            data.update({'Venezuela': i})
    df = pd.DataFrame([data['Brazil'], data['Colombia'], data['Venezuela']])
    df = df.transpose()
    df = df.drop('Country Name')
    df = df.rename(index=str, columns={0: 'Brazil', 1: 'Colombia', 2: 'Venezuela'})
    # df = df.transpose()
    df = df.dropna()
    df = df.astype(float)
    # df['Brazil'].plot(kind='bar', x='Year', y='FDI Inflows ', title='FDI Inflows: Brazil (/100Bn USD)\n1975-2016',
    #                  color='g')
    # df['Colombia'].plot(kind='bar', x='Year', y='FDI Inflows ', title='FDI Inflows: Colombia (/10Bn USD)\n1975-2016',
    #                    color='y')
    # df['Venezuela'].plot(kind='bar', x='Year', y='FDI Inflows ',
    #                      title='FDI Inflows: Venezuela (/10Bn USD)\n1975-2016', color='r')
    d = import_oil_price()
    print(d)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    d.plot(kind='line', color='b', title='South American FDI\nvs. Crude Prices 1989-2016', ax=ax2)
    df.plot(kind='bar', ax=ax1)

    plt.show()
    return df


def import_fdi_me():
    with open('data/fdi_inflows.csv') as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            r.append(line)
        f.close()

    data = {}
    for i in r:
        if i['Country Name'] == 'Saudi Arabia':
            data.update({'Saudi Arabia': i})
        elif i['Country Name'] == 'United Arab Emirates':
            data.update({'United Arab Emirates': i})
        elif i['Country Name'] == 'Iran':
            data.update({'Iran': i})
    df = pd.DataFrame([data['Saudi Arabia'], data['United Arab Emirates'], data['Iran']])
    df = df.transpose()
    df = df.drop('Country Name')
    df = df.rename(index=str, columns={0: 'Saudi Arabia', 1: 'UAE', 2: 'Iran'})
    df = df.astype(float)
    # df['Saudi Arabia'].plot(kind='bar', x='Year', y='FDI Inflows ',
    #                         title='FDI Inflows: Saudi Arabia (/100Bn USD)\n1975-2016', color='g')
    # df['UAE'].plot(kind='bar', x='Year', y='FDI Inflows ', title='FDI Inflows: U.A.E. (/100Bn USD)\n1975-2016',
    #                                color='b')
    # df['Iran'].plot(kind='bar', x='Year', y='FDI Inflows ', title='FDI Inflows: Iran (/10Bn USD)\n1975-2016',
    #                color='black')
    d = import_oil_price()
    print(d)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    d.plot(kind='line', color='b', title='Middle East FDI\nvs. Crude Prices 1989-2016', ax=ax2)
    df.plot(kind='bar', ax=ax1)

    plt.show()
    return df


def import_oil_price():
    with open('data/oil.csv') as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            r.append(line)
        f.close()
    data = {}
    print(r)
    for i in r:
        data.update({i['Date']: i['WTI Spot Price']})
    df = pd.DataFrame(data, index=['Brent Crude Price (USD)'])
    df = df.transpose()
    df['Brent Crude Price (USD)'].replace('', np.nan, inplace=True)
    df = df.dropna()
    df = df.astype(float)
    return df


if __name__ == '__main__':
    main()

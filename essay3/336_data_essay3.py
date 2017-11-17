# 336_data_essay_3.py
# analysis of energy access and use vs. democratic level
# Data Sources:
#   - World Bank Economic Indicators API
#   - Center for Systemic Peace INSCR Data Page
# written by Nicholas Poet, 2017
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def main():
    a = energy_vs_dem_level_df()
    vis_fig1(a)
    c = energy_access_vs_dem_level()
    vis_fig2(c)
    return


def energy_vs_dem_level_df():
    with open("essay3/data/energy_wb.csv") as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            r.append(line)

    data = {}
    lst = import_ibrd_csv()
    for i in r:
        # print(i)
        if "Electric power consumption (kWh per capita)" in i['Indicator Name']:
            if i['Country Name'] in lst:
                data.update({i['Country Name']: i['2014']})

    df = pd.DataFrame(data, index=['Energy Consumption (kWh per capita)'])
    df = df.transpose()
    df['Polity2 Dem Level'] = import_dem_lvl()
    df['Energy Consumption (kWh per capita)'].replace('', np.nan, inplace=True)
    df = df.dropna()
    return df


def energy_access_vs_dem_level():
    with open("essay3/data/energy_access.csv") as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            r.append(line)

    data = {}
    lst = import_ibrd_csv()
    for i in r:
        # print(i)
        if "Access to electricity (% of population)" in i['Indicator Name']:
            if i['Country Name'] in lst:
                data.update({i['Country Name']: i['2014']})
    df = pd.DataFrame(data, index=['Energy Access (% of population)'])
    df = df.transpose()
    df['Polity2 Dem Level'] = import_dem_lvl()
    df['Energy Access (% of population)'].replace('', np.nan, inplace=True)
    df = df.dropna()
    return df


def import_ibrd_csv():
    with open("essay3/data/ibrd.csv") as f:
        reader = csv.DictReader(f)
        r = []
        for line in reader:
            if line['GroupCode'] == 'IBD':
                r.append(line['CountryName'])
    return r


def import_dem_lvl():
    with open("essay3/data/polityIV.csv") as f:
        reader = csv.DictReader(f)
        dem = []
        for line in reader:
            dem.append(line)
    data = {}
    lst = import_ibrd_csv()
    for d in dem:
        if d['country'] in lst:
            if d['year'] == '2014':
                data.update({d['country']: d['polity2']})
    df = pd.DataFrame(data, index=['Polity2 Dem Level'])
    df = df.transpose()
    return df


def vis_fig1(df):
    df = df.astype(float)
    ax = df.plot(kind='scatter', title='Energy Consumption vs. Democratic Level 2014:\n IBRD Developing Nations',
                 y='Energy Consumption (kWh per capita)', x='Polity2 Dem Level')
    plt.show()
    return ax


def vis_fig2(df):
    df = df.astype(float)
    ax = df.plot(kind='scatter', title='Energy Access vs. Democratic Level 2014:\n IBRD Developing Nations',
                 x='Energy Access (% of population)', y='Polity2 Dem Level')
    plt.show()
    return ax


if __name__ == '__main__':
    main()

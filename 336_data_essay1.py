# 336_data_essay1.py
# analysis of GDP per Capita, Electricity use per Capita, and Democratic Level for
#   all nations (data permitting). Most recent aggregate data from 2014.
#   Data Sources:
#       - GDP per Capita: World Bank Economic Indicators API (2014 Nominal GDP per cap. in USD)
#       - Electricity use per Capita: World Bank Economic Indicators API (2014 kWh use per capita)
#       - Democratic Level: Center for Systemic Peace INSCR Data Page (Polity 2 Score)
# written by Nicholas Poet, 2017


import csv
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# run basic visualizer functions
def main():
    vis_gdp_elec(wb_gdp(), wb_elec())
    vis_elec_dem(wb_elec(), dem_level())
    return


# collect and parse data for World Bank GDP in 2014
def wb_gdp():
    with open('gdppercap.csv', 'r') as f:
        reader = csv.DictReader(f)
        gdp = []
        for line in reader:
            gdp.append(line)
    data = {}
    for g in gdp:
        try:
            data.update({g['\ufeff"Data Source"']: g[None][55]})    # 2014 GDP values occur in the 56th entry
        except KeyError:    # poorly encoded set, avoids conversion issues with non-utf-8 chars
            pass
    data.pop('Country Name')
    return data


# collect and parse data for World Bank Electricity use 2014
def wb_elec():
    with open('elecpercap.csv', 'r') as f:
        reader = csv.DictReader(f)
        elec = []
        for line in reader:
            elec.append(line)
    data = {}
    for e in elec:
        data.update({e['Country Name']: e['2014 [YR2014]']})
    return data


# collect and parse data for Polity2 Democracy Level 2014
def dem_level():
    with open('polityIV.csv', 'r') as f:
        reader = csv.DictReader(f)
        dem = []
        for line in reader:
            dem.append(line)
    data = {}
    for d in dem:
        if d['year'] == '2014':
            data.update({d['country']: d['polity2']})
    return data


# visualize data sets for gdp/elec use, take dictionaries for df creation
def vis_gdp_elec(gdp, elec):
    gdp1 = {}
    elec1 = {}
    for key in gdp.keys():
        if key in elec.keys():
            gdp1.update({key: gdp[key]})
            elec1.update({key: elec[key]})
    df = pd.DataFrame([gdp1, elec1])
    for country in df:    # clean data sets, remove countries with incomplete entries
        if df[country][0] == '..' or df[country][1] == '..':
            df.pop(country)
        elif df[country][0] == '' or df[country][1] == '':
            df.pop(country)
    df.dropna()
    df = df.transpose()    # transpose DataFrame for graphing
    df = df.rename(index=str, columns={0: 'GDP($) per Capita', 1: 'kWh per Capita'})
    df = df.iloc[1:]
    df = df.astype(float)
    ax = df.plot(kind='scatter', x='GDP($) per Capita', y='kWh per Capita', loglog=True,
                 title='Electricity Consumption vs. GDP 2014')
    ax.set_ylabel("Electricity Consumption (mWh per Capita)")
    ax.set_xlabel("GDP ($ equivalent per Capita)")
    ax.scatter(df['GDP($) per Capita']['World'], df['kWh per Capita']['World'],
               marker='o', color='red')
    ax.scatter(df['GDP($) per Capita']['United States'], df['kWh per Capita']['United States'],
               marker='o', color='orange')
    plt.interactive(False)
    plt.show()
    fig = ax.get_figure()
    fig.savefig('elec_gdp.png')


# visualize data sets for elec use/dem level, take dictionaries for df creation
def vis_elec_dem(elec, dem):
    elec1 = {}
    dem1 = {}
    for key in elec.keys():
        if key in dem.keys():
            elec1.update({key: elec[key]})
            dem1.update({key: dem[key]})
    df = pd.DataFrame([elec1, dem1])
    for country in df:    # clean data sets, remove countries with incomplete entries
        if df[country][0] == '..' or df[country][1] == '..':
            df.pop(country)
        elif df[country][0] == '' or df[country][1] == '':
            df.pop(country)
    df = df.transpose()    # transpose DataFrame for graphing
    df = df.rename(index=str, columns={0: 'kWh per Capita', 1: 'Democracy Level'})
    df = df.astype(float)
    ax = df.plot(kind='scatter', x='Democracy Level', y='kWh per Capita',
                 title='Electricity Consumption vs. Democracy Level 2014', logy=True)
    ax.set_ylabel("Electricity Consumption (mWh per Capita)")
    ax.set_xlabel("Democracy Level (Polity2 Score)")
    ax.scatter(df['Democracy Level']['United States'], df['kWh per Capita']['United States'],
               marker='o', color='orange')
    plt.interactive(False)
    plt.show()
    fig = ax.get_figure()
    fig.savefig('elec_dem.png')


if __name__ == '__main__':
    main()

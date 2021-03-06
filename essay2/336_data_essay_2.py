# 336_data_essay_2.py
# analysis of TPES in Bolivia in 2015 and from 1990-Present.
#   Data Sources:
#       - t_XXXX data from International Energy Agency
#  written by Nicholas Poet, 2017

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def main():
    df = parse_data()
    vis_line(df)
    vis_pie(df)
    return


def vis_line(df):
    df = df.transpose()
    df = df.rename(index=str, columns={0: 'Coal',  1: 'Crude Oil',  2: 'Oil Products', 3: 'Natural Gas', 4: 'Nuclear',
                                       5: 'Hydro', 6: 'Geothermal', 7: 'Biofuels',     8: 'Electricity', 9: 'Heat'})
    # print(df)
    ax = df.plot(kind='line', linewidth=3, cmap='Paired', title='Bolivian TPES per Year, 1990-Present')
    ax.set_ylabel('TPES (ktoe)')
    ax.set_xlabel('Year')
    plt.interactive(False)
    plt.show()
    return ax


def vis_pie(df):
    df = df.transpose()
    y2015 = []
    for i in df:
        y2015.append(df[i]['2015'])
    print(y2015)
    ndf = pd.DataFrame(y2015, index=['Coal', 'Crude Oil', 'Oil Products', 'Natural Gas', 'Nuclear',
                                     'Hydro', '', 'Biofuels', 'Electricity', 'Heat'])
    # print(ndf)
    explode = (0, 0.05, 0, 0.05, 0, 0, 0, 0, 0, 0)
    ax = ndf.plot(kind='pie', explode=explode, cmap='Paired', autopct=autopct, subplots=True)
    plt.interactive(False)
    plt.axis('equal')
    plt.ylabel('')
    plt.xlabel('Bolivian TPES by ktoe Equivalent 2015')
    plt.show()
    return ax


def autopct(pct):
    return ('%.2f%%' % pct) if pct > 5 else ''


def parse_data():
    t_1990 = [0, 1304, -177,  627, 0, 101, 0,  754, 1, 0]
    t_1991 = [0, 1328, -196,  658, 0, 112, 0,  788, 1, 0]
    t_1992 = [0, 1310, -133,  795, 0, 109, 0,  768, 1, 0]
    t_1993 = [0, 1331,  -62,  821, 0, 129, 0,  827, 1, 0]
    t_1994 = [0, 1533,  -99,  964, 0, 113, 0,  842, 1, 0]
    t_1995 = [0, 1796,  -71, 1070, 0, 109, 0,  861, 1, 0]
    t_1996 = [0, 1977, -100, 1219, 0, 123, 0,  828, 1, 0]
    t_1997 = [0, 1923,   65, 1470, 0, 135, 0,  820, 1, 0]
    t_1998 = [0, 2197,   60, 1258, 0, 134, 0,  812, 1, 0]
    t_1999 = [0, 2041,   29, 1356, 0, 154, 0,  804, 1, 0]
    t_2000 = [0, 1680,   27, 2342, 0, 167, 0,  687, 1, 0]
    t_2001 = [0, 1930, -164, 1180, 0, 183, 0,  686, 1, 0]
    t_2002 = [0, 1975, -243, 1968, 0, 189, 0,  685, 1, 0]
    t_2003 = [0, 2228, -105, 1777, 0, 171, 0,  685, 1, 0]
    t_2004 = [0, 2364, -218, 1742, 0, 185, 0,  690, 0, 0]
    t_2005 = [0, 2607, -252, 1970, 0, 169, 0,  700, 0, 0]
    t_2006 = [0, 2551, -216, 3253, 0, 186, 0,  727, 0, 0]
    t_2007 = [0, 2617,  -78, 1807, 0, 199, 0,  751, 0, 0]
    t_2008 = [0, 2665,  -94, 2083, 0, 199, 0,  781, 0, 0]
    t_2009 = [0, 2356,  200, 2196, 0, 197, 0,  812, 0, 0]
    t_2010 = [0, 2393,  332, 2500, 0, 188, 0,  888, 0, 0]
    t_2011 = [0, 2464,  424, 2675, 0, 202, 0,  924, 0, 0]
    t_2012 = [0, 2875,  652, 2956, 0, 202, 0,  960, 0, 0]
    t_2013 = [0, 2925,  566, 3078, 0, 218, 0,  998, 0, 0]
    t_2014 = [0, 3062,  608, 3342, 0, 194, 1, 1039, 0, 0]
    t_2015 = [0, 3400,  448, 3137, 0, 212, 2, 1080, 0, 0]
    t_total = {'1990': t_1990, '1991': t_1991, '1992': t_1992, '1993': t_1993, '1994': t_1994,
               '1995': t_1995, '1996': t_1996, '1997': t_1997, '1998': t_1998, '1999': t_1999,
               '2000': t_2000, '2001': t_2001, '2002': t_2002, '2003': t_2003, '2004': t_2004,
               '2005': t_2005, '2006': t_2006, '2007': t_2007, '2008': t_2008, '2009': t_2009,
               '2010': t_2010, '2011': t_2011, '2012': t_2012, '2013': t_2013, '2014': t_2014,
               '2015': t_2015}
    df = pd.DataFrame(t_total)
    return df


if __name__ == '__main__':
    main()

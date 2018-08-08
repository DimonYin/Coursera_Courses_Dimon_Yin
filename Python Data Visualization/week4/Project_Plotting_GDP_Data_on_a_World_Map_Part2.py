"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """

    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    filename = codeinfo["codefile"]
    keyfield = codeinfo["plot_codes"]
    separator = codeinfo["separator"]
    quote = codeinfo["quote"]

    dic1 = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    list1 = []
    list2 = []
    for dic in dic1:
        for dic3 in dic1[dic]:
            if dic3 == codeinfo["plot_codes"]:
                list1.append(dic1[dic][dic3])
            if dic3 == codeinfo["data_codes"]:
                list2.append(dic1[dic][dic3])
    dic2 = {}
    for item in range(0, len(list1)):
        dic2[list1[item]] = list2[item]

    return dic2

def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    dic1 = {}
    for key in plot_countries:
        for dic in gdp_countries:
            for key1 in gdp_countries[dic]:
                if plot_countries[key] == gdp_countries[dic][key1]:
                    dic1[key] = dic

    dic2 = {}
    for dic in gdp_countries:
        for key1 in gdp_countries[dic]:
            dic2[gdp_countries[dic][key1]] = key1

    set1 = set()
    for key in plot_countries:
        if plot_countries[key] in dic2:
            pass
        else:
            set1.add(key)

    return dic1, set1

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    filename1 = gdpinfo["gdpfile"]
    keyfield1 = gdpinfo["country_code"]
    separator1 = gdpinfo["separator"]
    quote1 = gdpinfo["quote"]

    filename2 = codeinfo["codefile"]
    keyfield2 = codeinfo["data_codes"]
    separator2 = codeinfo["separator"]
    quote2 = codeinfo["quote"]

    dic1 = read_csv_as_nested_dict(filename1, keyfield1, separator1, quote1)
    dic2 = read_csv_as_nested_dict(filename2, keyfield2, separator2, quote2)

    dic15 = {}
    for dic in dic2:
        dic15[dic.upper()] = dic2[dic]

    set1 = set()
    for dic in dic1:
        if dic.upper() in dic15:
            set1.add(dic15[dic.upper()][codeinfo["plot_codes"]])

    set2 = set()
    for key in plot_countries:
        set2.add(plot_countries[key])

    set3 = set2 - set1
    set8 = set()
    for data in set3:
        for key in plot_countries:
            if data == plot_countries[key]:
                set8.add(key)

    dic4 = {}
    set4 = set()
    for dic in dic1:
        for dic3 in dic1[dic]:
            if dic3 == year:
                if dic1[dic][dic3].isdigit():
                    dic4[dic1[dic][gdpinfo["country_code"]]] = dic1[dic][dic3]
                else:
                    set4.add(dic1[dic][gdpinfo["country_code"]])

    dic7 = {}
    for data in set4:
        if data.upper() in dic15:
            dic7[dic15[data.upper()][codeinfo["plot_codes"]]] = data

    set5 = set()
    for dic in dic7:
        for key in plot_countries:
            if dic == plot_countries[key]:
                set5.add(key)

    dic10 = {}
    for dic in dic4:
        dic10[dic.lower()] = dic4[dic]

    dic5 = {}
    for dic in dic10:
        if dic.upper() in dic15:
            dic5[dic15[dic.upper()][codeinfo["plot_codes"]]] = dic10[dic]

    dic6 = {}
    for dic in plot_countries:
        if plot_countries[dic] in dic5:
            dic6[dic] = math.log(int(dic5[plot_countries[dic]]), 10)

    return dic6, set8, set5

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    dic1 = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)[0]
    set1 = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)[1]
    set2 = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)[2]

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = "GDP of Countries"
    worldmap_chart.add("Existed GDP Data", dic1)
    worldmap_chart.add("Missed GDP Data", set1)
    worldmap_chart.add("No GDP Data", set2)
    worldmap_chart.render(map_file)
    worldmap_chart.render_in_browser()

    return


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

test_render_world_map()
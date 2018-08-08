"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    dic1 = {}
    set1 = set()
    for key in gdp_countries:
        for key1 in plot_countries:
            if len(gdp_countries) != 0:
                if key == plot_countries[key1]:
                    dic1[key1] = plot_countries[key1]
                if plot_countries[key1] in gdp_countries:
                    pass
                else:
                    set1.add(key1)

    if len(gdp_countries) == 0:
        for key2 in plot_countries:
            set1.add(key2)

    return dic1, set1

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

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    filename = gdpinfo["gdpfile"]
    keyfield = gdpinfo["country_name"]
    separator = gdpinfo["separator"]
    quote = gdpinfo["quote"]

    dic1 = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    set1 = set()
    set2 = set()
    set3 = set()
    dic2 = {}
    for key in plot_countries:
        if plot_countries[key] in dic1:
            pass
        else:
            set1.add(key)

    for dic in dic1:
        for key in plot_countries:
            if year in dic1[dic] and plot_countries[key] in dic1:
                if dic == plot_countries[key]:
                    if dic1[dic][year].isdigit():
                        dic2[key] = math.log(int(dic1[dic][year]), 10)
                    else:
                        set2.add(dic1[dic]["Country Name"])

    for element in set2:
        for key in plot_countries:
            if element == plot_countries[key]:
                set3.add(key)

    return dic2, set1, set3

def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """

    dic1 = build_map_dict_by_name(gdpinfo, plot_countries, year)[0]
    set1 = build_map_dict_by_name(gdpinfo, plot_countries, year)[1]
    set2 = build_map_dict_by_name(gdpinfo, plot_countries, year)[2]

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
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

test_render_world_map()
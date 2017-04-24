#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint
from collections import defaultdict

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    # type: (object, object) -> object
    fieldtypes = defaultdict(set)

    input_file = csv.DictReader(open(filename))
    skip_lines(input_file, 3)

    #for row in input_file:
    #    print row["name"]
    #    #print row["isPartOf_label"][:1]
    #    #test_array = row["isPartOf_label"].split('|')
    #    print type(row["name"])
    #    test_int = is_int(row["name"])
    #    print test_int
        #print type([])
    #    break
    for row in input_file:
        for field in fields:
            #s = set()
            #if fieldtypes[field]:
            #    s = fieldtypes[field]
            v = row[field].strip()
            if v == "NULL":
                fieldtypes[field].add(type(None))
                #s.add(None)
            elif v[:1] == '{':
                fieldtypes[field].add(type([]))
                #fieldtypes[field].add(3)
                #fieldtypes[field] = row[field].split('|')
                #s.add([])
            elif is_int(v):
                fieldtypes[field].add(type(1))
                #fieldtypes[field] = int(row[field])
                #s.add(1)
            elif is_float(v):
                fieldtypes[field].add(type(1.1))
                #fieldtypes[field] = float(row[field])
                #s.add(1.1)

            #fieldtypes[field] = s






    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)
    print fieldtypes["areaLand"]

    #assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    #assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])


if __name__ == "__main__":
    test()

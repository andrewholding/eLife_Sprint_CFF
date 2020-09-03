#!/usr/bin/python
import os.path
from os import path


print("\nCitation Check")

filename = 'CITATION.cff'


if path.isfile(filename):
	print ("File " +  filename + " found")
else: 
	print("File " + filename + " not found")
	
#Load YAML
print ("\nLoad YAML")

import yaml

with open(filename) as file:
	try:
		citation = yaml.safe_load(file)
	except yaml.YAMLError as exc:
        	print(exc)

print("CFF contents = " + str(citation))

#Validate YAML
print ("\nValidate YAML")
from voluptuous import Schema, MultipleInvalid, Invalid, Required, Any, Optional, ALLOW_EXTRA

s = Schema({
	Required("doi"): str,
	Required("title"): str,
	Optional("version"): str,
	Required("authors"): str,
	Required("license"): str,
	},
	extra=ALLOW_EXTRA
	)

try:
	s(citation)
	print("Passed")	
except	 MultipleInvalid as e:
	exc = e
	print ("Error: " + str(exc))

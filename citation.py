#!/usr/bin/python
import os.path
from os import path


print("Citation Check")

filename = 'CITATION.cff'


if path.isfile(filename):
	print ("File " +  filename + " found")
else: 
	print("File " + filename + " not found")
	
#Load YAML
print ("Load YAML")

import yaml

with open(filename) as file:
	try:
		citation = yaml.safe_load(file)
	except yaml.YAMLError as exc:
        	print(exc)

print(citation)

#Validate YAML
print ("Validate YAML")
from voluptuous import Schema, MultipleInvalid, Invalid, Required

s = Schema({
	Required("foo"): str,
	Required("bar"): str
	})

try:
	s({'foo': "123"})
	raise AssertionError('MultipleInvalid not raised')
except	 MultipleInvalid as e:
	exc = e
	print exc
	print(str(exc) == "required key not provided @ data['foo']")
	print(str(exc) == "required key not provided @ data['bar']")


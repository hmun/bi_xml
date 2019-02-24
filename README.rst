******
bi_xml
******

SAP-BW XML-export transformation
################################

This python script can be used to transform the objects in the XML-file created from SAP-BW transport connection.
The basic idea is to export standard objects and rename them and all their attributes before importing it again.
In addition to renaming them they can be compounded to an additional InfoObject like i.e. 0SOURSYSTEM

Usage
*****

	usage: bi_xml.py [-h] [-i XML_IN] [-o XML_OUT] [-d DUMP_OUT] [-m IO_MAP_FILE]
	                 [-c IO_COMMON_FILE] [-e IO_EXISTING_FILE] [-p COMPOUND]
	                 [--no_description] [--new_description]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -i XML_IN, --in_file XML_IN
	                        import xml from in_file
	  -o XML_OUT, --out_file XML_OUT
	                        import xml from out_file
	  -d DUMP_OUT, --dump_file DUMP_OUT
	                        dump parsing information to dump_file
	  -m IO_MAP_FILE, --io_map IO_MAP_FILE
	                        read InfoObject name mapping from io_map
	  -c IO_COMMON_FILE, --io_common IO_COMMON_FILE
	                        read common InfoObjects from io_common
	  -e IO_EXISTING_FILE, --io_existing IO_EXISTING_FILE
	                        read existing InfoObjects from io_existing
	  -p COMPOUND, --compound COMPOUND
	                        compound all new InfoObjects to InfoObject compound
	  --no_description      remove the existing Description ojects
	  --new_description     create new Description objects from annotation tags

Parameter in Detail
*******************
-i --in_file
------------
XML-file created by the export from the SAP BW Transport Connection

-o --out_file
-------------
XML-file created by the script after the conversion.

-d --dump_file
--------------
The script creates six dump files with the following names and content:
<DUMP_OUT>_oi: the InfoObjects that have been contained in the original XML_IN file
<DUMP_OUT>_tags: the XML-tags that have been contained in the original XML_IN file
<DUMP_OUT>_xmid: the XML-ids that have been contained in the original XML_IN file
<DUMP_OUT>_after_oi: the InfoObjects that are contained in the resulting XML_OUT file
<DUMP_OUT>_after_tags: the XML-tags that are contained in the resulting XML_OUT file
<DUMP_OUT>_after_xmid: the XML-ids that are contained in the resulting XML_OUT file

This files are mainly used to analyze the objects, tags and xmids in the input and output xml files

-m --io_map
-----------
a CSV file containing two columns.
The name of the original InfoObject mapped to the name of the converted InfoObjects.
InfoObjects that are converted but are not contained in the map file will be added to the file using the simple rule:
new name = 'X' + characters 2 to 8 of the original name.
This file should be changed after the first run so that all InfoObjects are converted to meaningful and valid new names.
The new names have to be unique and must not end with character '_'

-c --io_common
--------------
a CSV file containing one column.
InfoObjects contained in this file will not be converted but referenced in the XML_OUT.
For example InfoObjects like 0COUNTRY or units should be contained in this file as they can be reused without conversion.

-e --io_existing
----------------
a CSV file containing one column.
InfoObjects contained in this file will not be contained in the resulting XML_OUT.
The idea is that these objects already exist in the target system with the correct name and settings in the target BI system.
InfoObjects from the IO_COMMON_FILE should also be contained in this file.
Or if one already converted and imported in the target BI system (like 0PLANT and all its attribute) do not need to be imported again.

-p --compound
-------------
Converted InfoObjects will be compounded to this InfoObject.
For example if one specifies 0SOURSYSTEM in this parameter then all converted InfoObjects will be compounded to 0SOURSYSTEM.
In this case the resulting InfoObjects can be used in BI systems with several source systems without conflicting attributes and texts. 

--no_description
----------------
If this parameter is specified all Description objects that are referenced by the original InfoObjects will be removed.
The main reason for this parameter is a bug in the current SAP BI releases.
The referenced Description objects are not unique because the GUUID in the export file is wrong (shortened to 25 digits from their original 32 digits).
If one keeps this references then the descriptions of the resulting InfoObjects will be all mixed up.

--new_description
-----------------
If this parameter is specified the script will create new Description objects using the annotation tags of the original InfoObjects.
It should only be specified together with --no_description

Remarks
*******
Routines
--------
InfoObject.routine and the referenced RoutineABAP objects will not be converted but kept as they are.
This means that the original routines like for example transfer routines of the original InfoObjects will be referencend.
One will have to check and correct the routines of the resulting InfoObjects.

InfoAreas
---------
The program also converts InfoAreas using the mapping information that is hard coded in InfoAreaMap.py
For whatever reason the resulting InfoAreas are not created when the XML_OUT file is imported in the target system (needs further investigation).

Original System
---------------
The converted InfoObjects are assigned to the original system that is hardcoded in InfoObject.py
This should be changed and will be replaces by a parameter in a later version
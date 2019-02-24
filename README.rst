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
Usage::
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



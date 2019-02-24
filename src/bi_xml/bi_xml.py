'''
Created on Feb 7, 2019

@author: hmun
'''
import xml.etree.ElementTree as ET
from InfoAreaMap import IAM
from InfoObject import IO

class BiXML:

    def __init__(self, in_file, io_map_file, io_common_file, io_existing_file):
        ET.register_namespace('XMISAPBI', "com.sap.bi/metadata/1.0")
        xml_file_name = in_file
        self.io = IO(io_map_file, io_common_file, io_existing_file)
        self.iam = IAM()
        try:
            self.doc = ET.parse(xml_file_name)
        except Exception as e:
            print(e.message)
        self.out_tags = []
        self.out_xmid = []
        self.out_io = []

    def convert(self, add_comp, no_description, new_description):
        try:
            for content in self.doc.findall('XMI.content'):
                for child in content.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Document'):
                    content.remove(child)                    
                for elem in content.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject'):
                    print(elem.tag)
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.document'):
                        elem.remove(child)
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.documentDefault'):
                        elem.remove(child)
                    name = elem.attrib['name']
                    print(name)
                    if not name in self.io.commonInfoObjects:
                        # comment: if infoObjectType="KYF" do not compound
                        no_compound_change = False
                        if elem.attrib['infoObjectType'] == 'KYF':
                            no_compound_change = True
                        newname = self.io.newName(name)
                        elem.attrib['name'] = newname
                        elem.attrib['fieldname'] = self.io.newFieldname(newname)
                        if elem.attrib['tableDataTimeDependent'] != '':
                            elem.attrib['tableDataTimeDependent'] = self.io.tableDataTimeDependent(newname)
                        if elem.attrib['tableDataTimeIndependent'] != '':
                            elem.attrib['tableDataTimeIndependent'] = self.io.tableDataTimeIndependent(newname)
                        if elem.attrib['tableHierarchies'] != '':
                            elem.attrib['tableHierarchies'] = self.io.tableHierarchies(newname)
                        if elem.attrib['tableHierarchiesIntervals'] != '':
                            elem.attrib['tableHierarchiesIntervals'] = self.io.tableHierarchiesIntervals(newname)
                        if elem.attrib['tableTexts'] != '':
                            elem.attrib['tableTexts'] = self.io.tableTexts(newname)
                        if elem.attrib['viewOnDB'] != '':
                            elem.attrib['viewOnDB'] = self.io.viewOnDB(newname)
                        if elem.attrib['xmi.id'] != '':
                            elem.attrib['xmi.id'] = self.io.xmID(newname)
                        if elem.attrib['originalSystem'] != '':
                            elem.attrib['originalSystem'] = self.io.originalSystem()
                        if elem.attrib['owner'] != '':
                            elem.attrib['owner'] = self.io.owner()
                        if elem.attrib['package'] != '':
                            elem.attrib['package'] = self.io.package()
                        # remove the number range
                        elem.attrib.pop("numberRangeNumber", None)
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.referencedInfoObject'):
                            # if the referenced info object is a global info object -> we must not change combounding
                            if self.xmid2name(child.attrib['xmi.idref']) in self.io.commonInfoObjects:
                                if no_compound_change == False:
                                    no_compound_change = True
                            child.attrib['xmi.idref'] = self.io.substName(child.attrib['xmi.idref'])
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.unitInfoObject'):
                            child.attrib['xmi.idref'] = self.io.substName(child.attrib['xmi.idref'])
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.aggregationOtherByInfoObject'):
                            child.attrib['xmi.idref'] = self.io.substName(child.attrib['xmi.idref'])
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.GISAttribute'):
                            child.attrib['xmi.idref'] = self.io.substName(child.attrib['xmi.idref'])                            
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoArea'):
                            child.attrib['xmi.idref'] = self.iam.get_map(child.attrib['xmi.idref'])
                            
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionLong'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                                elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])                    
                                if no_description:
                                    content.remove(elem_ref)
                            if no_description:
                                elem.remove(child)
                                
                                                       
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionShort'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                                elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])                    
                                if no_description:
                                    content.remove(elem_ref)
                            if no_description:
                                elem.remove(child)
                        # generate one new description from the InfoObjects annotation
                        if new_description:
                            new_child = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionShort')
                            new_uuid = self.io.new_uuid('0000000000000000000000000')
                            new_child.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                            elem.append(new_child)   
                            new_child = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionLong')
                            new_child.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                            elem.append(new_child)   
                            new_elem_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description')
                            new_elem_ref.attrib['xmi.id'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                            new_elem_ref.attrib['name'] = new_uuid
                            new_elem_ref.attrib['annotation'] = ''
                            new_elem_ref.attrib['language'] = 'EN'
                            new_elem_ref.attrib['mimeType'] = 'text/plain'
                            new_elem_ref.attrib['isBinary'] = 'false'
                            new_child_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description.body')
                            new_child_ref.text = elem.attrib['annotation'] 
                            new_elem_ref.append(new_child_ref)
                            content.append(new_elem_ref)                                

                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectAttributeAssoc'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectAttributeAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                            elem_ref = content.find(xp)
                            if elem_ref is not None:                            
                                elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                                elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])
                                for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectAttributeAssoc.attributeInfoObject'):
                                    child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                                    if self.xmid2name(child_ref.attrib['xmi.idref']) == add_comp and not no_compound_change:
                                        # need to delete the attribute and the attribute association
                                        elem.remove(child)
                                        content.remove(elem_ref)
                                    else:
                                        for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectAttributeAssoc.infoObject'):
                                            child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                                

                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectNavAttributeAssoc'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectNavAttributeAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                            elem_ref = content.find(xp)
                            if elem_ref is not None:                            
                                elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                                elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])
                                elem_ref.attrib['navAttributeNameReport'] = self.io.navAttributeNameReport(elem_ref.attrib['navAttributeNameReport'])
                                for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectNavAttributeAssoc.navAttributeInfoObject'):
                                    child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                                    # change the reporting name of the elem_ref
                                    if self.xmid2name(child_ref.attrib['xmi.idref']) == add_comp and not no_compound_change:
                                        # need to delete the attribute and the attribute association
                                        elem.remove(child)
                                        content.remove(elem_ref)
                                    else:
                                        for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectNavAttributeAssoc.infoObject'):
                                            child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                        
                        if not no_compound_change:
                            posnr_max = 0
                            for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectCompoundAssoc'):
                                posnr_max = posnr_max + 1
                                xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                                child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                                elem_ref = content.find(xp)
                                if elem_ref is not None:
                                    elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                                    elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])
                                    for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc.compoundInfoObject'):
                                        if self.xmid2name(child_ref.attrib['xmi.idref']) == add_comp:
                                            # already compounded to add_comp -> must not be added again
                                            no_compound_change = True
                                        child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                                    for child_ref in elem_ref.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc.infoObject'):
                                        child_ref.attrib['xmi.idref'] = self.io.substName(child_ref.attrib['xmi.idref'])
                                # add additional compounding
                            if add_comp != '':
                                new_child = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectCompoundAssoc')
                                new_uuid = self.io.new_uuid('00000000000000000000000000000000')
                                new_child.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.InfoObjectCompoundAssoc::'+new_uuid
                                elem.append(new_child)   
                                new_elem_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc')
                                new_elem_ref.attrib['annotation'] = ''
                                new_elem_ref.attrib['compoundType'] = ''
                                new_elem_ref.attrib['name'] = new_uuid
                                new_elem_ref.attrib['position'] = "{:04d}".format(posnr_max+1)
                                new_elem_ref.attrib['xmi.id'] = 'com.sap.bw.cwm.core.InfoObjectCompoundAssoc::'+new_uuid
                                new_child_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc.compoundInfoObject')
                                new_child_ref.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.InfoObject::'+add_comp
                                new_elem_ref.append(new_child_ref)
                                new_child_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc.infoObject')
                                new_child_ref.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.InfoObject::'+newname
                                new_elem_ref.append(new_child_ref)
                                content.append(new_elem_ref)
                    
#                    else:
#                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionLong'):
#                            self.io.sav_xmi_idref_uuid(child.attrib['xmi.idref'])
#                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionShort'):
#                            self.io.sav_xmi_idref_uuid(child.attrib['xmi.idref'])
#                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectAttributeAssoc'):
#                            self.io.sav_xmi_idref_uuid(child.attrib['xmi.idref'])
#                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectNavAttributeAssoc'):
#                            self.io.sav_xmi_idref_uuid(child.attrib['xmi.idref'])
#                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectCompoundAssoc'):
#                            self.io.sav_xmi_idref_uuid(child.attrib['xmi.idref'])
                        
                for elem in content.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.foundation.DataFlowAssoc'):
                    content.remove(elem)

                for elem in content.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea'):
                    if elem.attrib['name'] != '':
                        elem.attrib['name'] = self.iam.get_short_map(elem.attrib['name'])
                    if elem.attrib['xmi.id'] != '':
                        elem.attrib['xmi.id'] = self.iam.get_map(elem.attrib['xmi.id'])
                    if elem.attrib['originalSystem'] != '':
                        elem.attrib['originalSystem'] = self.io.originalSystem()
                    if elem.attrib['owner'] != '':
                        elem.attrib['owner'] = self.io.owner()
                    if elem.attrib['package'] != '':
                        elem.attrib['package'] = self.io.package()
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.document'):
                        elem.remove(child)
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.documentDefault'):
                        elem.remove(child)
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.descriptionShort'):
                        xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                        child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                        elem_ref = content.find(xp)
                        if elem_ref is not None:
                            elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                            elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])                    
                            if no_description:
                                content.remove(elem_ref)
                        if no_description:
                            elem.remove(child)
                    for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.descriptionLong'):
                        xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                        child.attrib['xmi.idref'] = self.io.get_xmi_idref_uuid(child.attrib['xmi.idref'])
                        elem_ref = content.find(xp)
                        if elem_ref is not None:
                            elem_ref.attrib['name'] = self.io.get_name_uuid(elem_ref.attrib['name'])
                            elem_ref.attrib['xmi.id'] = self.io.get_xmi_idref_uuid(elem_ref.attrib['xmi.id'])                    
                            if no_description:
                                content.remove(elem_ref)
                        if no_description:
                            elem.remove(child)

                    # generate one new description from the InfoObjects annotation
                    if new_description:
                        new_child = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.descriptionShort')
                        new_uuid = self.io.new_uuid('0000000000000000000000000')
                        new_child.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                        elem.append(new_child)   
                        new_child = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.whm.InfoArea.descriptionLong')
                        new_child.attrib['xmi.idref'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                        elem.append(new_child)   
                        new_elem_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description')
                        new_elem_ref.attrib['xmi.id'] = 'com.sap.bw.cwm.core.Description::'+new_uuid
                        new_elem_ref.attrib['name'] = new_uuid
                        new_elem_ref.attrib['annotation'] = ''
                        new_elem_ref.attrib['language'] = 'EN'
                        new_elem_ref.attrib['mimeType'] = 'text/plain'
                        new_elem_ref.attrib['isBinary'] = 'false'
                        new_child_ref = ET.Element('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description.body')
                        new_child_ref.text = elem.attrib['annotation'] 
                        new_elem_ref.append(new_child_ref)
                        content.append(new_elem_ref)                                
                    
#                name = elem.attrib.get('name')
#                name = 'X' + name[2:]
#                print(name)
#               InfoObject.setAttribute('name',name)
#            for InfoObject in self.doc.getElementsByTagName('XMISAPBI:com.sap.bw.cwm.core.InfoObject.document'):
                # print(InfoObject.tag)
#                parentNode = InfoObject.parentNode
#                parentNode.remove(InfoObject)
                # InfoObject.unlink()
#            with open(outFile, "w") as xml_file:
#                xml_file.close()
        except Exception as e:
            print(e.message)
            
    def clean_existing(self):
        try:
            for content in self.doc.findall('XMI.content'):
                for elem in content.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject'):
                    print(elem.tag)
                    name = elem.attrib['name']
                    print(name)
                    if name in self.io.existingObjects:
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionLong'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                content.remove(elem_ref)
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.descriptionShort'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.Description[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                content.remove(elem_ref)
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectAttributeAssoc'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectAttributeAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                content.remove(elem_ref)
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectNavAttributeAssoc'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectNavAttributeAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                content.remove(elem_ref)
                        for child in elem.findall('{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject.infoObjectCompoundAssoc'):
                            xp = './/'+'{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObjectCompoundAssoc[@xmi.id="'+child.attrib['xmi.idref']+'"]'
                            elem_ref = content.find(xp)
                            if elem_ref is not None:
                                content.remove(elem_ref)
                        content.remove(elem)        
        except Exception as e:
            print(e.message)
        
            
    def write(self, out_file, out_io_map_file):
        self.doc.write(out_file)
        self.io.writeInfoObjectMap(out_io_map_file)
        
            
    def xmid2name(self, xmid):
        split = xmid.split("::")
        if split[1] is not None:
            return split[1]
        else:
            return ''
            
    def dumpObjects(self, out_file):
        self.out_tags = []
        self.out_xmid = []
        self.out_io = []
        root = self.doc.getroot()
        self.dumpRecursive(root, 0)
        dumpFile_tags = out_file + "_tags"
        dumpFile_xmid = out_file + "_xmid"
        dumpFile_io = out_file + "_oi"
        dump_file = open(dumpFile_tags, "w")
        dump_file.writelines(self.out_tags)
        dump_file.close()                
        dump_file = open(dumpFile_xmid, "w")
        dump_file.writelines(self.out_xmid)
        dump_file.close()                
        dump_file = open(dumpFile_io, "w")
        dump_file.writelines(self.out_io)
        dump_file.close()                
       
    def dumpRecursive(self, elem, level):
        level = level + 1
        print(elem.tag)
        tags_line = str(level) + " " + elem.tag + '\n'
        if tags_line not in self.out_tags:
            self.out_tags.append(tags_line)
        if 'xmi.idref' in elem.attrib.keys():
            xmid_line = elem.attrib['xmi.idref'] + '\n'
            if xmid_line not in self.out_xmid:
                self.out_xmid.append(xmid_line)
        if (elem.tag) == '{com.sap.bi/metadata/1.0}com.sap.bw.cwm.core.InfoObject':
            io_line = elem.attrib['name'] + '\n'
            if io_line not in self.out_io:
                self.out_io.append(io_line)
        for child in elem:
            self.dumpRecursive(child, level)
                
if __name__ == '__main__':
    xml_in = '/users/hmun/SparkleShare/MSF/BI/ZCOPC_O07_DWH_necessary_bhd.xml'
    xml_out = '/users/hmun/SparkleShare/MSF/BI/ZCOPC_O07_DWH_necessary_bhd_out.xml'
    dump_out = '/users/hmun/SparkleShare/MSF/BI/dumpFile.txt'
    dump_out2 = '/users/hmun/SparkleShare/MSF/BI/dumpFile_after.txt'
    io_map_file = '/users/hmun/SparkleShare/MSF/BI/io_map.csv'
    io_common_file = '/users/hmun/SparkleShare/MSF/BI/io_common.csv'
    io_existing_file = '/users/hmun/SparkleShare/MSF/BI/io_existing.csv'

    biXML = BiXML(xml_in, io_map_file, io_common_file, io_existing_file)
    biXML.dumpObjects(dump_out)
    biXML.convert('0SOURSYSTEM', True, True)
    biXML.clean_existing()
    biXML.write(xml_out, io_map_file)
    biXML.dumpObjects(dump_out2)

import csv
import uuid

class IO:

    def __init__(self, io_map_file, io_common_file, io_existing_file):
        with open(io_map_file, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            self.io_map = {rows[0]:rows[1] for rows in reader}
        with open(io_common_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            self.commonInfoObjects = {rows[0] for rows in reader}
        with open(io_existing_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            self.existingObjects = {rows[0] for rows in reader}
        self.uuid_dic = {}
          
    def writeInfoObjectMap(self, outfile):    
        with open(outfile, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in self.io_map.items():
                writer.writerow([key, value])   
        
    def newName(self, name):
        if not name in self.commonInfoObjects:
            if name in self.io_map.keys():
                return self.io_map[name]
            else:
                newname = 'X' + name[1:]
                newname = newname[:9]
                self.io_map[name] = newname
        else:
            newname = name
        return newname
    
    def get_xmi_idref_uuid(self, xmi_idref):
        split = xmi_idref.split("::")
        if split[1] in self.uuid_dic:
            return split[0]+"::"+self.uuid_dic[split[1]]
        else:
            new_uuid = self.new_uuid(split[1])
            self.uuid_dic[split[1]] = new_uuid
            return split[0]+"::"+new_uuid

    def sav_xmi_idref_uuid(self, xmi_idref):
        split = xmi_idref.split("::")
        if not split[1] in self.uuid_dic:
            self.uuid_dic[split[1]] = split[1]
    
    def get_name_uuid(self, name):
        if name in self.uuid_dic:
            return self.uuid_dic[name]
        else:
            new_uuid = self.new_uuid(name)
            self.uuid_dic[name] = new_uuid
            return new_uuid

    def new_uuid(self, old_uuid):
        u = uuid.uuid1()
        s = str(u).split('-')
        nuid1 = s[4]+s[3]+s[2]
        nuid2 = s[1]+s[0]
        nuid = nuid1[:len(old_uuid)-12]+nuid2
        return nuid.upper()
            
    def newFieldname(self, name):
        return '/BIC/' + name
    def tableDataTimeDependent(self, name):
        return '/BIC/Q' + name
    def tableDataTimeIndependent(self, name):
        return '/BIC/P' + name
    def tableHierarchies(self, name):
        return '/BIC/H' + name
    def tableHierarchiesIntervals(self, name):
        return '/BIC/J' + name
    def tableTexts(self, name):
        return '/BIC/T' + name
    def viewOnDB(self, name):
        return '/BIC/M' + name
    def xmID(self, name):
        return 'com.sap.bw.cwm.core.InfoObject::' + name
    def substName(self, attrib):
        split = attrib.split("::")
        return split[0]+"::"+self.newName(split[1])
    def navAttributeNameReport(self, name):
        split = name.split("__")
        return self.newName(split[0])+"__"+self.newName(split[1])
    def originalSystem(self):
        return 'BHD'
    def owner(self):
        return ''
    def package(self):
        return '$TMP'       

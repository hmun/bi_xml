'''
   Copyright (C) 2019  Hermann Mundprecht hmun@thinkthinkdo.com

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

'''

import csv
import uuid

class DSO:

    def __init__(self):
        self.uuid_dic = {}

    def newName(self, name):
        newname = 'X' + name[1:]
        newname = newname[:9]
        return newname

    def get_xmi_idref_uuid(self, xmi_idref):
        split = xmi_idref.split("::")
        if split[1] in self.uuid_dic:
            return split[0]+"::"+self.uuid_dic[split[1]]
        else:
            new_uuid = self.new_uuid(split[1])
            self.uuid_dic[split[1]] = new_uuid
            return split[0]+"::"+new_uuid

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

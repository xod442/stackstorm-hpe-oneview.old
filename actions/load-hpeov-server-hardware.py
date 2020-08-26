# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import HpeOVBaseAction


class loadDb(HpeOVBaseAction):
    def run(self, servers):

        mydb = self.dbclient["app_db"]
        known = mydb["ovservers"]

        new_server={}

        for server in servers:
            myquery = { "_id" : server['created'] }
            records = known.find(myquery).count()
            if records == 0:
                new_server['vendor']='hpe-oneview'
                new_server['_id']=server['created']
                new_server['assetTag']=server['assetTag']
                new_server['eTag']=server['eTag']
                new_server['hostOsType']=server['hostOsType']
                new_server['memoryMb']=server['memoryMb']
                new_server['model']=server['model']
                new_server['firmWare']=server['mpFirmwareVersion']
                new_server['hostName']=server['mpHostInfo']['mpHostName']
                new_server['hostName']=server['mpHostInfo']['mpIpAddresses'][0]['address']
                new_server['mpModel']=server['mpModel']
                new_server['mpState']=server['mpState']
                new_server['status']=server['status']
                new_server['uuid']=server['uuid']
                new_server['serno']=server['virtualSerialNumber']
                write_record = known.insert_one(new_server)
                # write_record = process.insert_one(alarm)
        return (records)

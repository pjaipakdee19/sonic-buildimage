#!/usr/bin/env python

import os
import json
import struct
import subprocess
from sonic_daemon_base.daemon_base import DaemonBase
from mmap import *

# HOST_CHK_CMD = "docker > /dev/null 2>&1"
# EMPTY_STRING = ""

CONFIG_PATH = '/usr/share/sonic/device/{}/sonic_platform_config'

class Common:

    NULL_VAL = 'N/A'

    OPER_IMPI = 'ipmi'
    OPER_FIXED_LIST = 'fixed_list'
    OPER_FIXED = 'fixed'

    def __init__(self):
        (self.platform, self.hwsku) = DaemonBase().get_platform_and_hwsku()

    def get_config_path(self):
        return CONFIG_PATH.format(self.platform)

    def load_json_file(self, path):
        json_data = {}
        try:
            json_data = json.load(open(path))
        except IOError:
            pass
        return json_data

    def run_command(self, cmd):
        status = True
        result = ""
        try:
            p = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            raw_data, err = p.communicate()
            if err == '':
                result = raw_data.strip()
        except Exception as e:
            print(e)
            status = False
        return status, result

    # def is_host(self):
    #     return os.system(HOST_CHK_CMD) == 0

    # def pci_get_value(self, resource, offset):
    #     status = True
    #     result = ""
    #     try:
    #         fd = os.open(resource, os.O_RDWR)
    #         mm = mmap(fd, 0)
    #         mm.seek(int(offset))
    #         read_data_stream = mm.read(4)
    #         result = struct.unpack('I', read_data_stream)
    #     except:
    #         status = False
    #     return status, result



    # def run_interactive_command(self, cmd):
    #     try:
    #         os.system(cmd)
    #     except:
    #         return False
    #     return True

    # def read_txt_file(self, file_path):
    #     try:
    #         with open(file_path, 'r') as fd:
    #             data = fd.read()
    #             return data.strip()
    #     except IOError:
    #         pass
    #     return None

    # def read_one_line_file(self, file_path):
    #     try:
    #         with open(file_path, 'r') as fd:
    #             data = fd.readline()
    #             return data.strip()
    #     except IOError:
    #         pass
    #     return None

    # def ipmi_raw(self, netfn, cmd):
    #     status = True
    #     result = ""
    #     try:
    #         cmd = "ipmitool raw {} {}".format(str(netfn), str(cmd))
    #         p = subprocess.Popen(
    #             cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         raw_data, err = p.communicate()
    #         if err == '':
    #             result = raw_data.strip()
    #         else:
    #             status = False
    #     except:
    #         status = False
    #     return status, result

    # def ipmi_fru_id(self, id, key=None):
    #     status = True
    #     result = ""
    #     try:
    #         cmd = "ipmitool fru print {}".format(str(
    #             id)) if not key else "ipmitool fru print {0} | grep '{1}' ".format(str(id), str(key))

    #         p = subprocess.Popen(
    #             cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         raw_data, err = p.communicate()
    #         if err == '':
    #             result = raw_data.strip()
    #         else:
    #             status = False
    #     except:
    #         status = False
    #     return status, result

    # def ipmi_set_ss_thres(self, id, threshold_key, value):
    #     status = True
    #     result = ""
    #     try:
    #         cmd = "ipmitool sensor thresh '{}' {} {}".format(
    #             str(id), str(threshold_key), str(value))
    #         p = subprocess.Popen(
    #             cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         raw_data, err = p.communicate()
    #         if err == '':
    #             result = raw_data.strip()
    #         else:
    #             status = False
    #     except:
    #         status = False
    #     return status, result

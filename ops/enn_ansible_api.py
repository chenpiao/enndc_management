#!/usr/bin/env python
# coding:utf-8
__author__ = 'syx'

import ansible.runner
import json

def save_info(ip):
    ip1 = json.dumps(ip)
    ip2 = str(ip)
    runner = ansible.runner.Runner(
        host_list='/var/www/cmdb/enndc_management/ops/inventory',
        module_name='setup',
        module_args='',
        pattern=ip,
        forks=10,
        remote_user="sunyx",
        remote_pass="1qazxsw@",
	#remote_tmp='/tmp/.ansible/tmp',
	become=True,
	become_method="sudo",
	become_user="sunyx",
	become_pass="1qazxsw@",
        #become_exe='sudo'
    )
    data_structure = runner.run()  # ansible_facts
    #data = json.dumps(data_structure, indent=4)
    #info = json.loads(data)
    facts = data_structure['contacted'][ip]
    #facts = info['contacted'][ip]['ansible_facts']
    #hostname = facts['ansible_hostname']
    #OS = facts['ansible_distribution']
    #OsVersion = facts['ansible_distribution_version']
    #CPU = facts['ansible_processor_count']
    #mem = facts['ansible_memtotal_mb']
    # k = facts['contacted']
    print ip2,
    print '#########################'
    print json.dumps(facts, indent=4)
    #print facts
    #print hostname
    #print k
    #print json.dumps(facts, indent=4)
    #return hostname, OS


if __name__ == '__main__':
    aa = "127.0.0.1"
    save_info(aa)

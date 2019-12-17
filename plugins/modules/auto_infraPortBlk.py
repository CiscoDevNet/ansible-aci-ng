#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_infraPortBlk 
short_description: Manage Access Port Block (infra:PortBlk)
description:
- port block
notes:
- More information about the internal APIC class B(infra:PortBlk) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - configuration item description. 
  fromCard:
    description:
    - from module 
  fromPort:
    description:
    - port block from port 
  name:
    description:
    - port block name 
    aliases: [ access_port_block ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  toCard:
    description:
    - port block to module 
  toPort:
    description:
    - port block to port 
  leaf_interface_profile:
    description:
    - interface profile name 
  access_port_selector:
    description:
    - host port selector name 
  access_port_selector_type:
    description:
    - host port selector type 
    choices: [ ALL, range ] 
  state: 
    description:
    - Use C(present) or C(absent) for adding or removing.
    - Use C(query) for listing an object or multiple objects.
    choices: [ absent, present, query ]
    default: present 

extends_documentation_fragment: aci
'''

from ansible_collections.cisco.aci.plugins.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule

def main():
    argument_spec = aci_argument_spec()
    argument_spec.update({ 
        'annotation': dict(type='str',),
        'descr': dict(type='str',),
        'fromCard': dict(type='str',),
        'fromPort': dict(type='str',),
        'name': dict(type='str', aliases=['access_port_block']),
        'nameAlias': dict(type='str',),
        'toCard': dict(type='str',),
        'toPort': dict(type='str',),
        'leaf_interface_profile': dict(type='str',),
        'access_port_selector': dict(type='str',),
        'access_port_selector_type': dict(type='str', choices=['ALL', 'range'], ),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_infra_rs_acc_bndl_subgrp': dict(type='str'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'leaf_interface_profile', 'access_port_selector', 'access_port_selector_type', ]], 
            ['state', 'present', ['name', 'leaf_interface_profile', 'access_port_selector', 'access_port_selector_type', ]],
        ],
    )
    
    annotation = module.params['annotation']
    descr = module.params['descr']
    fromCard = module.params['fromCard']
    fromPort = module.params['fromPort']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    toCard = module.params['toCard']
    toPort = module.params['toPort']
    leaf_interface_profile = module.params['leaf_interface_profile']
    access_port_selector = module.params['access_port_selector']
    access_port_selector_type = module.params['access_port_selector_type']
    state = module.params['state']
    child_configs=[]
    
    relation_infrarsaccbndlsubgrp = module.params['relation_infra_rs_acc_bndl_subgrp']
    if relation_infrarsaccbndlsubgrp:
        child_configs.append({'infraRsAccBndlSubgrp': {'attributes': {'tnInfraAccBndlSubgrpName': relation_infrarsaccbndlsubgrp}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'infraAccPortP',
            'aci_rn': 'infra/accportprof-{}'.format(leaf_interface_profile),
            'target_filter': 'eq(infraAccPortP.name, "{}")'.format(leaf_interface_profile),
            'module_object': leaf_interface_profile
        }, 
        subclass_1={
            'aci_class': 'infraHPortS',
            'aci_rn': 'hports-{}-typ-{}'.format(access_port_selector, access_port_selector_type),
            'target_filter': 'and(eq(infraHPortS.name, "{}"),eq(infraHPortS.type, "{}"))'.format(access_port_selector, access_port_selector_type),
            'module_object': access_port_selector
        }, 
        subclass_2={
            'aci_class': 'infraPortBlk',
            'aci_rn': 'portblk-{}'.format(name),
            'target_filter': 'eq(infraPortBlk.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['infraRsAccBndlSubgrp']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='infraPortBlk',
            class_config={ 
                'annotation': annotation,
                'descr': descr,
                'fromCard': fromCard,
                'fromPort': fromPort,
                'name': name,
                'nameAlias': nameAlias,
                'toCard': toCard,
                'toPort': toPort,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='infraPortBlk')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
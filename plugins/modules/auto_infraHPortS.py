#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_infraHPortS 
short_description: Manage Access Port Selector (infra:HPortS)
description:
- used to specify which ports to be configured and how
notes:
- More information about the internal APIC class B(infra:HPortS) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - policy definition 
  name:
    description:
    - host port selector name 
    aliases: [ access_port_selector ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
  access_port_selector_type:
    description:
    - host port selector type 
    choices: [ ALL, range ] 
  leaf_interface_profile:
    description:
    - interface profile name 
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
        'name': dict(type='str', aliases=['access_port_selector']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'access_port_selector_type': dict(type='str', choices=['ALL', 'range'], ),
        'leaf_interface_profile': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_infra_rs_acc_base_grp': dict(type='str'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'access_port_selector_type', 'leaf_interface_profile', ]], 
            ['state', 'present', ['name', 'access_port_selector_type', 'leaf_interface_profile', ]],
        ],
    )
    
    annotation = module.params['annotation']
    descr = module.params['descr']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    access_port_selector_type = module.params['access_port_selector_type']
    leaf_interface_profile = module.params['leaf_interface_profile']
    state = module.params['state']
    child_configs=[]
    
    relation_infrarsaccbasegrp = module.params['relation_infra_rs_acc_base_grp']
    if relation_infrarsaccbasegrp:
        child_configs.append({'infraRsAccBaseGrp': {'attributes': {'tnInfraAccBaseGrpName': relation_infrarsaccbasegrp}}})
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
            'aci_rn': 'hports-{}-typ-{}'.format(name, access_port_selector_type),
            'target_filter': 'and(eq(infraHPortS.name, "{}"),eq(infraHPortS.type, "{}"))'.format(name, access_port_selector_type),
            'module_object': name
        }, 
        
        child_classes=['infraRsAccBaseGrp']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='infraHPortS',
            class_config={ 
                'annotation': annotation,
                'descr': descr,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='infraHPortS')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
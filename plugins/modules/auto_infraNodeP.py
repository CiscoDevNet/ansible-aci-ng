#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_infraNodeP 
short_description: Manage Leaf Profile (infra:NodeP)
description:
- node profile
notes:
- More information about the internal APIC class B(infra:NodeP) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - node policy description 
  name:
    description:
    - node policy name 
    aliases: [ leaf_profile ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
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
        'name': dict(type='str', aliases=['leaf_profile']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_infra_rs_acc_card_p': dict(type='list'),

        'relation_infra_rs_acc_port_p': dict(type='list'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', ]], 
            ['state', 'present', ['name', ]],
        ],
    )
    
    annotation = module.params['annotation']
    descr = module.params['descr']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    state = module.params['state']
    child_configs=[]
    
    relation_infrarsacccardp = module.params['relation_infra_rs_acc_card_p']
    relation_infrarsaccportp = module.params['relation_infra_rs_acc_port_p']

    if relation_infrarsacccardp:
        for relation_param in relation_infrarsacccardp:
            child_configs.append({'infraRsAccCardP': {'attributes': {'tDn': relation_param}}})

    if relation_infrarsaccportp:
        for relation_param in relation_infrarsaccportp:
            child_configs.append({'infraRsAccPortP': {'attributes': {'tDn': relation_param}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'infraNodeP',
            'aci_rn': 'infra/nprof-{}'.format(name),
            'target_filter': 'eq(infraNodeP.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['infraRsAccCardP','infraRsAccPortP']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='infraNodeP',
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

        aci.get_diff(aci_class='infraNodeP')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
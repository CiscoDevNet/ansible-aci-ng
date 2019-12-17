#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_infraAttEntityP 
short_description: Manage Attachable Access Entity Profile (infra:AttEntityP)
description:
- attached entity profile
notes:
- More information about the internal APIC class B(infra:AttEntityP) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - attached entity profile description 
  name:
    description:
    - attached entity profile name 
    aliases: [ attachable_access_entity_profile ] 
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
        'name': dict(type='str', aliases=['attachable_access_entity_profile']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_infra_rs_dom_p': dict(type='list'),

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
    
    relation_infrarsdomp = module.params['relation_infra_rs_dom_p']

    if relation_infrarsdomp:
        for relation_param in relation_infrarsdomp:
            child_configs.append({'infraRsDomP': {'attributes': {'tDn': relation_param}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'infraAttEntityP',
            'aci_rn': 'infra/attentp-{}'.format(name),
            'target_filter': 'eq(infraAttEntityP.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['infraRsDomP']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='infraAttEntityP',
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

        aci.get_diff(aci_class='infraAttEntityP')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
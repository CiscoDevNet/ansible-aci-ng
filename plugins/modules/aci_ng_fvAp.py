#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvAp 
short_description: Manage Application Profile (fv:Ap)
description:
- application profile
notes:
- More information about the internal APIC class B(fv:Ap) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - definition root description 
  name:
    description:
    - application profile name 
    aliases: [ application_profile ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
  prio:
    description:
    - priority class id 
    choices: [ level1, level2, level3, level4, level5, level6, unspecified ] 
  tenant:
    description:
    - tenant name 
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
        'name': dict(type='str', aliases=['application_profile']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'prio': dict(type='str', choices=['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'unspecified'], ),
        'tenant': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_ap_mon_pol': dict(type='str'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'tenant', ]], 
            ['state', 'present', ['name', 'tenant', ]],
        ],
    )
    
    annotation = module.params['annotation']
    descr = module.params['descr']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    prio = module.params['prio']
    tenant = module.params['tenant']
    state = module.params['state']
    child_configs=[]
    
    relation_fvrsapmonpol = module.params['relation_fv_rs_ap_mon_pol']
    if relation_fvrsapmonpol:
        child_configs.append({'fvRsApMonPol': {'attributes': {'tnMonEPGPolName': relation_fvrsapmonpol}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant,
        }, 
        subclass_1={
            'aci_class': 'fvAp',
            'aci_rn': 'ap-{}'.format(name),
            'target_filter': 'eq(fvAp.name, "{}")'.format(name),
            'module_object': name,
        }, 
        
        child_classes=['fvRsApMonPol']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvAp',
            class_config={ 
                'annotation': annotation,
                'descr': descr,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
                'prio': prio,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvAp')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
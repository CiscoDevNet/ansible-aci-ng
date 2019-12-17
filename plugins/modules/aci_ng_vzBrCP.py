#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_vzBrCP 
short_description: Manage Contract (vz:BrCP)
description:
- binary contract
notes:
- More information about the internal APIC class B(vz:BrCP) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - description of this managed object 
  name:
    description:
    - name of this managed object 
    aliases: [ contract ] 
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
    - priority level of the service contract 
    choices: [ level1, level2, level3, level4, level5, level6, unspecified ] 
  scope:
    description:
    - scope of contract 
    choices: [ application-profile, context, global, tenant ] 
  targetDscp:
    description:
    - target dscp 
    choices: [ AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, CS0, CS1, CS2, CS3, CS4, CS5, CS6, CS7, EF, VA, unspecified ] 
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
        'name': dict(type='str', aliases=['contract']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'prio': dict(type='str', choices=['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'unspecified'], ),
        'scope': dict(type='str', choices=['application-profile', 'context', 'global', 'tenant'], ),
        'targetDscp': dict(type='str', choices=['AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'EF', 'VA', 'unspecified'], ),
        'tenant': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_vz_rs_graph_att': dict(type='str'),

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
    scope = module.params['scope']
    targetDscp = module.params['targetDscp']
    tenant = module.params['tenant']
    state = module.params['state']
    child_configs=[]
    
    relation_vzrsgraphatt = module.params['relation_vz_rs_graph_att']
    if relation_vzrsgraphatt:
        child_configs.append({'vzRsGraphAtt': {'attributes': {'tnVnsAbsGraphName': relation_vzrsgraphatt}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant
        }, 
        subclass_1={
            'aci_class': 'vzBrCP',
            'aci_rn': 'brc-{}'.format(name),
            'target_filter': 'eq(vzBrCP.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['vzRsGraphAtt']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='vzBrCP',
            class_config={ 
                'annotation': annotation,
                'descr': descr,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
                'prio': prio,
                'scope': scope,
                'targetDscp': targetDscp,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='vzBrCP')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
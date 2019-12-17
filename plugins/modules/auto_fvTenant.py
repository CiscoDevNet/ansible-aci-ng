#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvTenant 
short_description: Manage Tenant (fv:Tenant)
description:
- policy owner in the virtual fabric
notes:
- More information about the internal APIC class B(fv:Tenant) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Maxwell Lin-He (@maxyso)
version_added: '2.7'
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - description of this managed object 
  name:
    description:
    - tenant name 
    aliases: [ tenant ] 
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
        'name': dict(type='str', aliases=['tenant']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_tn_deny_rule': dict(type='list'),

        'relation_fv_rs_tenant_mon_pol': dict(type='str'),

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
    
    relation_fvrstndenyrule = module.params['relation_fv_rs_tn_deny_rule']
    relation_fvrstenantmonpol = module.params['relation_fv_rs_tenant_mon_pol']

    if relation_fvrstndenyrule:
        for relation_param in relation_fvrstndenyrule:
            child_configs.append({'fvRsTnDenyRule': {'attributes': {'tDn': relation_param}}})
    if relation_fvrstenantmonpol:
        child_configs.append({'fvRsTenantMonPol': {'attributes': {'tnMonEPGPolName': relation_fvrstenantmonpol}}})

    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(name),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(name),
            'module_object': '',
        }, 
        
        child_classes=['fvRsTnDenyRule','fvRsTenantMonPol']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvTenant',
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

        aci.get_diff(aci_class='fvTenant')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
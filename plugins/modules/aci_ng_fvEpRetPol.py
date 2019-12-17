#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvEpRetPol 
short_description: Manage End Point Retention Policy (fv:EpRetPol)
description:
- endpoint retention policy
notes:
- More information about the internal APIC class B(fv:EpRetPol) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  bounceAgeIntvl:
    description:
    - aging interval for endpoint migration 
    choices: [ infinite ] 
  bounceTrig:
    description:
    - bounce trigger 
    choices: [ protocol, rarp-flood ] 
  descr:
    description:
    - policy definition description 
  holdIntvl:
    description:
    - hold interval 
  localEpAgeIntvl:
    description:
    - local endpoint aging interval 
    choices: [ infinite ] 
  moveFreq:
    description:
    - move frequency 
    choices: [ none ] 
  name:
    description:
    - retention policy name 
    aliases: [ end_point_retention_policy ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
  remoteEpAgeIntvl:
    description:
    - remote endpoint aging interval 
    choices: [ infinite ] 
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
        'bounceAgeIntvl': dict(type='str', choices=['infinite'], ),
        'bounceTrig': dict(type='str', choices=['protocol', 'rarp-flood'], ),
        'descr': dict(type='str',),
        'holdIntvl': dict(type='str',),
        'localEpAgeIntvl': dict(type='str', choices=['infinite'], ),
        'moveFreq': dict(type='str', choices=['none'], ),
        'name': dict(type='str', aliases=['end_point_retention_policy']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'remoteEpAgeIntvl': dict(type='str', choices=['infinite'], ),
        'tenant': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

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
    bounceAgeIntvl = module.params['bounceAgeIntvl']
    bounceTrig = module.params['bounceTrig']
    descr = module.params['descr']
    holdIntvl = module.params['holdIntvl']
    localEpAgeIntvl = module.params['localEpAgeIntvl']
    moveFreq = module.params['moveFreq']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    remoteEpAgeIntvl = module.params['remoteEpAgeIntvl']
    tenant = module.params['tenant']
    state = module.params['state']
    child_configs=[]
    
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant
        }, 
        subclass_1={
            'aci_class': 'fvEpRetPol',
            'aci_rn': 'epRPol-{}'.format(name),
            'target_filter': 'eq(fvEpRetPol.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=[]
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvEpRetPol',
            class_config={ 
                'annotation': annotation,
                'bounceAgeIntvl': bounceAgeIntvl,
                'bounceTrig': bounceTrig,
                'descr': descr,
                'holdIntvl': holdIntvl,
                'localEpAgeIntvl': localEpAgeIntvl,
                'moveFreq': moveFreq,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
                'remoteEpAgeIntvl': remoteEpAgeIntvl,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvEpRetPol')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
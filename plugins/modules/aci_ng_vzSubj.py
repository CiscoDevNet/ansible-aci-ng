#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_vzSubj 
short_description: Manage Contract Subject (vz:Subj)
description:
- subject
notes:
- More information about the internal APIC class B(vz:Subj) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  consMatchT:
    description:
    - consumer subject match criteria 
    choices: [ All, AtleastOne, AtmostOne, None ] 
  descr:
    description:
    - description of this managed object 
  name:
    description:
    - name of this managed object 
    aliases: [ contract_subject ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  prio:
    description:
    - priority level specifier 
    choices: [ level1, level2, level3, level4, level5, level6, unspecified ] 
  provMatchT:
    description:
    - consumer subject match criteria 
    choices: [ All, AtleastOne, AtmostOne, None ] 
  revFltPorts:
    description:
    - enables filter to apply on ingress and egress traffic 
    choices: [ no, yes ] 
  targetDscp:
    description:
    - target dscp 
    choices: [ AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, CS0, CS1, CS2, CS3, CS4, CS5, CS6, CS7, EF, VA, unspecified ] 
  tenant:
    description:
    - tenant name 
  contract:
    description:
    - name of this managed object 
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
        'consMatchT': dict(type='str', choices=['All', 'AtleastOne', 'AtmostOne', 'None'], ),
        'descr': dict(type='str',),
        'name': dict(type='str', aliases=['contract_subject']),
        'nameAlias': dict(type='str',),
        'prio': dict(type='str', choices=['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'unspecified'], ),
        'provMatchT': dict(type='str', choices=['All', 'AtleastOne', 'AtmostOne', 'None'], ),
        'revFltPorts': dict(type='str', choices=['no', 'yes'], ),
        'targetDscp': dict(type='str', choices=['AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'EF', 'VA', 'unspecified'], ),
        'tenant': dict(type='str',),
        'contract': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_vz_rs_subj_graph_att': dict(type='str'),

        'relation_vz_rs_subj_filt_att': dict(type='list'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'tenant', 'contract', ]], 
            ['state', 'present', ['name', 'tenant', 'contract', ]],
        ],
    )
    
    annotation = module.params['annotation']
    consMatchT = module.params['consMatchT']
    descr = module.params['descr']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    prio = module.params['prio']
    provMatchT = module.params['provMatchT']
    revFltPorts = module.params['revFltPorts']
    targetDscp = module.params['targetDscp']
    tenant = module.params['tenant']
    contract = module.params['contract']
    state = module.params['state']
    child_configs=[]
    
    relation_vzrssubjgraphatt = module.params['relation_vz_rs_subj_graph_att']
    relation_vzrssubjfiltatt = module.params['relation_vz_rs_subj_filt_att']
    if relation_vzrssubjgraphatt:
        child_configs.append({'vzRsSubjGraphAtt': {'attributes': {'tnVnsAbsGraphName': relation_vzrssubjgraphatt}}})

    if relation_vzrssubjfiltatt:
        for relation_param in relation_vzrssubjfiltatt:
            child_configs.append({'vzRsSubjFiltAtt': {'attributes': {'tnVzFilterName': relation_param}}})
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
            'aci_rn': 'brc-{}'.format(contract),
            'target_filter': 'eq(vzBrCP.name, "{}")'.format(contract),
            'module_object': contract
        }, 
        subclass_2={
            'aci_class': 'vzSubj',
            'aci_rn': 'subj-{}'.format(name),
            'target_filter': 'eq(vzSubj.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['vzRsSubjGraphAtt','vzRsSubjFiltAtt']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='vzSubj',
            class_config={ 
                'annotation': annotation,
                'consMatchT': consMatchT,
                'descr': descr,
                'name': name,
                'nameAlias': nameAlias,
                'prio': prio,
                'provMatchT': provMatchT,
                'revFltPorts': revFltPorts,
                'targetDscp': targetDscp,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='vzSubj')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
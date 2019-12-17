#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvCtx 
short_description: Manage VRF (fv:Ctx)
description:
- private layer 3 network context
notes:
- More information about the internal APIC class B(fv:Ctx) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  bdEnforcedEnable:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  descr:
    description:
    - definition root description 
  ipDataPlaneLearning:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ disabled, enabled ] 
  knwMcastAct:
    description:
    - specifies if known multicast traffic is forwarded 
    choices: [ deny, permit ] 
  name:
    description:
    - network context name 
    aliases: [ vrf ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
  pcEnfDir:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ egress, ingress ] 
  pcEnfPref:
    description:
    - preferred policy control 
    choices: [ enforced, unenforced ] 
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
        'bdEnforcedEnable': dict(type='str', choices=['no', 'yes'], ),
        'descr': dict(type='str',),
        'ipDataPlaneLearning': dict(type='str', choices=['disabled', 'enabled'], ),
        'knwMcastAct': dict(type='str', choices=['deny', 'permit'], ),
        'name': dict(type='str', aliases=['vrf']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'pcEnfDir': dict(type='str', choices=['egress', 'ingress'], ),
        'pcEnfPref': dict(type='str', choices=['enforced', 'unenforced'], ),
        'tenant': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_ospf_ctx_pol': dict(type='str'),

        'relation_fv_rs_vrf_validation_pol': dict(type='str'),

        'relation_fv_rs_ctx_mcast_to': dict(type='list'),

        'relation_fv_rs_ctx_to_eigrp_ctx_af_pol': dict(type='list'),

        'relation_fv_rs_ctx_to_ospf_ctx_pol': dict(type='list'),

        'relation_fv_rs_ctx_to_ep_ret': dict(type='str'),

        'relation_fv_rs_bgp_ctx_pol': dict(type='str'),

        'relation_fv_rs_ctx_mon_pol': dict(type='str'),

        'relation_fv_rs_ctx_to_ext_route_tag_pol': dict(type='str'),

        'relation_fv_rs_ctx_to_bgp_ctx_af_pol': dict(type='list'),

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
    bdEnforcedEnable = module.params['bdEnforcedEnable']
    descr = module.params['descr']
    ipDataPlaneLearning = module.params['ipDataPlaneLearning']
    knwMcastAct = module.params['knwMcastAct']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    pcEnfDir = module.params['pcEnfDir']
    pcEnfPref = module.params['pcEnfPref']
    tenant = module.params['tenant']
    state = module.params['state']
    child_configs=[]
    
    relation_fvrsospfctxpol = module.params['relation_fv_rs_ospf_ctx_pol']
    relation_fvrsvrfvalidationpol = module.params['relation_fv_rs_vrf_validation_pol']
    relation_fvrsctxmcastto = module.params['relation_fv_rs_ctx_mcast_to']
    relation_fvrsctxtoeigrpctxafpol = module.params['relation_fv_rs_ctx_to_eigrp_ctx_af_pol']
    relation_fvrsctxtoospfctxpol = module.params['relation_fv_rs_ctx_to_ospf_ctx_pol']
    relation_fvrsctxtoepret = module.params['relation_fv_rs_ctx_to_ep_ret']
    relation_fvrsbgpctxpol = module.params['relation_fv_rs_bgp_ctx_pol']
    relation_fvrsctxmonpol = module.params['relation_fv_rs_ctx_mon_pol']
    relation_fvrsctxtoextroutetagpol = module.params['relation_fv_rs_ctx_to_ext_route_tag_pol']
    relation_fvrsctxtobgpctxafpol = module.params['relation_fv_rs_ctx_to_bgp_ctx_af_pol']
    if relation_fvrsospfctxpol:
        child_configs.append({'fvRsOspfCtxPol': {'attributes': {'tnOspfCtxPolName': relation_fvrsospfctxpol}}})
    if relation_fvrsvrfvalidationpol:
        child_configs.append({'fvRsVrfValidationPol': {'attributes': {'tnL3extVrfValidationPolName': relation_fvrsvrfvalidationpol}}})

    if relation_fvrsctxmcastto:
        for relation_param in relation_fvrsctxmcastto:
            child_configs.append({'fvRsCtxMcastTo': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsctxtoeigrpctxafpol:
        for relation_param in relation_fvrsctxtoeigrpctxafpol:
            child_configs.append({'fvRsCtxToEigrpCtxAfPol':{'attributes': { 'tnEigrpCtxAfPolName': relation_param['tnEigrpCtxAfPolName'] , 'af': relation_param['af']  }}})

    if relation_fvrsctxtoospfctxpol:
        for relation_param in relation_fvrsctxtoospfctxpol:
            child_configs.append({'fvRsCtxToOspfCtxPol':{'attributes': { 'tnOspfCtxPolName': relation_param['tnOspfCtxPolName'] , 'af': relation_param['af']  }}})
    if relation_fvrsctxtoepret:
        child_configs.append({'fvRsCtxToEpRet': {'attributes': {'tnFvEpRetPolName': relation_fvrsctxtoepret}}})
    if relation_fvrsbgpctxpol:
        child_configs.append({'fvRsBgpCtxPol': {'attributes': {'tnBgpCtxPolName': relation_fvrsbgpctxpol}}})
    if relation_fvrsctxmonpol:
        child_configs.append({'fvRsCtxMonPol': {'attributes': {'tnMonEPGPolName': relation_fvrsctxmonpol}}})
    if relation_fvrsctxtoextroutetagpol:
        child_configs.append({'fvRsCtxToExtRouteTagPol': {'attributes': {'tnL3extRouteTagPolName': relation_fvrsctxtoextroutetagpol}}})

    if relation_fvrsctxtobgpctxafpol:
        for relation_param in relation_fvrsctxtobgpctxafpol:
            child_configs.append({'fvRsCtxToBgpCtxAfPol':{'attributes': { 'tnBgpCtxAfPolName': relation_param['tnBgpCtxAfPolName'] , 'af': relation_param['af']  }}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant
        }, 
        subclass_1={
            'aci_class': 'fvCtx',
            'aci_rn': 'ctx-{}'.format(name),
            'target_filter': 'eq(fvCtx.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['fvRsOspfCtxPol','fvRsVrfValidationPol','fvRsCtxMcastTo','fvRsCtxToEigrpCtxAfPol','fvRsCtxToOspfCtxPol','fvRsCtxToEpRet','fvRsBgpCtxPol','fvRsCtxMonPol','fvRsCtxToExtRouteTagPol','fvRsCtxToBgpCtxAfPol']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvCtx',
            class_config={ 
                'annotation': annotation,
                'bdEnforcedEnable': bdEnforcedEnable,
                'descr': descr,
                'ipDataPlaneLearning': ipDataPlaneLearning,
                'knwMcastAct': knwMcastAct,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
                'pcEnfDir': pcEnfDir,
                'pcEnfPref': pcEnfPref,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvCtx')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
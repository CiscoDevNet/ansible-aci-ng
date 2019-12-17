#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvBD 
short_description: Manage Bridge Domain (fv:BD)
description:
- bridge domain
notes:
- More information about the internal APIC class B(fv:BD) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  OptimizeWanBandwidth:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  arpFlood:
    description:
    - arp flood enable 
    choices: [ no, yes ] 
  descr:
    description:
    - definition root description 
  epClear:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  epMoveDetectMode:
    description:
    - ep move detection garp based mode 
    choices: [ garp ] 
  hostBasedRouting:
    description:
    - enables advertising host routes out of l3outs of this BD 
    choices: [ no, yes ] 
  intersiteBumTrafficAllow:
    description:
    -  
    choices: [ no, yes ] 
  intersiteL2Stretch:
    description:
    -  
    choices: [ no, yes ] 
  ipLearning:
    description:
    - Endpoint Dataplane Learning 
    choices: [ no, yes ] 
  ipv6McastAllow:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  limitIpLearnToSubnets:
    description:
    - limits ip learning to bd subnets only 
    choices: [ no, yes ] 
  llAddr:
    description:
    - override of system generated ipv6 link-local address 
  mac:
    description:
    - mac address 
  mcastAllow:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  multiDstPktAct:
    description:
    - forwarding method for multi destinations 
    choices: [ bd-flood, drop, encap-flood ] 
  name:
    description:
    - bridge domain name 
    aliases: [ bridge_domain ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  ownerKey:
    description:
    - key for enabling clients to own their data 
  ownerTag:
    description:
    - tag for enabling clients to add their own data 
  type:
    description:
    - component type 
    choices: [ fc, regular ] 
  unicastRoute:
    description:
    - Unicast routing 
    choices: [ no, yes ] 
  unkMacUcastAct:
    description:
    - forwarding method for l2 destinations 
    choices: [ flood, proxy ] 
  unkMcastAct:
    description:
    - parameter used by node to forward data 
    choices: [ flood, opt-flood ] 
  v6unkMcastAct:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ flood, opt-flood ] 
  vmac:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ not-applicable ] 
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
        'OptimizeWanBandwidth': dict(type='str', choices=['no', 'yes'], ),
        'annotation': dict(type='str',),
        'arpFlood': dict(type='str', choices=['no', 'yes'], ),
        'descr': dict(type='str',),
        'epClear': dict(type='str', choices=['no', 'yes'], ),
        'epMoveDetectMode': dict(type='str', choices=['garp'], ),
        'hostBasedRouting': dict(type='str', choices=['no', 'yes'], ),
        'intersiteBumTrafficAllow': dict(type='str', choices=['no', 'yes'], ),
        'intersiteL2Stretch': dict(type='str', choices=['no', 'yes'], ),
        'ipLearning': dict(type='str', choices=['no', 'yes'], ),
        'ipv6McastAllow': dict(type='str', choices=['no', 'yes'], ),
        'limitIpLearnToSubnets': dict(type='str', choices=['no', 'yes'], ),
        'llAddr': dict(type='str',),
        'mac': dict(type='str',),
        'mcastAllow': dict(type='str', choices=['no', 'yes'], ),
        'multiDstPktAct': dict(type='str', choices=['bd-flood', 'drop', 'encap-flood'], ),
        'name': dict(type='str', aliases=['bridge_domain']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'type': dict(type='str', choices=['fc', 'regular'], ),
        'unicastRoute': dict(type='str', choices=['no', 'yes'], ),
        'unkMacUcastAct': dict(type='str', choices=['flood', 'proxy'], ),
        'unkMcastAct': dict(type='str', choices=['flood', 'opt-flood'], ),
        'v6unkMcastAct': dict(type='str', choices=['flood', 'opt-flood'], ),
        'vmac': dict(type='str', choices=['not-applicable'], ),
        'tenant': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_bd_to_profile': dict(type='str'),

        'relation_fv_rs_abd_pol_mon_pol': dict(type='str'),

        'relation_fv_rs_bd_to_nd_p': dict(type='str'),

        'relation_fv_rs_bd_flood_to': dict(type='list'),

        'relation_fv_rs_bd_to_fhs': dict(type='str'),

        'relation_fv_rs_bd_to_relay_p': dict(type='str'),

        'relation_fv_rs_ctx': dict(type='str'),

        'relation_fv_rs_bd_to_netflow_monitor_pol': dict(type='list'),

        'relation_fv_rs_igmpsn': dict(type='str'),

        'relation_fv_rs_bd_to_ep_ret': dict(type='str'),

        'relation_fv_rs_bd_to_out': dict(type='list'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'tenant', ]], 
            ['state', 'present', ['name', 'tenant', ]],
        ],
    )
    
    OptimizeWanBandwidth = module.params['OptimizeWanBandwidth']
    annotation = module.params['annotation']
    arpFlood = module.params['arpFlood']
    descr = module.params['descr']
    epClear = module.params['epClear']
    epMoveDetectMode = module.params['epMoveDetectMode']
    hostBasedRouting = module.params['hostBasedRouting']
    intersiteBumTrafficAllow = module.params['intersiteBumTrafficAllow']
    intersiteL2Stretch = module.params['intersiteL2Stretch']
    ipLearning = module.params['ipLearning']
    ipv6McastAllow = module.params['ipv6McastAllow']
    limitIpLearnToSubnets = module.params['limitIpLearnToSubnets']
    llAddr = module.params['llAddr']
    mac = module.params['mac']
    mcastAllow = module.params['mcastAllow']
    multiDstPktAct = module.params['multiDstPktAct']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    ownerKey = module.params['ownerKey']
    ownerTag = module.params['ownerTag']
    type = module.params['type']
    unicastRoute = module.params['unicastRoute']
    unkMacUcastAct = module.params['unkMacUcastAct']
    unkMcastAct = module.params['unkMcastAct']
    v6unkMcastAct = module.params['v6unkMcastAct']
    vmac = module.params['vmac']
    tenant = module.params['tenant']
    state = module.params['state']
    child_configs=[]
    
    relation_fvrsbdtoprofile = module.params['relation_fv_rs_bd_to_profile']
    relation_fvrsabdpolmonpol = module.params['relation_fv_rs_abd_pol_mon_pol']
    relation_fvrsbdtondp = module.params['relation_fv_rs_bd_to_nd_p']
    relation_fvrsbdfloodto = module.params['relation_fv_rs_bd_flood_to']
    relation_fvrsbdtofhs = module.params['relation_fv_rs_bd_to_fhs']
    relation_fvrsbdtorelayp = module.params['relation_fv_rs_bd_to_relay_p']
    relation_fvrsctx = module.params['relation_fv_rs_ctx']
    relation_fvrsbdtonetflowmonitorpol = module.params['relation_fv_rs_bd_to_netflow_monitor_pol']
    relation_fvrsigmpsn = module.params['relation_fv_rs_igmpsn']
    relation_fvrsbdtoepret = module.params['relation_fv_rs_bd_to_ep_ret']
    relation_fvrsbdtoout = module.params['relation_fv_rs_bd_to_out']
    if relation_fvrsbdtoprofile:
        child_configs.append({'fvRsBDToProfile': {'attributes': {'tnRtctrlProfileName': relation_fvrsbdtoprofile}}})
    if relation_fvrsabdpolmonpol:
        child_configs.append({'fvRsABDPolMonPol': {'attributes': {'tnMonEPGPolName': relation_fvrsabdpolmonpol}}})
    if relation_fvrsbdtondp:
        child_configs.append({'fvRsBDToNdP': {'attributes': {'tnNdIfPolName': relation_fvrsbdtondp}}})

    if relation_fvrsbdfloodto:
        for relation_param in relation_fvrsbdfloodto:
            child_configs.append({'fvRsBdFloodTo': {'attributes': {'tDn': relation_param}}})
    if relation_fvrsbdtofhs:
        child_configs.append({'fvRsBDToFhs': {'attributes': {'tnFhsBDPolName': relation_fvrsbdtofhs}}})
    if relation_fvrsbdtorelayp:
        child_configs.append({'fvRsBDToRelayP': {'attributes': {'tnDhcpRelayPName': relation_fvrsbdtorelayp}}})
    if relation_fvrsctx:
        child_configs.append({'fvRsCtx': {'attributes': {'tnFvCtxName': relation_fvrsctx}}})

    if relation_fvrsbdtonetflowmonitorpol:
        for relation_param in relation_fvrsbdtonetflowmonitorpol:
            child_configs.append({'fvRsBDToNetflowMonitorPol':{'attributes': { 'tnNetflowMonitorPolName': relation_param['tnNetflowMonitorPolName'] , 'fltType': relation_param['fltType']  }}})
    if relation_fvrsigmpsn:
        child_configs.append({'fvRsIgmpsn': {'attributes': {'tnIgmpSnoopPolName': relation_fvrsigmpsn}}})
    if relation_fvrsbdtoepret:
        child_configs.append({'fvRsBdToEpRet': {'attributes': {'tnFvEpRetPolName': relation_fvrsbdtoepret}}})

    if relation_fvrsbdtoout:
        for relation_param in relation_fvrsbdtoout:
            child_configs.append({'fvRsBDToOut': {'attributes': {'tnL3extOutName': relation_param}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant
        }, 
        subclass_1={
            'aci_class': 'fvBD',
            'aci_rn': 'BD-{}'.format(name),
            'target_filter': 'eq(fvBD.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['fvRsBDToProfile','fvRsABDPolMonPol','fvRsBDToNdP','fvRsBdFloodTo','fvRsBDToFhs','fvRsBDToRelayP','fvRsCtx','fvRsBDToNetflowMonitorPol','fvRsIgmpsn','fvRsBdToEpRet','fvRsBDToOut']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvBD',
            class_config={ 
                'OptimizeWanBandwidth': OptimizeWanBandwidth,
                'annotation': annotation,
                'arpFlood': arpFlood,
                'descr': descr,
                'epClear': epClear,
                'epMoveDetectMode': epMoveDetectMode,
                'hostBasedRouting': hostBasedRouting,
                'intersiteBumTrafficAllow': intersiteBumTrafficAllow,
                'intersiteL2Stretch': intersiteL2Stretch,
                'ipLearning': ipLearning,
                'ipv6McastAllow': ipv6McastAllow,
                'limitIpLearnToSubnets': limitIpLearnToSubnets,
                'llAddr': llAddr,
                'mac': mac,
                'mcastAllow': mcastAllow,
                'multiDstPktAct': multiDstPktAct,
                'name': name,
                'nameAlias': nameAlias,
                'ownerKey': ownerKey,
                'ownerTag': ownerTag,
                'type': type,
                'unicastRoute': unicastRoute,
                'unkMacUcastAct': unkMacUcastAct,
                'unkMcastAct': unkMcastAct,
                'v6unkMcastAct': v6unkMcastAct,
                'vmac': vmac,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvBD')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_infraAccPortGrp 
short_description: Manage Leaf Access Port Policy Group (infra:AccPortGrp)
description:
- singular ports
notes:
- More information about the internal APIC class B(infra:AccPortGrp) from
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
    - singular ports name 
    aliases: [ leaf_access_port_policy_group ] 
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
        'name': dict(type='str', aliases=['leaf_access_port_policy_group']),
        'nameAlias': dict(type='str',),
        'ownerKey': dict(type='str',),
        'ownerTag': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_infra_rs_span_v_src_grp': dict(type='list'),

        'relation_infra_rs_stormctrl_if_pol': dict(type='str'),

        'relation_infra_rs_poe_if_pol': dict(type='str'),

        'relation_infra_rs_lldp_if_pol': dict(type='str'),

        'relation_infra_rs_macsec_if_pol': dict(type='str'),

        'relation_infra_rs_qos_dpp_if_pol': dict(type='str'),

        'relation_infra_rs_h_if_pol': dict(type='str'),

        'relation_infra_rs_netflow_monitor_pol': dict(type='list'),

        'relation_infra_rs_l2_port_auth_pol': dict(type='str'),

        'relation_infra_rs_mcp_if_pol': dict(type='str'),

        'relation_infra_rs_l2_port_security_pol': dict(type='str'),

        'relation_infra_rs_copp_if_pol': dict(type='str'),

        'relation_infra_rs_span_v_dest_grp': dict(type='list'),

        'relation_infra_rs_dwdm_if_pol': dict(type='str'),

        'relation_infra_rs_qos_pfc_if_pol': dict(type='str'),

        'relation_infra_rs_qos_sd_if_pol': dict(type='str'),

        'relation_infra_rs_mon_if_infra_pol': dict(type='str'),

        'relation_infra_rs_fc_if_pol': dict(type='str'),

        'relation_infra_rs_qos_ingress_dpp_if_pol': dict(type='str'),

        'relation_infra_rs_cdp_if_pol': dict(type='str'),

        'relation_infra_rs_l2_if_pol': dict(type='str'),

        'relation_infra_rs_stp_if_pol': dict(type='str'),

        'relation_infra_rs_qos_egress_dpp_if_pol': dict(type='str'),

        'relation_infra_rs_att_ent_p': dict(type='str'),

        'relation_infra_rs_l2_inst_pol': dict(type='str'),

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
    
    relation_infrarsspanvsrcgrp = module.params['relation_infra_rs_span_v_src_grp']
    relation_infrarsstormctrlifpol = module.params['relation_infra_rs_stormctrl_if_pol']
    relation_infrarspoeifpol = module.params['relation_infra_rs_poe_if_pol']
    relation_infrarslldpifpol = module.params['relation_infra_rs_lldp_if_pol']
    relation_infrarsmacsecifpol = module.params['relation_infra_rs_macsec_if_pol']
    relation_infrarsqosdppifpol = module.params['relation_infra_rs_qos_dpp_if_pol']
    relation_infrarshifpol = module.params['relation_infra_rs_h_if_pol']
    relation_infrarsnetflowmonitorpol = module.params['relation_infra_rs_netflow_monitor_pol']
    relation_infrarsl2portauthpol = module.params['relation_infra_rs_l2_port_auth_pol']
    relation_infrarsmcpifpol = module.params['relation_infra_rs_mcp_if_pol']
    relation_infrarsl2portsecuritypol = module.params['relation_infra_rs_l2_port_security_pol']
    relation_infrarscoppifpol = module.params['relation_infra_rs_copp_if_pol']
    relation_infrarsspanvdestgrp = module.params['relation_infra_rs_span_v_dest_grp']
    relation_infrarsdwdmifpol = module.params['relation_infra_rs_dwdm_if_pol']
    relation_infrarsqospfcifpol = module.params['relation_infra_rs_qos_pfc_if_pol']
    relation_infrarsqossdifpol = module.params['relation_infra_rs_qos_sd_if_pol']
    relation_infrarsmonifinfrapol = module.params['relation_infra_rs_mon_if_infra_pol']
    relation_infrarsfcifpol = module.params['relation_infra_rs_fc_if_pol']
    relation_infrarsqosingressdppifpol = module.params['relation_infra_rs_qos_ingress_dpp_if_pol']
    relation_infrarscdpifpol = module.params['relation_infra_rs_cdp_if_pol']
    relation_infrarsl2ifpol = module.params['relation_infra_rs_l2_if_pol']
    relation_infrarsstpifpol = module.params['relation_infra_rs_stp_if_pol']
    relation_infrarsqosegressdppifpol = module.params['relation_infra_rs_qos_egress_dpp_if_pol']
    relation_infrarsattentp = module.params['relation_infra_rs_att_ent_p']
    relation_infrarsl2instpol = module.params['relation_infra_rs_l2_inst_pol']

    if relation_infrarsspanvsrcgrp:
        for relation_param in relation_infrarsspanvsrcgrp:
            child_configs.append({'infraRsSpanVSrcGrp': {'attributes': {'tnSpanVSrcGrpName': relation_param}}})
    if relation_infrarsstormctrlifpol:
        child_configs.append({'infraRsStormctrlIfPol': {'attributes': {'tnStormctrlIfPolName': relation_infrarsstormctrlifpol}}})
    if relation_infrarspoeifpol:
        child_configs.append({'infraRsPoeIfPol': {'attributes': {'tnPoeIfPolName': relation_infrarspoeifpol}}})
    if relation_infrarslldpifpol:
        child_configs.append({'infraRsLldpIfPol': {'attributes': {'tnLldpIfPolName': relation_infrarslldpifpol}}})
    if relation_infrarsmacsecifpol:
        child_configs.append({'infraRsMacsecIfPol': {'attributes': {'tnMacsecIfPolName': relation_infrarsmacsecifpol}}})
    if relation_infrarsqosdppifpol:
        child_configs.append({'infraRsQosDppIfPol': {'attributes': {'tnQosDppPolName': relation_infrarsqosdppifpol}}})
    if relation_infrarshifpol:
        child_configs.append({'infraRsHIfPol': {'attributes': {'tnFabricHIfPolName': relation_infrarshifpol}}})

    if relation_infrarsnetflowmonitorpol:
        for relation_param in relation_infrarsnetflowmonitorpol:
            child_configs.append({'infraRsNetflowMonitorPol':{'attributes': { 'tnNetflowMonitorPolName': relation_param['tnNetflowMonitorPolName'] , 'fltType': relation_param['fltType']  }}})
    if relation_infrarsl2portauthpol:
        child_configs.append({'infraRsL2PortAuthPol': {'attributes': {'tnL2PortAuthPolName': relation_infrarsl2portauthpol}}})
    if relation_infrarsmcpifpol:
        child_configs.append({'infraRsMcpIfPol': {'attributes': {'tnMcpIfPolName': relation_infrarsmcpifpol}}})
    if relation_infrarsl2portsecuritypol:
        child_configs.append({'infraRsL2PortSecurityPol': {'attributes': {'tnL2PortSecurityPolName': relation_infrarsl2portsecuritypol}}})
    if relation_infrarscoppifpol:
        child_configs.append({'infraRsCoppIfPol': {'attributes': {'tnCoppIfPolName': relation_infrarscoppifpol}}})

    if relation_infrarsspanvdestgrp:
        for relation_param in relation_infrarsspanvdestgrp:
            child_configs.append({'infraRsSpanVDestGrp': {'attributes': {'tnSpanVDestGrpName': relation_param}}})
    if relation_infrarsdwdmifpol:
        child_configs.append({'infraRsDwdmIfPol': {'attributes': {'tnDwdmIfPolName': relation_infrarsdwdmifpol}}})
    if relation_infrarsqospfcifpol:
        child_configs.append({'infraRsQosPfcIfPol': {'attributes': {'tnQosPfcIfPolName': relation_infrarsqospfcifpol}}})
    if relation_infrarsqossdifpol:
        child_configs.append({'infraRsQosSdIfPol': {'attributes': {'tnQosSdIfPolName': relation_infrarsqossdifpol}}})
    if relation_infrarsmonifinfrapol:
        child_configs.append({'infraRsMonIfInfraPol': {'attributes': {'tnMonInfraPolName': relation_infrarsmonifinfrapol}}})
    if relation_infrarsfcifpol:
        child_configs.append({'infraRsFcIfPol': {'attributes': {'tnFcIfPolName': relation_infrarsfcifpol}}})
    if relation_infrarsqosingressdppifpol:
        child_configs.append({'infraRsQosIngressDppIfPol': {'attributes': {'tnQosDppPolName': relation_infrarsqosingressdppifpol}}})
    if relation_infrarscdpifpol:
        child_configs.append({'infraRsCdpIfPol': {'attributes': {'tnCdpIfPolName': relation_infrarscdpifpol}}})
    if relation_infrarsl2ifpol:
        child_configs.append({'infraRsL2IfPol': {'attributes': {'tnL2IfPolName': relation_infrarsl2ifpol}}})
    if relation_infrarsstpifpol:
        child_configs.append({'infraRsStpIfPol': {'attributes': {'tnStpIfPolName': relation_infrarsstpifpol}}})
    if relation_infrarsqosegressdppifpol:
        child_configs.append({'infraRsQosEgressDppIfPol': {'attributes': {'tnQosDppPolName': relation_infrarsqosegressdppifpol}}})
    if relation_infrarsattentp:
        child_configs.append({'infraRsAttEntP': {'attributes': {'tnInfraAttEntityPName': relation_infrarsattentp}}})
    if relation_infrarsl2instpol:
        child_configs.append({'infraRsL2InstPol': {'attributes': {'tnL2InstPolName': relation_infrarsl2instpol}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'infraAccPortGrp',
            'aci_rn': 'infra/funcprof/accportgrp-{}'.format(name),
            'target_filter': 'eq(infraAccPortGrp.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['infraRsSpanVSrcGrp','infraRsStormctrlIfPol','infraRsPoeIfPol','infraRsLldpIfPol','infraRsMacsecIfPol','infraRsQosDppIfPol','infraRsHIfPol','infraRsNetflowMonitorPol','infraRsL2PortAuthPol','infraRsMcpIfPol','infraRsL2PortSecurityPol','infraRsCoppIfPol','infraRsSpanVDestGrp','infraRsDwdmIfPol','infraRsQosPfcIfPol','infraRsQosSdIfPol','infraRsMonIfInfraPol','infraRsFcIfPol','infraRsQosIngressDppIfPol','infraRsCdpIfPol','infraRsL2IfPol','infraRsStpIfPol','infraRsQosEgressDppIfPol','infraRsAttEntP','infraRsL2InstPol']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='infraAccPortGrp',
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

        aci.get_diff(aci_class='infraAccPortGrp')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
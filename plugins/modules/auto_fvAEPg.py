#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvAEPg 
short_description: Manage Application EPG (fv:AEPg)
description:
- endpoint group
notes:
- More information about the internal APIC class B(fv:AEPg) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  descr:
    description:
    - policy component description 
  exceptionTag:
    description:
    - Mo doc not defined in techpub!!! 
  floodOnEncap:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ disabled, enabled ] 
  fwdCtrl:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ none, proxy-arp ] 
  hasMcastSource:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  isAttrBasedEPg:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  matchT:
    description:
    - match criteria 
    choices: [ All, AtleastOne, AtmostOne, None ] 
  name:
    description:
    - endpoint group name 
    aliases: [ application_epg ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  pcEnfPref:
    description:
    - enforcement preference 
    choices: [ enforced, unenforced ] 
  prefGrMemb:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ exclude, include ] 
  prio:
    description:
    - qos priority class id 
    choices: [ level1, level2, level3, level4, level5, level6, unspecified ] 
  shutdown:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  tenant:
    description:
    - tenant name 
  application_profile:
    description:
    - application profile name 
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
        'exceptionTag': dict(type='str',),
        'floodOnEncap': dict(type='str', choices=['disabled', 'enabled'], ),
        'fwdCtrl': dict(type='str', choices=['none', 'proxy-arp'], ),
        'hasMcastSource': dict(type='str', choices=['no', 'yes'], ),
        'isAttrBasedEPg': dict(type='str', choices=['no', 'yes'], ),
        'matchT': dict(type='str', choices=['All', 'AtleastOne', 'AtmostOne', 'None'], ),
        'name': dict(type='str', aliases=['application_epg']),
        'nameAlias': dict(type='str',),
        'pcEnfPref': dict(type='str', choices=['enforced', 'unenforced'], ),
        'prefGrMemb': dict(type='str', choices=['exclude', 'include'], ),
        'prio': dict(type='str', choices=['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'unspecified'], ),
        'shutdown': dict(type='str', choices=['no', 'yes'], ),
        'tenant': dict(type='str',),
        'application_profile': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_bd': dict(type='str'),

        'relation_fv_rs_cust_qos_pol': dict(type='str'),

        'relation_fv_rs_dom_att': dict(type='list'),

        'relation_fv_rs_fc_path_att': dict(type='list'),

        'relation_fv_rs_prov': dict(type='list'),

        'relation_fv_rs_graph_def': dict(type='list'),

        'relation_fv_rs_cons_if': dict(type='list'),

        'relation_fv_rs_sec_inherited': dict(type='list'),

        'relation_fv_rs_node_att': dict(type='list'),

        'relation_fv_rs_dpp_pol': dict(type='str'),

        'relation_fv_rs_cons': dict(type='list'),

        'relation_fv_rs_prov_def': dict(type='list'),

        'relation_fv_rs_trust_ctrl': dict(type='str'),

        'relation_fv_rs_path_att': dict(type='list'),

        'relation_fv_rs_prot_by': dict(type='list'),

        'relation_fv_rs_ae_pg_mon_pol': dict(type='str'),

        'relation_fv_rs_intra_epg': dict(type='list'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'tenant', 'application_profile', ]], 
            ['state', 'present', ['name', 'tenant', 'application_profile', ]],
        ],
    )
    
    annotation = module.params['annotation']
    descr = module.params['descr']
    exceptionTag = module.params['exceptionTag']
    floodOnEncap = module.params['floodOnEncap']
    fwdCtrl = module.params['fwdCtrl']
    hasMcastSource = module.params['hasMcastSource']
    isAttrBasedEPg = module.params['isAttrBasedEPg']
    matchT = module.params['matchT']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    pcEnfPref = module.params['pcEnfPref']
    prefGrMemb = module.params['prefGrMemb']
    prio = module.params['prio']
    shutdown = module.params['shutdown']
    tenant = module.params['tenant']
    application_profile = module.params['application_profile']
    state = module.params['state']
    child_configs=[]
    
    relation_fvrsbd = module.params['relation_fv_rs_bd']
    relation_fvrscustqospol = module.params['relation_fv_rs_cust_qos_pol']
    relation_fvrsdomatt = module.params['relation_fv_rs_dom_att']
    relation_fvrsfcpathatt = module.params['relation_fv_rs_fc_path_att']
    relation_fvrsprov = module.params['relation_fv_rs_prov']
    relation_fvrsgraphdef = module.params['relation_fv_rs_graph_def']
    relation_fvrsconsif = module.params['relation_fv_rs_cons_if']
    relation_fvrssecinherited = module.params['relation_fv_rs_sec_inherited']
    relation_fvrsnodeatt = module.params['relation_fv_rs_node_att']
    relation_fvrsdpppol = module.params['relation_fv_rs_dpp_pol']
    relation_fvrscons = module.params['relation_fv_rs_cons']
    relation_fvrsprovdef = module.params['relation_fv_rs_prov_def']
    relation_fvrstrustctrl = module.params['relation_fv_rs_trust_ctrl']
    relation_fvrspathatt = module.params['relation_fv_rs_path_att']
    relation_fvrsprotby = module.params['relation_fv_rs_prot_by']
    relation_fvrsaepgmonpol = module.params['relation_fv_rs_ae_pg_mon_pol']
    relation_fvrsintraepg = module.params['relation_fv_rs_intra_epg']
    if relation_fvrsbd:
        child_configs.append({'fvRsBd': {'attributes': {'tnFvBDName': relation_fvrsbd}}})
    if relation_fvrscustqospol:
        child_configs.append({'fvRsCustQosPol': {'attributes': {'tnQosCustomPolName': relation_fvrscustqospol}}})

    if relation_fvrsdomatt:
        for relation_param in relation_fvrsdomatt:
            child_configs.append({'fvRsDomAtt': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsfcpathatt:
        for relation_param in relation_fvrsfcpathatt:
            child_configs.append({'fvRsFcPathAtt': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsprov:
        for relation_param in relation_fvrsprov:
            child_configs.append({'fvRsProv': {'attributes': {'tnVzBrCPName': relation_param}}})

    if relation_fvrsgraphdef:
        for relation_param in relation_fvrsgraphdef:
            child_configs.append({'fvRsGraphDef': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsconsif:
        for relation_param in relation_fvrsconsif:
            child_configs.append({'fvRsConsIf': {'attributes': {'tnVzCPIfName': relation_param}}})

    if relation_fvrssecinherited:
        for relation_param in relation_fvrssecinherited:
            child_configs.append({'fvRsSecInherited': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsnodeatt:
        for relation_param in relation_fvrsnodeatt:
            child_configs.append({'fvRsNodeAtt': {'attributes': {'tDn': relation_param}}})
    if relation_fvrsdpppol:
        child_configs.append({'fvRsDppPol': {'attributes': {'tnQosDppPolName': relation_fvrsdpppol}}})

    if relation_fvrscons:
        for relation_param in relation_fvrscons:
            child_configs.append({'fvRsCons': {'attributes': {'tnVzBrCPName': relation_param}}})

    if relation_fvrsprovdef:
        for relation_param in relation_fvrsprovdef:
            child_configs.append({'fvRsProvDef': {'attributes': {'tDn': relation_param}}})
    if relation_fvrstrustctrl:
        child_configs.append({'fvRsTrustCtrl': {'attributes': {'tnFhsTrustCtrlPolName': relation_fvrstrustctrl}}})

    if relation_fvrspathatt:
        for relation_param in relation_fvrspathatt:
            child_configs.append({'fvRsPathAtt': {'attributes': {'tDn': relation_param}}})

    if relation_fvrsprotby:
        for relation_param in relation_fvrsprotby:
            child_configs.append({'fvRsProtBy': {'attributes': {'tnVzTabooName': relation_param}}})
    if relation_fvrsaepgmonpol:
        child_configs.append({'fvRsAEPgMonPol': {'attributes': {'tnMonEPGPolName': relation_fvrsaepgmonpol}}})

    if relation_fvrsintraepg:
        for relation_param in relation_fvrsintraepg:
            child_configs.append({'fvRsIntraEpg': {'attributes': {'tnVzBrCPName': relation_param}}})
    aci = ACIModule(module)
    aci.construct_url(
        root_class={
            'aci_class': 'fvTenant',
            'aci_rn': 'tn-{}'.format(tenant),
            'target_filter': 'eq(fvTenant.name, "{}")'.format(tenant),
            'module_object': tenant
        }, 
        subclass_1={
            'aci_class': 'fvAp',
            'aci_rn': 'ap-{}'.format(application_profile),
            'target_filter': 'eq(fvAp.name, "{}")'.format(application_profile),
            'module_object': application_profile
        }, 
        subclass_2={
            'aci_class': 'fvAEPg',
            'aci_rn': 'epg-{}'.format(name),
            'target_filter': 'eq(fvAEPg.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=['fvRsBd','fvRsCustQosPol','fvRsDomAtt','fvRsFcPathAtt','fvRsProv','fvRsGraphDef','fvRsConsIf','fvRsSecInherited','fvRsNodeAtt','fvRsDppPol','fvRsCons','fvRsProvDef','fvRsTrustCtrl','fvRsPathAtt','fvRsProtBy','fvRsAEPgMonPol','fvRsIntraEpg']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvAEPg',
            class_config={ 
                'annotation': annotation,
                'descr': descr,
                'exceptionTag': exceptionTag,
                'floodOnEncap': floodOnEncap,
                'fwdCtrl': fwdCtrl,
                'hasMcastSource': hasMcastSource,
                'isAttrBasedEPg': isAttrBasedEPg,
                'matchT': matchT,
                'name': name,
                'nameAlias': nameAlias,
                'pcEnfPref': pcEnfPref,
                'prefGrMemb': prefGrMemb,
                'prio': prio,
                'shutdown': shutdown,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvAEPg')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
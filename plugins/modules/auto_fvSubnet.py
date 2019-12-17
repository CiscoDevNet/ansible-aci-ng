#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_fvSubnet 
short_description: Manage Subnet (fv:Subnet)
description:
- epg subnet
notes:
- More information about the internal APIC class B(fv:Subnet) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  ctrl:
    description:
    - subnet control state 
    choices: [ nd, no-default-gateway, querier, unspecified ] 
  descr:
    description:
    - policy component description 
  ip:
    description:
    - default gateway IP address and mask 
  name:
    description:
    - object name 
    aliases: [ subnet ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  preferred:
    description:
    - subnet preferred status 
    choices: [ no, yes ] 
  scope:
    description:
    - subnet visibility 
    choices: [ private, public, shared ] 
  virtual:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ no, yes ] 
  tenant:
    description:
    - tenant name 
  bridge_domain:
    description:
    - bridge domain name 
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
        'ctrl': dict(type='str', choices=['nd', 'no-default-gateway', 'querier', 'unspecified'], ),
        'descr': dict(type='str',),
        'ip': dict(type='str',),
        'name': dict(type='str', aliases=['subnet']),
        'nameAlias': dict(type='str',),
        'preferred': dict(type='str', choices=['no', 'yes'], ),
        'scope': dict(type='str', choices=['private', 'public', 'shared'], ),
        'virtual': dict(type='str', choices=['no', 'yes'], ),
        'tenant': dict(type='str',),
        'bridge_domain': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

        'relation_fv_rs_bd_subnet_to_out': dict(type='list'),

        'relation_fv_rs_nd_pfx_pol': dict(type='str'),

        'relation_fv_rs_bd_subnet_to_profile': dict(type='str'),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['ip', 'tenant', 'bridge_domain', ]], 
            ['state', 'present', ['ip', 'tenant', 'bridge_domain', ]],
        ],
    )
    
    annotation = module.params['annotation']
    ctrl = module.params['ctrl']
    descr = module.params['descr']
    ip = module.params['ip']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    preferred = module.params['preferred']
    scope = module.params['scope']
    virtual = module.params['virtual']
    tenant = module.params['tenant']
    bridge_domain = module.params['bridge_domain']
    state = module.params['state']
    child_configs=[]
    
    relation_fvrsbdsubnettoout = module.params['relation_fv_rs_bd_subnet_to_out']
    relation_fvrsndpfxpol = module.params['relation_fv_rs_nd_pfx_pol']
    relation_fvrsbdsubnettoprofile = module.params['relation_fv_rs_bd_subnet_to_profile']

    if relation_fvrsbdsubnettoout:
        for relation_param in relation_fvrsbdsubnettoout:
            child_configs.append({'fvRsBDSubnetToOut': {'attributes': {'tnL3extOutName': relation_param}}})
    if relation_fvrsndpfxpol:
        child_configs.append({'fvRsNdPfxPol': {'attributes': {'tnNdPfxPolName': relation_fvrsndpfxpol}}})
    if relation_fvrsbdsubnettoprofile:
        child_configs.append({'fvRsBDSubnetToProfile': {'attributes': {'tnRtctrlProfileName': relation_fvrsbdsubnettoprofile}}})
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
            'aci_rn': 'BD-{}'.format(bridge_domain),
            'target_filter': 'eq(fvBD.name, "{}")'.format(bridge_domain),
            'module_object': bridge_domain
        }, 
        subclass_2={
            'aci_class': 'fvSubnet',
            'aci_rn': 'subnet-[{}]'.format(ip),
            'target_filter': 'eq(fvSubnet.ip, "{}")'.format(ip),
            'module_object': ip
        }, 
        
        child_classes=['fvRsBDSubnetToOut','fvRsNdPfxPol','fvRsBDSubnetToProfile']
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='fvSubnet',
            class_config={ 
                'annotation': annotation,
                'ctrl': ctrl,
                'descr': descr,
                'ip': ip,
                'name': name,
                'nameAlias': nameAlias,
                'preferred': preferred,
                'scope': scope,
                'virtual': virtual,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='fvSubnet')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
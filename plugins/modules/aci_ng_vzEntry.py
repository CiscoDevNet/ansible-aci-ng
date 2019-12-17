#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: auto_vzEntry 
short_description: Manage Filter Entry (vz:Entry)
description:
- filter entry
notes:
- More information about the internal APIC class B(vz:Entry) from
  L(the APIC Management Information Model reference,https://developer.cisco.com/docs/apic-mim-ref/).
author:
- Devarshi Shah (@devarshishah3)
options: 
  annotation:
    description:
    - Mo doc not defined in techpub!!! 
  applyToFrag:
    description:
    - fragment 
    choices: [ no, yes ] 
  arpOpc:
    description:
    - open peripheral codes 
    choices: [ reply, req, unspecified ] 
  dFromPort:
    description:
    - end of the destination port range 
    choices: [ dns, ftpData, http, https, pop3, rtsp, smtp, unspecified ] 
  dToPort:
    description:
    - start of the destination port range 
    choices: [ dns, ftpData, http, https, pop3, rtsp, smtp, unspecified ] 
  descr:
    description:
    - description of a filter entry 
  etherT:
    description:
    - ethertype 
    choices: [ arp, fcoe, ip, ipv4, ipv6, mac_security, mpls_ucast, trill, unspecified ] 
  icmpv4T:
    description:
    -  
    choices: [ dst-unreach, echo, echo-rep, src-quench, time-exceeded, unspecified ] 
  icmpv6T:
    description:
    -  
    choices: [ dst-unreach, echo-rep, echo-req, nbr-advert, nbr-solicit, redirect, time-exceeded, unspecified ] 
  matchDscp:
    description:
    - Mo doc not defined in techpub!!! 
    choices: [ AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, CS0, CS1, CS2, CS3, CS4, CS5, CS6, CS7, EF, VA, unspecified ] 
  name:
    description:
    - name of a filter entry 
    aliases: [ filter_entry ] 
  nameAlias:
    description:
    - Mo doc not defined in techpub!!! 
  prot:
    description:
    - level 3 ip protocol 
    choices: [ egp, eigrp, icmp, icmpv6, igmp, igp, l2tp, ospfigp, pim, tcp, udp, unspecified ] 
  sFromPort:
    description:
    - start of the source port range 
    choices: [ dns, ftpData, http, https, pop3, rtsp, smtp, unspecified ] 
  sToPort:
    description:
    - end of the source port range 
    choices: [ dns, ftpData, http, https, pop3, rtsp, smtp, unspecified ] 
  stateful:
    description:
    - stateful entry 
    choices: [ no, yes ] 
  tcpRules:
    description:
    - tcp flags 
    choices: [ ack, est, fin, rst, syn, unspecified ] 
  tenant:
    description:
    - tenant name 
  filter:
    description:
    - name of a filter policy 
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
        'applyToFrag': dict(type='str', choices=['no', 'yes'], ),
        'arpOpc': dict(type='str', choices=['reply', 'req', 'unspecified'], ),
        'dFromPort': dict(type='str', choices=['dns', 'ftpData', 'http', 'https', 'pop3', 'rtsp', 'smtp', 'unspecified'], ),
        'dToPort': dict(type='str', choices=['dns', 'ftpData', 'http', 'https', 'pop3', 'rtsp', 'smtp', 'unspecified'], ),
        'descr': dict(type='str',),
        'etherT': dict(type='str', choices=['arp', 'fcoe', 'ip', 'ipv4', 'ipv6', 'mac_security', 'mpls_ucast', 'trill', 'unspecified'], ),
        'icmpv4T': dict(type='str', choices=['dst-unreach', 'echo', 'echo-rep', 'src-quench', 'time-exceeded', 'unspecified'], ),
        'icmpv6T': dict(type='str', choices=['dst-unreach', 'echo-rep', 'echo-req', 'nbr-advert', 'nbr-solicit', 'redirect', 'time-exceeded', 'unspecified'], ),
        'matchDscp': dict(type='str', choices=['AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'EF', 'VA', 'unspecified'], ),
        'name': dict(type='str', aliases=['filter_entry']),
        'nameAlias': dict(type='str',),
        'prot': dict(type='str', choices=['egp', 'eigrp', 'icmp', 'icmpv6', 'igmp', 'igp', 'l2tp', 'ospfigp', 'pim', 'tcp', 'udp', 'unspecified'], ),
        'sFromPort': dict(type='str', choices=['dns', 'ftpData', 'http', 'https', 'pop3', 'rtsp', 'smtp', 'unspecified'], ),
        'sToPort': dict(type='str', choices=['dns', 'ftpData', 'http', 'https', 'pop3', 'rtsp', 'smtp', 'unspecified'], ),
        'stateful': dict(type='str', choices=['no', 'yes'], ),
        'tcpRules': dict(type='str', choices=['ack', 'est', 'fin', 'rst', 'syn', 'unspecified'], ),
        'tenant': dict(type='str',),
        'filter': dict(type='str',),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query']),

    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[ 
            ['state', 'absent', ['name', 'tenant', 'filter', ]], 
            ['state', 'present', ['name', 'tenant', 'filter', ]],
        ],
    )
    
    annotation = module.params['annotation']
    applyToFrag = module.params['applyToFrag']
    arpOpc = module.params['arpOpc']
    dFromPort = module.params['dFromPort']
    dToPort = module.params['dToPort']
    descr = module.params['descr']
    etherT = module.params['etherT']
    icmpv4T = module.params['icmpv4T']
    icmpv6T = module.params['icmpv6T']
    matchDscp = module.params['matchDscp']
    name = module.params['name']
    nameAlias = module.params['nameAlias']
    prot = module.params['prot']
    sFromPort = module.params['sFromPort']
    sToPort = module.params['sToPort']
    stateful = module.params['stateful']
    tcpRules = module.params['tcpRules']
    tenant = module.params['tenant']
    filter = module.params['filter']
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
            'aci_class': 'vzFilter',
            'aci_rn': 'flt-{}'.format(filter),
            'target_filter': 'eq(vzFilter.name, "{}")'.format(filter),
            'module_object': filter
        }, 
        subclass_2={
            'aci_class': 'vzEntry',
            'aci_rn': 'e-{}'.format(name),
            'target_filter': 'eq(vzEntry.name, "{}")'.format(name),
            'module_object': name
        }, 
        
        child_classes=[]
        
    )

    aci.get_existing()

    if state == 'present':
        aci.payload(
            aci_class='vzEntry',
            class_config={ 
                'annotation': annotation,
                'applyToFrag': applyToFrag,
                'arpOpc': arpOpc,
                'dFromPort': dFromPort,
                'dToPort': dToPort,
                'descr': descr,
                'etherT': etherT,
                'icmpv4T': icmpv4T,
                'icmpv6T': icmpv6T,
                'matchDscp': matchDscp,
                'name': name,
                'nameAlias': nameAlias,
                'prot': prot,
                'sFromPort': sFromPort,
                'sToPort': sToPort,
                'stateful': stateful,
                'tcpRules': tcpRules,
            },
            child_configs=child_configs
           
        )

        aci.get_diff(aci_class='vzEntry')

        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    aci.exit_json()

if __name__ == "__main__":
    main()
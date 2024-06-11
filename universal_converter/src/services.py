#!/usr/bin/python3
from dataclasses import dataclass


@dataclass(frozen = True)
class ServicePorts:
    tcp = {
        '1': 'tcpmux',
        '7': 'echo-tcp',
        '9': 'discard-udp',
        '11': 'systat',
        '13': 'daytime-tcp',
        '15': 'netstat',
        '17': 'qotd',
        '19': 'chargen-tcp',
        '20': 'ftp-data',
        '21': 'ftp-control',
        '22': 'SSH',
        '23': 'Telnet',
        '25': 'SMTP',
        '37': 'time-tcp',
        '43': 'whois',
        '49': 'tacacs-tcp',
        '53': 'DNS-tcp',
        '67': 'DHCP-tcp',
        '70': 'gopher',
        '79': 'finger',
        '80': 'HTTP',
        '88': 'kerberos-tcp',
        '102': 'iso-tsap',
        '104': 'acr-nema',
        '106': 'poppassd',
        '109': 'pop2',
        '110': 'POP3',
        '111': 'RPC portmapper-tcp',
        '113': 'auth tap ident',
        '119': 'nntp',
        '135': 'epmap',
        '139': 'Netbios session service',
        '143': 'IMAP',
        '161': 'SNMP-tcp',
        '162': 'SNMPTRAP-tcp',
        '163': '',
        '443': 'HTTPS',
        '445': 'SMB',
        '465': 'SMTPS',
        '873': 'Rsync',
        '993': 'IMAPS',
        '995': 'POP3S',
        '1194': 'OpenVPN-tcp',
        '1433-1434': 'MS SQL',
        '1494': 'Citrix',
        '1503': 'NetMeeting',
        '1645-1646': 'Radius-tcp',
        '1723': 'VPN PPTP - tcp',
        '2041-2042': 'Mail Agent',
        '2404': 'SCADA',
        '2598': 'Citrix',
        '3050': 'Firebird',
        '3306': 'MySQL',
        '3389': 'RDP',
        '3690': 'SVN-tcp',
        '4899': 'Radmin',
        '5000': 'UPnP',
        '5004-5005': 'RTP-tcp',
        '5060': 'SIP-tcp-5090',
        '5061': 'SIP auth',
        '5060-5061': 'SIP-tcp',
        '5190': 'ICQ',
        '5222': 'XMPP-CLIENT',
        '5269': 'XMPP-SERVER',
        '5432': 'Postgres SQL',
        '6665-6669': 'IRC',
        '6881-6999': 'Torrents-tcp',
        '8080': 'CheckPoint Proxy',
        '8090': 'HTTP Proxy',
        '8091': 'HTTPS Proxy',
        '1000-65535': 'TCP 1000-65535',
        '10053': 'DNS Proxy-tcp',
        }
    udp = {
        '7': 'echo-udp',
        '9': 'discard-udp',
        '13': 'daytime-udp',
        '19': 'chargen-udp',
        '37': 'time-udp',
        '49': 'tacacs-udp',
        '53': 'DNS-udp',
        '67': 'DHCP bootps',
        '68': 'DHCP bootpc',
        '69': 'TFTP',
        '80': 'Quick UDP Internet Connections (port 80)',
        '87': 'Client-Bank Sberbank',
        '88': 'kerberos-udp',
        '111': 'RPC portmapper-udp',
        '123': 'NTP',
        '137': 'Netbios Name Service',
        '138': 'Netbios Datagram Service',
        '161': 'SNMP-udp',
        '162': 'SNMPTRAP-udp',
        '443': 'Quick UDP Internet Connections (port 443)',
        '1194': 'OpenVPN-udp',
        '1645-1646': 'Radius-udp',
        '3690': 'SVN-udp',
        '4500': 'IPSec-udp',
        '5004-5005': 'RTP-udp',
        '5060': 'SIP-udp',
        '5777': 'VipNet Client (port 5777)',
        '6881-6999': 'Torrents-udp',
        '1000-65535': 'UDP 1000-65535',
        '10053': 'DNS Proxy-udp',
        '55777': 'VipNet Client (port 55777)',
        }

    @classmethod
    def get_dict_by_port(cls, proto, service_port, service_name):
        try:
            if proto == 'tcp':
                return {'type': 'service', 'name': cls.tcp[service_port]}
            else:
                return {'type': 'service', 'name': cls.udp[service_port]}
        except KeyError:
            return {'type': 'service', 'name': service_name}

    @classmethod
    def get_name_by_port(cls, proto, service_port, service_name):
        try:
            if proto == 'tcp':
                return cls.tcp[service_port]
            else:
                return cls.udp[service_port]
        except KeyError:
            return service_name


default_urlcategorygroup = {
    'URL_CATEGORY_GROUP_PARENTAL_CONTROL': 'Parental Control',
    'URL_CATEGORY_GROUP_PRODUCTIVITY': 'Productivity',
    'URL_CATEGORY_GROUP_SAFE': 'Safe categories',
    'URL_CATEGORY_GROUP_THREATS': 'Threats',
    'URL_CATEGORY_MORPHO_RECOMMENDED': 'Recommended for morphology checking',
    'URL_CATEGORY_VIRUSCHECK_RECOMMENDED': 'Recommended for virus check'
}


dict_risk = {
    'Very Low': 1,
    'Low': 2,
    'Medium': 3,
    'High': 4,
    'Critical': 5,
    'Unknown': 1,
}

character_map = {
    ord('\n'): None,
    ord('\t'): None,
    ord('\r'): None,
}
trans_table = str.maketrans(character_map)

character_map_file_name = {
    ord('\n'): None,
    ord('\t'): None,
    ord('\r'): None,
    '#': None,
    '=': '_',
    ':': '_',
    '"': None,
    "'": None,
    '!': '_',
    '?': '_',
    '@': '_',
    ';': None,
    '$': None,
    '%': None,
    '&': None,
    '^': None,
    '[': None,
    ']': None,
    '{': None,
    '}': None,
    '*': '+',
    '<': None,
    '>': None,
    '|': None,
    '/': '_',
    '\\': None,
}
trans_filename = str.maketrans(character_map_file_name)

character_map_for_name = {
    ord('\n'): None,
    ord('\t'): None,
    ord('\r'): None,
    '#': None,
    '=': ' ',
    '"': None,
    "'": None,
    '!': None,
    '?': ' ',
    '@': None,
    ';': " ",
    '$': None,
    '%': None,
    '&': " ",
    '^': None,
    '[': None,
    ']': None,
    '{': None,
    '}': None,
    '*': '+',
    '~': None,
    '<': None,
    '>': None,
    '|': "-",
    '\\': None,
}
trans_name = str.maketrans(character_map_for_name)

character_map_userlogin = {
    '-': '_',
    ' ': '_',
    '.': '_',
    '"': None,
    "'": None,
    '!': None,
    '?': None,
    '@': None,
    ';': None,
    '$': None,
    '%': None,
    '&': None,
    '^': None,
    '[': None,
    ']': None,
    '{': None,
    '}': None,
    '*': None,
    '+': '_',
    '<': None,
    '>': None,
    '|': "_",
    '/': None,
    '\\': None,
}
trans_userlogin = str.maketrans(character_map_userlogin)

character_map_for_url = {
    '{': None,
    '}': None,
    '(': None,
    ')': None,
    '[': None,
    ']': None,
    '\\': None,
}
trans_url = str.maketrans(character_map_for_url)

ip_proto = {
    '0': 'ip',          # ASA
    '1': 'icmp',        # ASA
    '2': 'igmp',        # ASA
    '3': 'ggp',
    '4': 'ipip',        # ASA
    '5': 'st',
    '6': 'tcp',
    '8': 'egp',
    '9': 'igp',
    '11': 'pup',
    '17': 'udp',
    '20': 'hmp',
    '22': 'xns-idp',
    '27': 'rdp',
    '29': 'iso-tp4',
    '33': 'dccp',
    '36': 'xtp',
    '37': 'ddp',
    '38': 'idpr-cmtp',
    '41': 'ipv6',
    '43': 'ipv6-route',
    '44': 'ipv6-frag',
    '45': 'idrp',
    '46': 'rsvp',
    '47': 'gre',        # ASA
    '50': 'esp',        # ASA
    '51': 'ah',         # ASA
    '57': 'skip',
    '58': 'ipv6-icmp',  # ASA
    '59': 'ipv6-nonxt',
    '60': 'ipv6-opts',
    '81': 'vmtp',
    '88': 'eigrp',      # ASA
    '89': 'ospf',       # ASA
    '93': 'ax.25',
    '94': 'nos',        # ASA
    '97': 'etherip',
    '98': 'encap',
    '103': 'pim',       # ASA
    '108': 'ipcomp',
    '109': 'snp',        # ASA
    '112': 'vrrp',
    '115': 'l2tp',
    '124': 'isis',
    '132': 'sctp',
    '133': 'fc',
    '135': 'mobility-header',
    '136': 'udplite',
    '137': 'mpls-in-ip',
    '138': 'manet',
    '139': 'hip',
    '140': 'shim6',
    '141': 'wesp',
    '142': 'rohc'
}

ug_services = {
    'dns': 'DNS',
    'http': 'HTTP',
    'https': 'HTTPS',
    'ftp': 'FTP',
    'icmp': 'Any ICMP',
    'imap4': 'IMAP',
    'ntp': 'NTP',
    'pop3': 'POP3',
    'postgresql': 'Postgres SQL',
    'rdp': 'RDP',
    'rdp-tcp': 'RDP',
    'sip': 'SIP',
    'smtp': 'SMTP',
    'smtps': 'SMTPS',
    'snmp': 'SNMP',
    'ssh': 'SSH',
    'tftp': 'TFTP',
    'www': 'HTTP',
    '873': 'Rsync',
    '80': 'HTTP',
    '5432': 'Postgres SQL',
}

zone_services = {
    1: "Ping",
    2: "SNMP",
    3: False,
    4: "Captive-портал и страница блокировки",
    5: "XML-RPC для управления",
    6: "Кластер",
    7: "VRRP",
    8: "Консоль администрирования",
    9: "DNS",
    10: "HTTP(S)-прокси",
    11: "Агент аутентификации",
    12: "SMTP(S)-прокси",
    13: "POP(S)-прокси",
    14: "CLI по SSH",
    15: "VPN",
    16: False,
    17: "SCADA",
    18: "Reverse-прокси",
    19: "Веб-портал",
    20: False,
    21: False,
    22: "SAML сервер",
    23: "Log analyzer",
    24: "OSPF",
    25: "BGP",
    26: "SNMP-прокси",
    27: "SSH-прокси",
    28: "Multicast",
    29: "NTP сервис",
    30: "RIP",
    31: "UserID syslog collector",
    32: "BFD",
    33: "Endpoints connect",
}

# Для конвертации с Cisco FPR
network_proto = {
    'ah', 'ax.25', 'dccp', 'ddp', 'egp', 'eigrp', 'encap', 'esp', 'etherip', 'fc', 'ggp',
    'gre', 'hip', 'hmp', 'icmp', 'idpr-cmtp', 'idrp', 'igmp', 'igp', 'ipcomp', 'ipencap',
    'ipip', 'ipv6', 'ipv6-frag', 'ipv6-icmp', 'ipv6-nonxt', 'ipv6-opts', 'ipv6-route',
    'isis', 'iso-tp4', 'l2tp', 'manet', 'mobility-header', 'mpls-in-ip', 'ospf', 'pim',
    'pop3', 'pop3s', 'pup', 'rdp', 'rohc', 'rspf', 'rsvp', 'sctp', 'shim6', 'skip', 'smtp',
    'smtps', 'st', 'tcp', 'udp', 'udplite', 'vmtp', 'vrrp', 'wesp', 'xns-idp', 'xtp'
}

service_ports = {
    'tcpmux': '1',
    'echo': '7',
    'discard': '9',
    'systat': '11',
    'daytime': '13',
    'netstat': '15',
    'qotd': '17',
    'chargen': '19',
    'ftp-data': '20',
    'ftp': '21',
    'fsp': '21',
    'ssh': '22',
    'telnet': '23',
    'smtp': '25',
    'time': '37',
    'whois': '43',
    'tacacs': '49',
    'domain': '53',
    'dns': '53',
    'bootps': '67',
    'dhcp': '67',
    'bootpc': '68',
    'tftp': '69',
    'gopher': '70',
    'finger': '79',
    'http': '80',
    'www': '80',
    'kerberos': '88',
    'iso-tsap': '102',
    'acr-nema': '104',
    'poppassd': '106',
    'pop3': '110',
    'sunrpc': '111',
    'auth': '113',
    'nntp': '119',
    'ntp': '123',
    'epmap': '135',
    'netbios-ns': '137',
    'netbios-dgm': '138',
    'netbios-ssn': '139',
    'netbios': '139',
    'imap2': '143',
    'imap4': '143',
    'imap': '143',
    'snmp': '161',
    'snmp-trap': '162',
    'snmptrap': '162',
    'cmip-man': '163',
    'cmip-agent': '164',
    'mailq': '174',
    'xdmcp': '177',
    'bgp': '179',
    'smux': '199',
    'qmtp': '209',
    'z3950': '210',
    'ipx': '213',
    'ptp-event': '319',
    'ptp-general': '320',
    'pawserv': '345',
    'zserv': '346',
    'rpc2portmap': '369',
    'codaauth2': '370',
    'clearcase': '371',
    'ldap': '389',
    'svrloc': '427',
    'https': '443',
    'snpp': '444',
    'microsoft-ds': '445',
    'smb': '445',
    'kpasswd': '464',
    'submissions': '465',
    'smtps': '465',
    'saft': '487',
    'isakmp': '500',
    'exec': '512',
    'biff': '512',
    'login': '513',
    'who': '513',
    'rsh': '514',
    'shell': '514',
    'syslog': '514',
    'lpd': '515',
    'printer': '515',
    'talk': '517',
    'ntalk': '518',
    'route': '520',
    'gdomap': '538',
    'uucp': '540',
    'klogin': '543',
    'kshell': '544',
    'dhcpv6-client': '546',
    'dhcpv6-server': '547',
    'afpovertcp': '548',
    'rtsp': '554',
    'nqs': '607',
    'asf-rmcp': '623',
    'qmqp': '628',
    'ipp': '631',
    'ldp': '646',
    'nntps': '563',
    'submission': '587',
    'ldaps': '636',
    'tinc': '655',
    'silc': '706',
    'kerberos-adm': '749',
    'kerberos4': '750',
    'kerberos-master': '751',
    'passwd-server': '752',
    'krb-prop': '754',
    'moira-db': '775',
    'moira-update': '777',
    'moira-ureg': '779',
    'spamd': '783',
    'domain-s': '853',
    'supfilesrv': '871',
    'rsync': '873',
    'ftps-data': '989',
    'ftps': '990',
    'telnets': '992',
    'imaps': '993',
    'imap4s': '993',
    'pop3s': '995',
    'socks': '1080',
    'proofd': '1093',
    'rootd': '1094',
    'rmiregistry': '1099',
    'supfiledbg': '1127',
    'skkserv': '1178',
    'openvpn': '1194',
    'predict': '1210',
    'rmtcfg': '1236',
    'xtel': '1313',
    'xtelw': '1314',
    'lotusnote': '1352',
    'lotusnotes': '1352',
    'ms-sql-s': '1433',
    'ms-sql-m': '1434',
    'mssql': '1433-1434',
    'ms-sql': '1433-1434',
    'citrix-ica': '1494',
    'netmeeting': '1503',
    'sqlnet': '1521',
    'ingreslock': '1524',
    'support': '1529',
    'datametrics': '1645',
    'sa-msg-port': '1646',
    'kermit': '1649',
    'groupwise': '1677',
    'l2f': '1701',
    'h323': '1720',
    'radius': '1812',
    'radius-acct': '1813',
    'cisco-sccp': '2000',
    'cfinger': '2003',
    'mail agent': '2041-2042',
    'nfs': '2049',
    'gnunet': '2086',
    'rtcm-sc104': '2101',
    'gsigatekeeper': '2119',
    'frox': '2121',
    'iprop': '2121',
    'gris': '2135',
    'cvspserver': '2401',
    'scada': '2404',
    'venus': '2430',
    'venus-se': '2431',
    'codasrv': '2432',
    'codasrv-se': '2433',
    'mon': '2583',
    'citriximaclient': '2598',
    'zebrasrv': '2600',
    'zebra': '2601',
    'ripd': '2602',
    'ripngd': '2603',
    'ospfd': '2604',
    'bgpd': '2605',
    'ospf6d': '2606',
    'ospfapi': '2607',
    'isisd': '2608',
    'dict': '2628',
    'ctiqbe': '2748',
    'f5-globalsite': '2792',
    'gsiftp': '2811',
    'gpsd': '2947',
    'afbackup': '2988',
    'afmbackup': '2989',
    'gds-db': '3050',
    'firebird': '3050',
    'icpv2': '3130',
    'isns': '3205',
    'iscsi-target': '3260',
    'mysql': '3306',
    'ms-wbt-server': '3389',
    'rdp': '3389',
    'nut': '3493',
    'distcc': '3632',
    'daap': '3689',
    'svn': '3690',
    'suucp': '4031',
    'sysrqd': '4094',
    'sieve': '4190',
    'epmd': '4369',
    'remctl': '4373',
    'f5-iquery': '4353',
    'ipsec-nat-t': '4500',
    'ipsec': '4500',
    'fax': '4557',
    'hylafax': '4559',
    'iax': '4569',
    'distmp3': '4600',
    'mtn': '4691',
    'radmin-port': '4899',
    'radmin': '4899',
    'munin': '4949',
    'upnp': '5000',
    'rtp': '5004-5005',
    'enbd-cstatd': '5051',
    'enbd-sstatd': '5052',
    'sip': '5060',
    'sip-tls': '5061',
    'pcrd': '5151',
    'icq': '5190',
    'xmpp-client': '5222',
    'xmpp-server': '5269',
    'cfengine': '5308',
    'mdns': '5353',
    'noclog': '5354',
    'hostmon': '5355',
    'postgresql': '5432',
    'rplay': '5555',
    'freeciv': '5556',
    'nrpe': '5666',
    'nsca': '5667',
    'amqps': '5671',
    'amqp': '5672',
    'mrtd': '5674',
    'bgpsim': '5675',
    'canna': '5680',
    'x11': '6000',
    'x11-1': '6001',
    'x11-2': '6002',
    'x11-3': '6003',
    'x11-4': '6004',
    'x11-5': '6005',
    'x11-6': '6006',
    'x11-7': '6007',
    'gnutella-svc': '6346',
    'gnutella-rtr': '6347',
    'sge-qmaster': '6444',
    'sge-execd': '6445',
    'mysql-proxy': '6446',
    'syslog-tls': '6514',
    'sane-port': '6566',
    'ircd': '6667',
    'irc': '6665-6669',
    'babel': '6696',
    'ircs-u': '6697',
    'torrents': '6881-6999',
    'afs3-fileserver': '7000',
    'afs3-callback': '7001',
    'afs3-prserver': '7002',
    'afs3-vlserver': '7003',
    'afs3-kaserver': '7004',
    'afs3-volser': '7005',
    'afs3-errors': '7006',
    'afs3-bos': '7007',
    'afs3-update': '7008',
    'afs3-rmtsys': '7009',
    'font-service': '7100',
    'zope-ftp': '8021',
    'http-alt': '8080',
    'tproxy': '8081',
    'omniorb': '8088',
    'http proxy': '8090',
    'https proxy': '8091',
    'puppet': '8140',
    'clc-build-daemon': '8990',
    'xinetd': '9098',
    'bacula-dir': '9101',
    'bacula-fd': '9102',
    'bacula-sd': '9103',
    'mandelspawn': '9359',
    'git': '9418',
    'xmms2': '9667',
    'zope': '9673',
    'webmin': '10000',
    'zabbix-agent': '10050',
    'zabbix-trapper': '10051',
    'dns proxy': '10053',
    'amanda': '10080',
    'kamanda': '10081',
    'amandaidx': '10082',
    'amidxtape': '10083',
    'nbd': '10809',
    'dicom': '11112',
    'smsqp': '11201',
    'smsqp': '11201',
    'hkp': '11371',
    'xpilot': '15345',
    'sgi-cmsd': '17001',
    'sgi-crsd': '17002',
    'sgi-gcd': '17003',
    'sgi-cad': '17004',
    'db-lsp': '17500',
    'isdnlog': '20011',
    'isdnlog': '20011',
    'vboxd': '20012',
    'zephyr-srv': '2102',
    'zephyr-clt': '2103',
    'zephyr-hm': '2104',
    'dcap': '22125',
    'gsidcap': '22128',
    'wnn6': '22273',
    'binkp': '24554',
    'asp': '27374',
    'csync2': '30865',
    'vipnet-client': '55777',
    'dircproxy': '57000',
    'tfido': '60177',
    'fido': '60179',
}

MONTHS = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}

TIME_ZONE = {
    "2": "Europe/Kaliningrad",
    "3": "Europe/Moscow",
    "4": "Europe/Samara",
    "5": "Asia/Yekaterinburg",
    "6": "Asia/Omsk",
    "7": "Asia/Krasnoyarsk",
    "8": "Asia/Irkutsk",
    "9": "Asia/Yakutsk",
    "10": "Asia/Vladivostok",
    "11": "Asia/Magadan",
    "12": "Asia/Kamchatka"
}

GEOIP_CODE = {
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Angola": "AO",
    "Asia/Pacific Region": "AP",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Åland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Bermuda": "BM",
    "Brunei": "BN",
    "Bolivia": "BO",
    "Bonaire, Saint Eustatius and Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Botswana": "BW",
    "Republic of Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos (Keeling) Islands": "CC",
    "DR Congo": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Côte d'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cape Verde": "CV",
    "Country of Curaçao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Spanish Western Sahara": "EH",
    "Eritrea": "ER",
    "Spanish State": "ES",
    "Ethiopia": "ET",
    "Europe": "EU",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands": "FK",
    "Federated States of Micronesia": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "U.K": "GB",
    "United Kingdom": "GB",
    "Grenada": "GD",
    "Georgian Soviet Socialist Republic": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Spanish Guinea": "GQ",
    "Greece": "GR",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "Iraq": "IQ",
    "Empire of Iran": "IR",
    "Iceland": "IS",
    "Republic of Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Democratic Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "St. Kitts & Nevis": "KN",
    "North Korea": "KP",
    "South Korea": "KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Laos": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuanian Soviet Socialist Republic": "LT",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Socialist People’s Libyan Arab Jamahiriya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova": "MD",
    "Socialist Republic of Montenegro": "ME",
    "St. Martin (French Part)": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "Peoples Republic of Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolian People’s Republic": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Republic of Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "United Mexican States": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Republic of Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "St. Pierre & Miquelon": "PM",
    "Pitcairn Islands": "PN",
    "Commonwealth of Puerto Rico": "PR",
    "Palestinian Territory (the Occupied)": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russian Federation": "RU",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "Republic of South Sudan": "SS",
    "São Tomé & Príncipe": "ST",
    "El Salvador": "SV",
    "Country of Sint Maarten": "SX",
    "Syria": "SY",
    "Swaziland": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "East Timor": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad & Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan": "TW",
    "Tanzania": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "U.S. Outlying Islands": "UM",
    "United States": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vatican City": "VA",
    "St. Vincent & Grenadines": "VC",
    "United States of Venezuela": "VE",
    "British Virgin Islands": "VG",
    "U.S. Virgin Islands": "VI",
    "Vietnam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Republic of Kosovo": "XK",
    "Yemen": "YE",
    "Mayotte": "YT",
    "Union of South Africa": "ZA",
    "Northern Rhodesia": "ZM",
    "Zimbabwe": "ZW"
}

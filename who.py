import re
import subprocess
import string
from itertools import permutations, combinations, combinations_with_replacement

c = combinations_with_replacement(string.ascii_lowercase + '-', 3)
free_domains = []
list = ['cc', 'us', 'vc', 'io', 'co', 'me', 'im']  # 'de','li','cs','be','pl']
the_list = re.compile(r'registrar|Expiry Date|Creation Date', flags=re.IGNORECASE)
count = 0
for x in c:
    domainname = ''.join(x)
    a, b, c = x
    if a == '-' or c == '-':
        continue
    for domain in list:
        fulldomainname = domainname + '.' + domain
        print(f'checkdomainname: {fulldomainname}')
        d = subprocess.run(['whois', fulldomainname], stdout=subprocess.PIPE)
        output = str(d.stdout)
        if the_list.findall(output) == []:
            # if output.find('Expiry Date') == -1 and output.find('Creation Date') == -1 and the_list.findall(output) == []:
            print(d.stdout)
            print(fulldomainname)
            # print(d.stdout)
            free_domains.append(fulldomainname + '\n')
            count += 1
        if count == 5:
            with open('free_domains.lst', 'a+') as f:
                f.writelines(free_domains)
            free_domains = []
            count = 0
#ya = subprocess.run(['whois', 'aaa.cc'], stdout=subprocess.PIPE)
print(ya.stdout)
print(str(ya.stdout).find('Expiry Date'))
# b'% IANA WHOIS server\n% for more information on IANA, visit http://www.iana.org\n% This query returned 1 object\n\nrefer:        ccwhois.verisign-grs.com\n\ndomain:       CC\n\norganisation: eNIC Cocos (Keeling) Islands Pty.\norganisation: Ltd. d/b/a Island Internet Services\naddress:      Level 10, 5 Queens Road\naddress:      Melbourne Victoria 3004\naddress:      Australia\n\ncontact:      administrative\nname:         Mario West, Managing Director\norganisation: eNIC Cocos (Keeling) Islands Pty.\norganisation: Ltd. d/b/a Island Internet Services\naddress:      c/o Verisign Internet Services\naddress:      Level 10, 5 Queens Road\naddress:      Melbourne Victoria 3004\naddress:      Australia\nphone:        +613 9926 6700\nfax-no:       +613 9926 6788\ne-mail:       cc-administration@verisign.com\n\ncontact:      technical\nname:         Registry Customer Service\norganisation: VeriSign Global Registry Services\naddress:      12061 Bluemont Way\naddress:      Reston Virginia 20190\naddress:      United States\nphone:        +1 703 925-6999\nfax-no:       +1 703 948 3978\ne-mail:       info@verisign-grs.com\n\nnserver:      AC1.NSTLD.COM 192.42.173.30 2001:500:120:0:0:0:0:30\nnserver:      AC2.NSTLD.COM 192.42.174.30 2001:500:121:0:0:0:0:30\nnserver:      AC3.NSTLD.COM 192.42.175.30 2001:500:122:0:0:0:0:30\nnserver:      AC4.NSTLD.COM 192.42.176.30 2001:500:123:0:0:0:0:30\nds-rdata:     519 8 1 7285EF05E1B4E679D4F072EEA9B00953E01F3AE2\nds-rdata:     519 8 2 E1EC6495ABD34562E6F433DEE201E6C6A52CB10AF69C04D675DA692D2D566897\n\nwhois:        ccwhois.verisign-grs.com\n\nstatus:       ACTIVE\nremarks:      Registration information: http://www.nic.cc/\n\ncreated:      1997-10-13\nchanged:      2016-04-26\nsource:       IANA\n\n# ccwhois.verisign-grs.com\n\n   Domain Name: AAA.CC\r\n   Registry Domain ID: 86888386_DOMAIN_CC-VRSN\r\n   Registrar WHOIS Server: whois.godaddy.com\r\n   Registrar URL: http://www.godaddy.com\r\n   Updated Date: 2020-03-08T14:42:02Z\r\n   Creation Date: 2005-12-01T09:02:02Z\r\n   Registry Expiry Date: 2026-12-01T09:02:02Z\r\n   Registrar: GoDaddy.com, LLC\r\n   Registrar IANA ID: 146\r\n   Registrar Abuse Contact Email: abuse@godaddy.com\r\n   Registrar Abuse Contact Phone: 480-624-2505\r\n   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\r\n   Domain Status: clientRenewProhibited https://icann.org/epp#clientRenewProhibited\r\n   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\r\n   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\r\n   Name Server: V1.DNS.COM\r\n   Name Server: V2.DNS.COM\r\n   DNSSEC: unsigned\r\n   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\r\n>>> Last update of WHOIS database: 2020-08-31T08:23:37Z <<<\r\n\n# whois.godaddy.com\n\nDomain Name: aaa.cc\r\nRegistry Domain ID: 86888386_DOMAIN_CC-VRSN\r\nRegistrar WHOIS Server: whois.godaddy.com\r\nRegistrar URL: http://www.godaddy.com\r\nUpdated Date: 2020-03-08T09:41:59Z\r\nCreation Date: 2005-12-01T04:02:02Z\r\nRegistrar Registration Expiration Date: 2026-12-01T04:02:02Z\r\nRegistrar: GoDaddy.com, LLC\r\nRegistrar IANA ID: 146\r\nRegistrar Abuse Contact Email: abuse@godaddy.com\r\nRegistrar Abuse Contact Phone: +1.4806242505\r\nDomain Status: clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited\r\nDomain Status: clientUpdateProhibited http://www.icann.org/epp#clientUpdateProhibited\r\nDomain Status: clientRenewProhibited http://www.icann.org/epp#clientRenewProhibited\r\nDomain Status: clientDeleteProhibited http://www.icann.org/epp#clientDeleteProhibited\r\nRegistry Registrant ID: Not Available From Registry\r\nRegistrant Name: Registration Private\r\nRegistrant Organization: Domains By Proxy, LLC\r\nRegistrant Street: DomainsByProxy.com\r\nRegistrant Street: 14455 N. Hayden Road\r\nRegistrant City: Scottsdale\r\nRegistrant State/Province: Arizona\r\nRegistrant Postal Code: 85260\r\nRegistrant Country: US\r\nRegistrant Phone: +1.4806242599\r\nRegistrant Phone Ext: \r\nRegistrant Fax: +1.4806242598\r\nRegistrant Fax Ext: \r\nRegistrant Email: aaa.cc@domainsbyproxy.com\r\nRegistry Admin ID: Not Available From Registry\r\nAdmin Name: Registration Private\r\nAdmin Organization: Domains By Proxy, LLC\r\nAdmin Street: DomainsByProxy.com\r\nAdmin Street: 14455 N. Hayden Road\r\nAdmin City: Scottsdale\r\nAdmin State/Province: Arizona\r\nAdmin Postal Code: 85260\r\nAdmin Country: US\r\nAdmin Phone: +1.4806242599\r\nAdmin Phone Ext: \r\nAdmin Fax: +1.4806242598\r\nAdmin Fax Ext: \r\nAdmin Email: aaa.cc@domainsbyproxy.com\r\nRegistry Tech ID: Not Available From Registry\r\nTech Name: Registration Private\r\nTech Organization: Domains By Proxy, LLC\r\nTech Street: DomainsByProxy.com\r\nTech Street: 14455 N. Hayden Road\r\nTech City: Scottsdale\r\nTech State/Province: Arizona\r\nTech Postal Code: 85260\r\nTech Country: US\r\nTech Phone: +1.4806242599\r\nTech Phone Ext: \r\nTech Fax: +1.4806242598\r\nTech Fax Ext: \r\nTech Email: aaa.cc@domainsbyproxy.com\r\nName Server: V1.DNS.COM\r\nName Server: V2.DNS.COM\r\nDNSSEC: unsigned\r\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\r\n>>> Last update of WHOIS database: 2020-08-31T08:00:00Z <<<\r\n\n'

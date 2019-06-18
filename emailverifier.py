import re
import smtplib
import dns.resolver

fromAddress = 'panurag247365@gmail.com'
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

def verify(addressToVerify):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 6
    resolver.lifetime = 6
    match = re.match(regex, addressToVerify)
    if match == None:
	    print('Bad Syntax')
	    return
    else:
        splitAddress = addressToVerify.split('@')
        domain = str(splitAddress[1])
        print('Domain:', domain)
        try:
            records = dns.resolver.query(domain, 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)
            server = smtplib.SMTP()
            server.set_debuglevel(0)
            server.connect(mxRecord)
            server.helo(server.local_hostname) 
            server.mail(fromAddress)
            code, message = server.rcpt(str(addressToVerify))
            server.quit()
        except:
            return
    if code == 250:
	    return True
    else:
	    return False

from twisted.internet import reactor
from twisted.words.protocols.jabber.jid import JID
from wokkel.client import XMPPClient


from echo import Echo
from roster import Roster

with open('account', 'r') as f:
    account = f.readlines()

jid = JID(account[0].rstrip('\n'))
password = account[1].rstrip('\n')

client = XMPPClient(jid, password)

echo = Echo()
roster = Roster()

roster.setHandlerParent(client)
echo.setHandlerParent(client)

client.startService()
reactor.run()

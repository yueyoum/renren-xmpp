from twisted.words.xish import domish

from wokkel.xmppim import MessageProtocol, AvailablePresence

class Echo(MessageProtocol):
    def connectionMade(self):
        self.send(AvailablePresence())
        print "connected"

    def connectionLost(self, reason):
        print "disconnected"

    def onMessage(self, msg):
        print "onMessage"
        print msg.toXml()

        reply = domish.Element((None, "message"))
        reply['to'] = msg['from']
        reply['type'] = 'chat'
        reply.addElement("body", content='echo: %s' % unicode(msg.body))

        self.send(reply)

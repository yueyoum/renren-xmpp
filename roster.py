from wokkel.xmppim import RosterClientProtocol

class Roster(RosterClientProtocol):
    def showRoster(self, roster):
        for jid, item in roster.iteritems():
            print '%s %s' % (jid, item.name or '')

    def err(self, *args):
        print 'getRoster error'

    def connectionInitialized(self):
        super(Roster, self).connectionInitialized()
        d = self.getRoster()
        d.addCallback(self.showRoster)
        d.addErrback(self.err)

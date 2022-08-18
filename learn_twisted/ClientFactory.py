from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout

class Echo(Protocol):
    def dataReceived(self, data: bytes):
        stdout.write(data)

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')
    
    def buildProtocol(self, addr):
        print('Connected.')
        return Echo()
    
    def clientConnectionLost(self, connector, reason):
        print('Lost connection. Reason: ', reason)
    
    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason: ', reason)


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.connectTCP('guold-blog.cn', 80, EchoClientFactory())
    reactor.run()
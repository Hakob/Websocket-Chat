from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory


class MyServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf8')))

        if payload.decode('utf8') == 'start':
            print(payload.decode('utf8').upper() + ' was successfully derived!!!')

        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

    def onPing(self, payload):
        pass


if __name__ == "__main__":
    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)
    factory = WebSocketServerFactory(u"ws://127.0.0.1:3000")
    factory.protocol = MyServerProtocol

    reactor.listenTCP(3000, factory)
    reactor.run()

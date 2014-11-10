from Yowsup.layers import YowLayer, YowLayerEvent, YowProtocolLayer
from .protocolentities import AckProtocolEntity
class YowAckProtocolLayer(YowProtocolLayer):
    def __init__(self):
        handleMap = {
            "ack": (self.recvAckNode, self.sendAckEntity)
        }
        super(YowAckProtocolLayer, self).__init__(handleMap)

    def __str__(self):
        return "Ack Layer"

    def sendAckEntity(self, entity):
        self.entityToLower(entity)

    def recvAckNode(self, node):
        self.toUpper(IncomingAckProtocolEntity.fromProtocolTreeNode(node))

    def sendMessageEntity(self, entity):
        if entity.getType() == "text":
            self.entityToLower(entity)

    ###recieved node handlers handlers
    def recvMessageNode(self, node):
        if node.getAttributeValue("type") == "text":
            entity = TextMessageProtocolEntity.fromProtocolTreeNode(node)
            self.toUpper(entity) 


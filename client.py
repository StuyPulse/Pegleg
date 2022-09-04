import threading
from networktables import NetworkTables


cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='127.0.0.1')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")

pegleg = NetworkTables.getTable("pegleg")

while True:
    pegleg.putNumber("horizontal-angle-error", 6.94)
    pegleg.putNumber("vertical-angle-error", 6.94)

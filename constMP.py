#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['44.220.2.241','44.206.203.140','54.88.55.186','107.23.70.91','3.232.114.77','54.163.114.25']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['44.220.2.241','44.206.203.140','54.88.55.186','107.23.70.91','52.89.31.9','52.35.213.24']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='44.220.2.241'
SERVER_PORT = 5678


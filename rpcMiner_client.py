import xmlrpc.client
import sys

# usage python .\rpcCalc_client.py localhost 8000
 
# Calcula total de argumentos
n = len(sys.argv)
 
# Verificação do uso correto/argumentos
if (n!=3):
    print("\nUso correto: rpcCalc_client server_address port_number.\n")
    exit(-1)

rpcServerAddr = "http://" + sys.argv[1] + ":" + sys.argv[2] + "/"
proxy = xmlrpc.client.ServerProxy(rpcServerAddr)

transID = proxy.getTransactionID()
print(transID)

chall = proxy.getChallenge(0)
print(chall)

transStatus = proxy.getTransactionStatus(0)
print(transStatus)

""" winner = proxy.getWinner(0)
print(winner) """

seed = proxy.getSeed(0)
print(seed)
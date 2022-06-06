from xmlrpc.server import SimpleXMLRPCServer

# Identificador da transação, representada por um valor inteiro (32 bits). Use valores incrementais começando em 0 (zero);
# Valor do desafio criptográfico associado à transação, representado por um número [1..128], onde 1 é o desafio mais fácil.
# String que, se aplicada a função de hashing SHA-1, solucionará o desafio criptográfico proposto;
# ClientID do usuário que solucionou o desafio criptográfico para a referida TransactionID (mesma linha da tabela).

table = [
     { "transactionID": 0, "challenge": 0, "seed" : "", "winner": -1 },
 ]
print(table[0]["transactionID"])

def validTransactionID(transactionID: int) -> bool:
    return table[transactionID]["transactionID"] >= len(table)

def getTransactionID() -> int:
    return table[-1]["transactionID"]

def getChallenge(transactionID: int) -> int:
    if (validTransactionID(transactionID)):
        return table[0]
    else:
        return -1

def getTransactionStatus(transactionID: int) -> int:
    if (validTransactionID(transactionID)):
        return 0
    elif (transactionID < len(table) - 1): # pendente
        return 1
    else:
        return -1
    

def submitChallenge(transactionID: int, clientID: int, seed: int):
    return 0

def getWinner(transactionID: int):
        transaction = table[transactionID]
        print(transaction)
        if transaction is None:
            return -1
        if (transaction["seed"] is None):
            return 0
        return transaction["winner"]

def getSeed(transactionID: int) -> int:
    transaction = table[transactionID]
    print(transaction)
    if transaction is not None:
        return transaction["seed"]

# A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(getTransactionID, 'getTransactionID')
server.register_function(getChallenge, 'getChallenge')
server.register_function(getTransactionStatus, 'getTransactionStatus')
# server.register_function(submitChallenge, 'submitChallenge')
server.register_function(getWinner, 'getWinner')
server.register_function(getSeed, 'getSeed') 

server.serve_forever()

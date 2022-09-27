from abc import abstractmethod
import threading
import socket



clients = [] # DEVERIA SER QUEUE => SQS or MQ

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('Não foi possível iniciar o servidor')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread = threading.Thread(target=httpRequest, args=[client])
        thread.start()



def httpTreatment(request):
    """ Tratar o request e chamar o send command
        >> send_command_to_device()

        return:
            device_id, cmd_type
    """
    pass

def send_command_to_device(device_id: str, client_id: int):
    """ Tem a responsabilidade traduzir para o epacket

        Parameters:
            device_id: str
            cmd_type: str

        return:
            hex com single location
    """
    pass


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client) # SQS or RabbitMQ 

main()
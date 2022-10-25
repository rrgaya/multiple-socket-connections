# Multi Socket's

Projeto consiste em 3 camadas, a primeira é um device/sensor que envia um hex via socket para um server. O server hoje tem a
responsabilidade de receber esse hex, converter e chamar o método. Após ter "traduzido" o hex, o server enviar o data para um App mobile.

> O app mobile tbm faz solicitações para o server pedindo a localização do device/sensor. # Ainda em dev


Código criado apenas com fins educacionais

```mermaid
    sequenceDiagram
    participant DeviceGSM
    participant Server
    participant Mobile
    Note left of DeviceGSM: DeviceGSM IoT
    DeviceGSM-->>Server: Socket Connection
    DeviceGSM->>+Server: Send []bytes
    Server-->>-Mobile: Send data
    Server-->>Mobile: Send data []bytes 
    Mobile->>Server: [GET] Request >> Send device_ID 
    Note right of Mobile: App Mobile solicitando alguma info.
    Server-->>DeviceGSM: Send command
```


## TODO's

- [x] Server
- [x] Client
- [x] Broadcast
- [ ] Handler para http protocol



```mermaid
    sequenceDiagram
    participant Client
    participant OAM
    participant API_AQ
    participant Database
    participant Domain

    Client-->>OAM: Lorem
    API_AQ-->>OAM: Lorem
    API_AQ-->>Domain: Lorem
```

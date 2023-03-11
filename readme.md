## What is API? 
API stands for Application Programming Interface. It is a set of functions and procedures that allow the creation of applications that access the features or data of an operating system, application, or other service.
**example** *(resturant)*:
- You order food from the menu.
- The waiter takes your order to the kitchen.
- The chef prepares your order.
- The waiter brings your food to your table.
- You eat your food.
- You pay the bill.
- The Waiter act as API between you and the kitchen.

```mermaid 
sequenceDiagram
autonumber
actor A as You 
participant  B as Waiter 
participant D as Kitchen    
A->>B: Order food from menu
note right of B: Waiter act as API
B->>D: Take order to the kitchen  
B->>A: Bring food to your table
A->>B: Pay the bill
```
## What is REST?
REST stands for REpresentational State Transfer. It is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server.

## What is REST API?
```mermaid 
graph LR
A((Client))--request--> B(API)
X((client))--request-->B(API)
B-->C[web application]
C-->D[(database)]
D --> C
C -- response --> B
B -- response --> A
B -- response --> X
```
REST API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data.

```mermaid 
graph TD
A[Client] --> B[Server]
B --> C{Request}
C -->|GET| D[Retrieve data]
C -->|POST| E[Create data]
C -->|PUT| F[Update data]
C -->|DELETE| G[Delete data]
```


## Go to [docs](./docs/basic.md)  learn more about Django REST framework 



       



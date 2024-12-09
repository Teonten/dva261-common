### **File Structure for Each Raspberry Pi**


#### **CTRL Raspberry Pi (Control Unit)**

This will serve as the **central API** server. All other Raspberry Pis communicate with this server.

```
/ctrl-api
  ├── /app
  │    ├── __init__.py       # Initialize Flask app
  │    ├── routes.py         # API endpoints (heartbeat, actuation, logging)
  │    ├── auth.py           # Authentication for nodes (API keys)
  │    ├── utils.py          # Helper functions (e.g., time sync, validation)
  ├── /config
  │    ├── settings.py       # App settings (host, port, API keys)
  │    ├── tls_config.py     # TLS configuration (certs and keys)
  ├── /certs
  │    ├── ca.pem            # CA certificate for verifying nodes
  │    ├── server.crt        # CTRL server's public certificate
  │    ├── server.key        # CTRL server's private key
  ├── /logs
  │    ├── ctrl.log          # Logs from the CTRL server
  ├── app.py                 # Entry point for the API
  ├── requirements.txt       # Dependencies for Python
```

#### **LOCK Raspberry Pi**

The **LOCK** node handles locking/unlocking and communicates with CTRL.

```
/lock-node
  ├── /app
  │    ├── __init__.py       # Initialize the app
  │    ├── client.py         # Sends heartbeat and receives lock/unlock commands
  │    ├── actuators.py      # Controls the lock actuator
  │    ├── utils.py          # Helper functions (e.g., validate responses)
  ├── /config
  │    ├── settings.py       # Node-specific settings (API key, CTRL host)
  │    ├── tls_config.py     # TLS configuration (certs and keys)
  ├── /certs
  │    ├── ca.pem            # CA certificate for verifying CTRL
  │    ├── lock.crt          # LOCK node's public certificate
  │    ├── lock.key          # LOCK node's private key
  ├── /logs
  │    ├── lock.log          # Logs for the LOCK node
  ├── app.py                 # Entry point for the LOCK node
  ├── requirements.txt       # Dependencies for Python
```

#### **ULTRAIN Raspberry Pi**

The **ULTRAIN** node handles an ultrasonic sensor and a buzzer.

```
/ultrain-node
  ├── /app
  │    ├── __init__.py       # Initialize the app
  │    ├── client.py         # Sends heartbeat and ultrasonic data
  │    ├── sensors.py        # Reads ultrasonic sensor data
  │    ├── actuators.py      # Controls the buzzer
  │    ├── utils.py          # Helper functions (e.g., validate responses)
  ├── /config
  │    ├── settings.py       # Node-specific settings (API key, CTRL host)
  │    ├── tls_config.py     # TLS configuration (certs and keys)
  ├── /certs
  │    ├── ca.pem            # CA certificate for verifying CTRL
  │    ├── ultrain.crt       # ULTRAIN node's public certificate
  │    ├── ultrain.key       # ULTRAIN node's private key
  ├── /logs
  │    ├── ultrain.log       # Logs for the ULTRAIN node
  ├── app.py                 # Entry point for the ULTRAIN node
  ├── requirements.txt       # Dependencies for Python
```

#### **ULTRAUT Raspberry Pi**

The **ULTRAUT** node handles an ultrasonic sensor and multiple LEDs.

```
/ultraut-node
  ├── /app
  │    ├── __init__.py       # Initialize the app
  │    ├── client.py         # Sends heartbeat and ultrasonic data
  │    ├── sensors.py        # Reads ultrasonic sensor data
  │    ├── actuators.py      # Controls LEDs
  │    ├── utils.py          # Helper functions (e.g., validate responses)
  ├── /config
  │    ├── settings.py       # Node-specific settings (API key, CTRL host)
  │    ├── tls_config.py     # TLS configuration (certs and keys)
  ├── /certs
  │    ├── ca.pem            # CA certificate for verifying CTRL
  │    ├── ultraut.crt       # ULTRAUT node's public certificate
  │    ├── ultraut.key       # ULTRAUT node's private key
  ├── /logs
  │    ├── ultraut.log       # Logs for the ULTRAUT node
  ├── app.py                 # Entry point for the ULTRAUT node
  ├── requirements.txt       # Dependencies for Python
```
## for the git commands
```txt
git status
(stage all changes)
git add -A
git add 'Playing around'
git commit -m ""
git push origin main
git pull origin main

```
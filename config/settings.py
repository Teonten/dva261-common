# Node Configuration
CTRL_HOST = "10.42.0.1"
CTRL_PORT = 443
HOSTNAME = "ultraut"
HOST_IP = "10.132.136.7"
HOST_PORT = 2443

# API Key for Node
API_KEY = "key_" + HOSTNAME

NODE_CONF = {
    "ctrl_host": CTRL_HOST,
    "ctrl_port": CTRL_PORT,
    "hostname": HOSTNAME,
    "host_ip": HOST_IP,
    "host_port": HOST_PORT

}

# Define node communication time synchronization
SYNC_HB_DELAY = 0.05
ACK_TIMEOUT = 1
MAX_RETRIES = 2
RETRY_DELAY = 1

COM_INT = {
    "next": 300.0,                    # ctrl schedules next heartbeat 
    "heartbeat": SYNC_HB_DELAY,     # delay from start of window until heartbeat
    "ack_timeout": ACK_TIMEOUT,     # timeout til for waiting for acknowledgement
    "max_retries": MAX_RETRIES,     # max number of communication retries
    "retry_delay": RETRY_DELAY      # delay between retries
}


# Define actuator GPIO pins
BUZZER = 27
RED_LED = 10
GREEN_LED = 17
YELLOW_LED = 18
ACTUATOR = {    
    "buzzer": 27,         # GPIO27
    "red_led": 10,        # GPIO10
    "green_led": 17,      # GPIO17
    "yellow_led": 18      # GPIO18
}

# Defining sensor GPIO pins
BUTTON_GPIO = 25       # GPIO25

#Define ultrasonic communcation:
ECHO = 17
TRIGGER = 4
MAX_DISTANCE = 1.0
THRESHOLD_DISTANCE = 0.5
QUEUE_LEN = 3

ULTRASONIC = {
'echo': ECHO,
'trigger': TRIGGER,
'max_distance': MAX_DISTANCE,
'threshold_distance': THRESHOLD_DISTANCE,
'queue_len': QUEUE_LEN
}


SENSORS = {
    "button": BUTTON_GPIO,
    "ultrasonic": ULTRASONIC 
}





# In-memory node status
NODE_STATUS = { # will be set on a per node basis with install.bash 
    "previous": None,
    "door_lock": {"lock": False, "last_stamp": None},
    "heartbeat": None,
    "time_delta": None,
}

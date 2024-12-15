import gpiozero

# Node Configuration
CTRL_HOST = "172.23.19.1" #"10.42.0.1"
CTRL_PORT = 443
HOSTNAME = "ultraut"
HOST_IP = "172.23.19.4" #"10.42.0.151" #"10.132.136.7"
HOST_PORT = 2443

# for testing:
#CTRL_HOST = "192.168.0.5" #"172.23.19.1"
#CTRL_PORT = 443
#HOSTNAME = "ultraut"
#HOST_IP = "192.168.0.4" #"10.132.136.7"
#HOST_PORT = 2443



# API Key for Node
API_KEY = "key_" + HOSTNAME
CTRL_KEY = "key_ctrl"

NODE_CONF = {
    "ctrl_host": CTRL_HOST,
    "ctrl_port": CTRL_PORT,
    "hostname": HOSTNAME,
    "host_ip": HOST_IP,
    "host_port": HOST_PORT,
    "api_key": API_KEY,
    "ctrl_key": CTRL_KEY
}

# Define node communication time synchronization
SYNC_HB_DELAY = 0.05
ACK_TIMEOUT = 1
MAX_RETRIES = 20000 ### changed to 20000
RETRY_DELAY = 1

COM_INT = {
    "next": None,                    # ctrl schedules next heartbeat 
    "heartbeat": SYNC_HB_DELAY,     # delay from start of window until heartbeat
    "ack_timeout": ACK_TIMEOUT,     # timeout til for waiting for acknowledgement
    "max_retries": MAX_RETRIES,     # max number of communication retries
    "retry_delay": RETRY_DELAY      # delay between retries
}

#Define ultrasonic communcation:
ULTRASONIC = gpiozero.DistanceSensor(echo=17,trigger=4,max_distance=1.0,threshold_distance=0.5,queue_len=3)
YELLOW_LED = gpiozero.OutputDevice(22, active_high=True, initial_value=False)
RED_LED = gpiozero.OutputDevice(23, active_high=True, initial_value=False)
GREEN_LED = gpiozero.OutputDevice(24, active_high=True, initial_value=False)
BUTTON = gpiozero.Button(27, active_state=None, pull_up=False, bounce_time=0.02)

# In-memory node status
NODE_STATUS = {
    "hostname": HOSTNAME,
    "next": None,
    "button": False,
    "yellow_led": False,
    "red_led": True,
    "green_led": None,
    "ultrasonic": False,
    "door_lock": {
        "lock": False,
        "last_stamp": None
    },
}

from config.settings import GREEN_LED, YELLOW_LED, RED_LED, NODE_STATUS

def actuator_function(action):

    YELLOW_LED.on()

    if action == 'door':

        if NODE_STATUS['door_lock']['lock']:
            RED_LED.on()
            GREEN_LED.off()

        elif NODE_STATUS['door_lock']['lock']:
            RED_LED.off()
            GREEN_LED.on()

    YELLOW_LED.off()
    pass
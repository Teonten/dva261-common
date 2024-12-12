import config.settings
import app.utils

def button_pressed():
    # timer för button och lampa om inget ack
    # Logging DEBUG
    app.utils.logging.info(f"Button pressed")
    if not config.settings.NODE_STATUS['button']:
        # Turn on yellow LED
        config.settings.YELLOW_LED.on()
        # Updating status
        config.settings.NODE_STATUS['button'] = True
        config.settings.NODE_STATUS['yellow_led'] = True

        # Logging DEBUG
        app.utils.logging.info(f"Yellow LED on.")

        # Notify CTRL-node
        ack = app.client.communicate(action='update')

    if ack is not None:
        print(ack)
        # Turn on yellow LED
        config.settings.YELLOW_LED.off()
        # Updating status
        config.settings.NODE_STATUS['yellow_led'] = False
        config.settings.NODE_STATUS['button'] = False


  
def ultra_in():

    # Logging DEBUG
    app.utils.logging.info(f"Ultrasonic OUT")

    # Updating status
    config.settings.NODE_STATUS['yellow_led'] = True

    # Notify CTRL-node
    app.client.communicate(action='update')

    #TODO tidsblock på knapptryckning igen

def ultra_out():

        # Logging DEBUG
        app.utils.logging.info(f"Ultrasonic IN")

        # Updating status
        config.settings.NODE_STATUS['ultrasonic'] = False

        # Notify CTRL-node
        app.client.communicate(action='update')

        #TODO tidsblock på knapptryckning igen
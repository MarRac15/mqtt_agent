import ast
#translates model data from TTS to kafka

def convert_message(mqtt_message: str):

    try:
        if not mqtt_message:
            return None
                
        mqtt_message = ast.literal_eval(mqtt_message)
        old_message = mqtt_message.copy()
        old_message.pop("ID")
        new_msg_values = list(old_message.values())
        kafka_message = {mqtt_message["ID"]: new_msg_values}

        return kafka_message
    
    except Exception as e:
        
        print(f"Error while converting the message: {e}")
        return None
        

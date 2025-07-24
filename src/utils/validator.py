from models.lora_model import VALID_LABELS, REQUIRED_LABELS
import ast

def is_valid_message(mqtt_message: str):
    
    try:

        mqtt_message = ast.literal_eval(mqtt_message)
        incoming_keys = set(mqtt_message.keys())
        
        #temporary mapper:
        label_mapper = {"T": "MD", "F": "P"}
        mapped_message = {}
        for key, value in mqtt_message.items():
            new_key = label_mapper.get(key, key)
            mapped_message[new_key] = value
        mqtt_message = mapped_message

        # owner set to PCSS on default:
        mqtt_message.update({'O': 'PCSS'})
        
        # label validation:
        unknown_labels = incoming_keys - VALID_LABELS

        #check if there are all required fields (id, date, owner):
        msg_keys = mqtt_message.keys()
        for label in REQUIRED_LABELS:
            if label not in msg_keys:
                print("Message doesnt have all the obligatory fields, so it won't be sent.")
                return False

        if unknown_labels :
            print("Detected unknown labels in the message, so it won't be sent.")
            return False
        
        return True
    
    except Exception:
        print("Error with the message format")
        return False

    
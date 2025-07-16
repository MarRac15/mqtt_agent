from models.lora_model import VALID_LABELS
import ast

def is_valid_message(mqtt_message: str):

    mqtt_message = ast.literal_eval(mqtt_message)
    incoming_keys = set(mqtt_message.keys())
    unknown_labels = incoming_keys - VALID_LABELS
    
    if unknown_labels :
        print("Detected unknown labels in the message")
        return False

    return True
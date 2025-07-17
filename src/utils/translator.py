import ast
from models.lora_model import FIELD_ALIASES
#translates model data from TTS to kafka


def convert_message(mqtt_message: str):

    try:
        if not mqtt_message:
            return None
        
        mqtt_message = ast.literal_eval(mqtt_message)
        
        mapped_message = {
            FIELD_ALIASES[key]: value for key, value in mqtt_message.items() if key in FIELD_ALIASES
        }

        return mapped_message
    
    except Exception as e:

        print(f"Error while converting the message: {e}")
        return None




    


        

import json

def save_message(Status:str):
    with open('msg_data.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(Status)
        #json.dump(Status, ensure_ascii=True, indent=4, fp=file)
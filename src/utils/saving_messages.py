

def save_message(Status: dict):
    with open('msg_data.txt', 'r') as file:
        #change keys
        file.write(str(Status["T"] + " "))
        file.write(str(Status["P"] + " "))
        file.write(str(Status["F"] + " "))


def save_message(Status: str, file_name: str):

    # clear the file when reached the limit:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > 500:
            open(file_name, 'w').close()

    #save a message
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(Status+'\n')

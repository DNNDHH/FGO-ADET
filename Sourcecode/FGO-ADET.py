import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import os
import sys
import base64
from Crypto.Cipher import DES3
import json
import time

sys.stdout = sys.__stdout__ 

font = ('宋体', 10) 
root = tk.Tk()
root.title("FGO-AEDT")
root.geometry("270x180")

script_dir = os.path.dirname(os.path.abspath(__file__)) 

background_image = PhotoImage(file="b.png")  
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

def remove_hex_prefix(filename, prefix):
    with open(filename, 'rb') as file:
        data = file.read()
        
    hex_prefix = bytes.fromhex(prefix)
    if hex_prefix in data:
        index = data.index(hex_prefix)
        data = data[index:]

    with open(filename, 'wb') as file:
        file.write(data)

def run_main_py():
    try:
        remove_hex_prefix("54cc790bf952ea710ed7e8be08049531", "5A53762F")
        time.sleep(0.2)

        with open("54cc790bf952ea710ed7e8be08049531", "r") as file:
            YourCertificate = file.read().strip()

        CertByte = base64.b64decode(YourCertificate)

        bytes1 = "b5nHjsMrqaeNliSs3jyOzgpD".encode('utf-8')
        bytes2 = "wuD6keVr".encode('utf-8')

        des3 = DES3.new(bytes1, DES3.MODE_CBC, bytes2)

        decrypted_bytes = des3.decrypt(CertByte)

        decrypted_text = decrypted_bytes.decode('utf-8')

        data_to_save = decrypted_text

        with open("Decrypt_Server_Key.json", "w") as json_file:
            json.dump(data_to_save, json_file)

        messagebox.showinfo("Decrypted（成功）", "Decrypted account data is saved in a Decrypt_Server_Key.json file \n（解密的账户数据保存在 Decrypt_Server_Key.json 文件中）")

    except Exception as e:

        messagebox.showerror("ERROR 错误", f"\n(确保你的54cc790bf952ea710ed7e8be08049531在当前目录下)\n")

    with open("Decrypt_Server_Key.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

        decrypted_data = data
        if decrypted_data is not None:

            cleaned_decrypted_data = decrypted_data.replace("\u0007", "")

            try:

                decrypted_data_dict = json.loads(cleaned_decrypted_data)

                auth_key = decrypted_data_dict.get("authKey")
                secret_key = decrypted_data_dict.get("secretKey")
                user_id = decrypted_data_dict.get("userId")

                if user_id is not None:
                    user_id_str = user_id 
                else:
                    user_id_str = ""

                if auth_key is not None:
                    auth_key_str = auth_key 
                else:
                    auth_key_str = ""

                if secret_key is not None:
                    secret_key_str = secret_key 
                else:
                    secret_key_str = ""

                with open("authKey.txt", "w", encoding='utf-8') as auth_file:
                    auth_file.write(auth_key_str)

                with open("secretKey.txt", "w", encoding='utf-8') as secret_file:
                    secret_file.write(secret_key_str)

                with open("userId.txt", "w", encoding='utf-8') as user_file:
                    user_file.write(user_id_str)
                    
                messagebox.showinfo("Parsing method 1 successfu ", "账号密钥已分别保存到 authKey.txt secretKey.txt userId.txt 文件中 \nThe account key has been saved to the authKey.txt secretKey.txt userId.txt file")

            except json.JSONDecodeError as e:
                messagebox.showinfo("Parsing method 1 failed_Using method 2", "账号密钥已分别保存到 authKey.txt secretKey.txt userId.txt 文件中 \nThe account key has been saved to the authKey.txt secretKey.txt userId.txt file")

                with open("Decrypt_Server_Key.json", "r", encoding='utf-8') as json_file:
                    data = json.load(json_file)

                decrypted_data = data
                if decrypted_data is not None:
                    cleaned_decrypted_data = decrypted_data.replace("\b", "")

                    decrypted_data_dict = json.loads(cleaned_decrypted_data)

                    auth_key = decrypted_data_dict.get("authKey")
                    secret_key = decrypted_data_dict.get("secretKey")
                    user_id = decrypted_data_dict.get("userId")

                    if user_id is not None:
                        user_id_str = user_id 
                    else:
                        user_id_str = ""

                    if auth_key is not None:
                        auth_key_str = auth_key 
                    else:
                        auth_key_str = ""

                    if secret_key is not None:
                        secret_key_str = secret_key 
                    else:
                        secret_key_str = ""

                    with open("authKey.txt", "w", encoding='utf-8') as auth_file:
                        auth_file.write(auth_key_str)

                    with open("secretKey.txt", "w", encoding='utf-8') as secret_file:
                        secret_file.write(secret_key_str)

                    with open("userId.txt", "w", encoding='utf-8') as user_file:
                        user_file.write(user_id_str)

def extract_and_save_keys(json_filepath):
    with open(json_filepath, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    decrypted_data = data
    if decrypted_data is not None:
        cleaned_decrypted_data = decrypted_data.replace("\u0007", "")

        try:
            decrypted_data_dict = json.loads(cleaned_decrypted_data)

            auth_key = decrypted_data_dict.get("authKey")
            secret_key = decrypted_data_dict.get("secretKey")
            user_id = decrypted_data_dict.get("userId")

            user_id_str = user_id + "," if user_id is not None else ""
            auth_key_str = auth_key + "," if auth_key is not None else ""
            secret_key_str = secret_key + "," if secret_key is not None else ""

            with open("batch_authKey.txt", "a", encoding='utf-8') as auth_file:
                auth_file.write(auth_key_str)

            with open("batch_secretKey.txt", "a", encoding='utf-8') as secret_file:
                secret_file.write(secret_key_str)

            with open("batch_userId.txt", "a", encoding='utf-8') as user_file:
                user_file.write(user_id_str)

        except json.JSONDecodeError as e:

            with open(json_filepath, "r", encoding='utf-8') as json_file:
                data = json.load(json_file)

            decrypted_data = data
            if decrypted_data is not None:

                cleaned_decrypted_data = decrypted_data.replace("\b", "")

                decrypted_data_dict = json.loads(cleaned_decrypted_data)

                auth_key = decrypted_data_dict.get("authKey")
                secret_key = decrypted_data_dict.get("secretKey")
                user_id = decrypted_data_dict.get("userId")

                user_id_str = user_id + "," if user_id is not None else ""
                auth_key_str = auth_key + "," if auth_key is not None else ""
                secret_key_str = secret_key + "," if secret_key is not None else ""

                with open("batch_authKey.txt", "a", encoding='utf-8') as auth_file:
                    auth_file.write(auth_key_str)

                with open("batch_secretKey.txt", "a", encoding='utf-8') as secret_file:
                    secret_file.write(secret_key_str)

                with open("batch_userId.txt", "a", encoding='utf-8') as user_file:
                    user_file.write(user_id_str)

def run_main2_py():
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

    for folder in folders:
        filepath = os.path.join(folder, "54cc790bf952ea710ed7e8be08049531")
            
        if os.path.exists(filepath):
            remove_hex_prefix(filepath, "5A53762F")

            with open(filepath, "r") as file:
                YourCertificate = file.read().strip()

            CertByte = base64.b64decode(YourCertificate)
            bytes1 = "b5nHjsMrqaeNliSs3jyOzgpD".encode('utf-8')
            bytes2 = "wuD6keVr".encode('utf-8')
            des3 = DES3.new(bytes1, DES3.MODE_CBC, bytes2)
            decrypted_bytes = des3.decrypt(CertByte)
            decrypted_text = decrypted_bytes.decode('utf-8')
            data_to_save = decrypted_text
            json_filepath = os.path.join(folder, "Decrypt_Server_Key.json")

            with open(json_filepath, "w") as json_file:
                json.dump(data_to_save, json_file)

        json_filepath_s = os.path.join(folder, "Decrypt_Server_Key.json")

        if os.path.exists(json_filepath_s):
            extract_and_save_keys(json_filepath_s)


def ddd():
    with open("userId.txt", 'r', encoding='utf-8') as a_file:
        userId = a_file.read().strip()

    with open("authKey.txt", 'r', encoding='utf-8') as b_file:
        authKey = b_file.read().strip()

    with open("secretKey.txt", 'r', encoding='utf-8') as c_file:
        secretKey = c_file.read().strip()

    text2 = f"""{{"SaveDataVer":"Fgo_20150511_1","userCreateServer":"game.fate-go.jp/","userId":"{userId}","authKey":"{authKey}","secretKey":"{secretKey}"}}\b\b\b\b\b\b\b\b"""

    text_bytes = text2.encode('utf-8')

    bytes1 = "b5nHjsMrqaeNliSs3jyOzgpD".encode('utf-8')
    bytes2 = "wuD6keVr".encode('utf-8')

    des3 = DES3.new(bytes1, DES3.MODE_CBC, bytes2)

    encrypted_bytes = des3.encrypt(text_bytes)

    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')

    encrypted_text_with_question = encrypted_text

    encrypted_bytes_with_question = encrypted_text_with_question.encode('utf-8')

    hex_prefix = bytes.fromhex("F801")
    encrypted_bytes_with_question = hex_prefix + encrypted_bytes_with_question

    folder_path = "com.aniplex.fategrandorder/files/data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, "54cc790bf952ea710ed7e8be08049531")
    with open(file_path, "wb") as file:
        file.write(encrypted_bytes_with_question)

    file_path = os.path.join(folder_path, "969b46577f365fadeb79ef14cf5d6370")
    with open(file_path, "wb") as file:
        file.write(encrypted_bytes_with_question)

def ddd2():
    with open("userId.txt", 'r', encoding='utf-8') as a_file:
        userId = a_file.read().strip()

    with open("authKey.txt", 'r', encoding='utf-8') as b_file:
        authKey = b_file.read().strip()

    with open("secretKey.txt", 'r', encoding='utf-8') as c_file:
        secretKey = c_file.read().strip()

    text = f"""{{"SaveDataVer":"Fgo_20150511_1","userCreateServer":"game.fate-go.jp/","userId":"{userId}","authKey":"{authKey}","secretKey":"{secretKey}"}}\u0007\u0007\u0007\u0007\u0007\u0007\u0007"""

    text_bytes = text.encode('utf-8')

    bytes1 = "b5nHjsMrqaeNliSs3jyOzgpD".encode('utf-8')
    bytes2 = "wuD6keVr".encode('utf-8')

    des3 = DES3.new(bytes1, DES3.MODE_CBC, bytes2)

    encrypted_bytes = des3.encrypt(text_bytes)

    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')

    encrypted_text_with_question = encrypted_text

    encrypted_bytes_with_question = encrypted_text_with_question.encode('utf-8')

    hex_prefix = bytes.fromhex("F801")
    encrypted_bytes_with_question = hex_prefix + encrypted_bytes_with_question

    folder_path = "com.aniplex.fategrandorder/files/data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, "54cc790bf952ea710ed7e8be08049531")
    with open(file_path, "wb") as file:
        file.write(encrypted_bytes_with_question)

    file_path = os.path.join(folder_path, "969b46577f365fadeb79ef14cf5d6370")
    with open(file_path, "wb") as file:
        file.write(encrypted_bytes_with_question)

button1 = tk.Button(root, text=u"Decrypt (解密) ", command=run_main_py, font=font, bg="#ffc0cb")
button1.pack()

button11 = tk.Button(root, text=u"Batch Decrypt (批量解密)", command=run_main2_py, font=font, bg="#ffc0cb")
button11.pack()

button2 = tk.Button(root, text="Encryption mode o（加密模式o）", command=ddd, font=font, bg="#ffc0cb")
button2.pack()

button3 = tk.Button(root, text="Encryption mode s（加密模式s）", command=ddd2, font=font, bg="#ffc0cb")
button3.pack()

button1.place(relx=0.5, rely=0.2, anchor="center")
button11.place(relx=0.5, rely=0.4, anchor="center")
button2.place(relx=0.5, rely=0.6, anchor="center")
button3.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()

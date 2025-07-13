from flask import Flask, render_template, request

import random
import string

app = Flask(__name__)

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")

def get_key(seed):
    key = chars.copy()
    random.seed(seed)
    random.shuffle(key)
    return key

def encrypt_message(message, seed):
    key = get_key(seed)
    encrypted = ""
    for letter in message:
        if letter in chars:
            index = chars.index(letter)
            encrypted += key[index]
        else:
            encrypted += letter
    return encrypted

def decrypt_message(message, seed):
    key = get_key(seed)
    decrypted = ""
    for letter in message:
        if letter in key:
            index = key.index(letter)
            decrypted += chars[index]
        else:
            decrypted += letter
    return decrypted

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form.get("message")
        seed = request.form.get("seed")
        action = request.form.get("action")
        
        if action == "encrypt":
            result = encrypt_message(message, seed)
        elif action == "decrypt":
            result = decrypt_message(message, seed)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

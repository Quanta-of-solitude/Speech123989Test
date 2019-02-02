import speech_recognition as sr
import json

#Speech Recognition , just a base for a new project yet to be, NOT INCLUDING COMMENTS IN THIS ONE
__author__= "Nyzex"


class Tree:

    def recognizer():

        r = sr.Recognizer()
        file = open("config.json")
        file = file.read()
        index_data = json.loads(file)
        if index_data["device ID"] == "10000":
            print("Do  you know your device ID? if no, type no, else Enter")
            choice = str(input(">")).lower()
            if choice == "no":
                mic = sr.Microphone.list_microphone_names()
                c = 0
                print("\n")
                for x in mic:
                    print(str(c) + ". {}".format(x))
                    c +=1

                print("\n\nThe index starts from 0, your device ID is the number at which your device name is starting from 0\n\nNow,\n")

                print("Enter your input device ID: ")
                index_id = input(">")
                print("\nYou selected your device ID: {}\nYou can later modify it in config.json!".format(index_id))
                index_data["device ID"] = index_id
                index_data = json.dumps(index_data)
                file = open("config.json", "w")
                file = file.write(index_data)
            else:
                print("Enter your input device ID: ")
                index_id = input(">")
                index_data["device ID"] = index_id
                index_data = json.dumps(index_data)
                file = open("config.json", "w")
                file = file.write(index_data)
        else:
            index_id = index_data["device ID"]
        print("Listening to your query...")

        mic = sr.Microphone(device_index=int(index_id))

        with mic as source:
            audio = r.listen(source)

        query = r.recognize_wit(audio, key="KEY")
        return query


#we get what we said as text

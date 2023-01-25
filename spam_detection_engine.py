import pickle
import sys

file = str(sys.argv[1])
email = open(file, "r")
email_content = email.read()

loaded_model = pickle.load(open("lr_spam_detection_model.sav", 'rb'))
result = loaded_model.predict([email_content])

if result[0] == 1:
    print("spam")
else:
    print("ham")
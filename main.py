from uci1 import app
while True:
    user=input("Enter you query:")
    if user=='q':
        break
    else:
        app.invoke({"messages":[user]})
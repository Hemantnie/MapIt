import sys,webbrowser,pyperclip

city_name = ""
print(len(sys.argv))
if len(sys.argv) > 1:
    city_name = sys.argv[1]
else:
    city_name = pyperclip.paste()

city_name = "https://www.google.com/search?q=weather+in+{}".format(city_name)
webbrowser.open(city_name)
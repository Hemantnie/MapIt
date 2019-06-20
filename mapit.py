import webbrowser,sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    address.replace(',','');
    address = "www.google.com/maps/place/{}/".format(address.replace(' ','+'))
    print(address)
    webbrowser.open(address)
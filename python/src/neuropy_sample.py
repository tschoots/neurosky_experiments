from NeuroPy import NeuroPy


def attention_callback(attention_value):
    print(attention_value)
    return None


def main():
    print ("hallo hallo")

    object1 = NeuroPy("/dev/rfcomm0")

    object1.setCallBack("attention", attention_callback)

    object1.start()

    while True:
        if (object1.meditation>70):
            object1.stop()




if __name__ == "__main__":
    main()
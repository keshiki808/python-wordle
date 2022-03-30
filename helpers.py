from random import choice
def read_word_list(txt_file):
    try:
        with open(txt_file, mode="r") as file:
            lines = file.readlines()
            return choice(lines)
    except FileNotFoundError:
        print(f"FileNotFoundError: The file {txt_file} could not be found")
        quit()
    except OSError as e:
        print("OSError:", e)
        quit()
    except Exception as e:
        print(type(e), e)
        quit()

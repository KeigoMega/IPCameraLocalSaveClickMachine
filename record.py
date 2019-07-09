#record.py

import windows_control
from time import sleep

def main():
    while True:
        sleep(0.5)
        parent = windows_control.get_parent_handle('ローカル保存')
        if parent != 0:
            print('detect parent!')
            child = windows_control.get_child_handles(parent)
            if len(child) != 0:
                print('detect child!')
                windows_control.lbutton_down(child[0])
                sleep(0.5)
                windows_control.lbutton_up(child[0])

if __name__ == '__main__':
    main()

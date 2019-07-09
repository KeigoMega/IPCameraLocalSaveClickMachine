#windows_control.py

import ctypes
import array
import win32con
from time import sleep

WM_CHAR = win32con.WM_CHAR
BM_CLICK = win32con.BM_CLICK
BM_SETSTATE = win32con.BM_SETSTATE
BM_SETCHECK = win32con.BM_SETCHECK
WM_CLOSE = win32con.WM_CLOSE
WM_COMMAND = win32con.WM_COMMAND
WM_SETFOCUS = win32con.WM_SETFOCUS
WM_KILLFOCUS = win32con.WM_KILLFOCUS
WM_KEYDOWN = win32con.WM_KEYDOWN
WM_KEYUP = win32con.WM_KEYUP
WM_LBUTTON_DOWN = win32con.WM_LBUTTONDOWN
WM_LBUTTON_UP = win32con.WM_LBUTTONUP

def close_window(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_CLOSE, 1, 0)

def get_parent_handle(window_name):
    handle = ctypes.windll.user32.FindWindowW(0, window_name)
    return handle

def enum_child_windows_proc(handle, list):
    list.append(handle)
    return 1

def convert_path_to_keymap(filepath):
    path_ascii = []
    for strs in filepath:
        path_ascii.append(ord(strs))
    return path_ascii

def make_folder_path(filepath):
    return filepath[0: filepath.rfind('\\')]

def focus_wm(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_SETFOCUS, 0, 0)

def kill_focus_wm(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_KILLFOCUS, 0, 0)

def insert_paths(handle, path_ascii):
    focus_wm(handle)
    sleep(0.5)
    for charac in path_ascii:
        ctypes.windll.user32.SendMessageW(handle, WM_CHAR, charac, 0)

def click_btn(handle):
    ctypes.windll.user32.SendMessageW(handle, BM_CLICK, 0, 0)

def command(handle, num):
    ctypes.windll.user32.SendMessageW(handle, WM_COMMAND, num, 0)

def set_state(handle, torf):
    ctypes.windll.user32.SendMessageW(handle, BM_SETSTATE, torf, 0)

def set_check(handle, torf):
    ctypes.windll.user32.SendMessageW(handle, win32con.BM_SETCHECK, 0, 0)

def lbutton_down(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_LBUTTON_DOWN, 0, 0)

def lbutton_up(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_LBUTTON_UP, 0, 0)

def key_down(handle, code):
    ctypes.windll.user32.SendMessageW(handle, WM_KEYDOWN, code, 0)

def key_up(handle):
    ctypes.windll.user32.SendMessageW(handle, WM_KEYUP, 0, 0)

def get_child_handles(parent_handle):
    child_handle_list = array.array('i')
    ENUM_CHILD_WINDOWS = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.py_object)
    ctypes.windll.user32.EnumChildWindows(parent_handle, ENUM_CHILD_WINDOWS(enum_child_windows_proc), ctypes.py_object(child_handle_list))
    return child_handle_list

if __name__ == '__main__':
    print('Don\'t use this for Standalone')
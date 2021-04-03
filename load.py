from tkinter import Frame, Label, Entry, Checkbutton, NSEW, EW,IntVar, StringVar
from irc import client
import myNotebook as nb
from theme import theme

def plugin_start3(plugin_dir:str):
    """Code executed to start the plugin"""
    
    return "Elite Coordinator"

def plugin_prefs(parent: nb.Notebook, cmdr: str, is_beta:bool):
    """ Prepares a list of plugin configuration settings to connect to the IRC server with"""
    frame = nb.Frame(parent)

    ServerName = StringVar()
    Label(frame, text = "Server Name", textvariable = ServerName).grid(row = 0, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 0, column = 1, sticky = NSEW)

    PortNumber = StringVar()
    Label(frame, text = "Port", textvariable = PortNumber).grid(row = 1, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 1, column = 1, sticky = NSEW)

    ServerAddress = StringVar()
    Label(frame, text = "Server Address", textvariable = ServerAddress).grid(row = 2, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 2, column = 1, sticky = NSEW)

    Nick = StringVar()
    Label(frame, text = "Nick", textvariable = Nick).grid(row = 3, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 1, column = 3, sticky = NSEW)

    Username = StringVar()
    Label(frame, text = "Username", textvariable = Username).grid(row = 4, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 1, column = 4, sticky = NSEW)

    Password = StringVar()
    Label(frame, text = "Password", show = "*", textvariable = Password).grid(row = 5, column = 0, sticky = NSEW)
    Entry(frame).grid(row = 1, column = 5, sticky = NSEW)

    SSL = IntVar()
    Checkbutton(frame, text = "SSL", variable = SSL).grid(row = 6, column = 0, columnspan = 2, sticky = NSEW)

    return frame

def prefs_changed(cmdr: str, is_beta:bool):
    raise NotImplementedError

def plugin_app(parent:Frame):
    frame = Frame(parent)

    serverNameLabel = Label(frame)
    serverNameLabel.grid(row = 0, column = 0, sticky = EW)

    currentCase = Label(frame)
    currentCase.grid(row = 1, column = 0, sticky = EW)

    return frame

def plugin_stop():
    pass
    # Close the IRC connection
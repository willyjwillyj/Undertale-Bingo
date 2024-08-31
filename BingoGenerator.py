import tkinter as tk
import bingo as bingo
import requests
import webbrowser  


root = tk.Tk()
root.title("Undertale Bingo Generator")
root.geometry("400x400")

def genBoard():
    genOutput.delete("1.0",tk.END)
    genOutput.insert(tk.END, bingo.genProcess())

current_version = "v1.0.2"
github_connection_success = False
newest_version = current_version

try:
    release_data = requests.get("https://api.github.com/repos/willyjwillyj/Undertale-Bingo/releases/latest")
    newest_version = (release_data.json()["name"])
except:
    pass
else:
    github_connection_success = True
    

ver_label = tk.Label(master=root, text="You are using version " + current_version)
ver_label.grid(row=0,column=0)

if github_connection_success:
    if newest_version == current_version:
        ver_label_success = tk.Label(master=root, text="You are on the latest version")
        ver_label_success.grid(row=0,column=1)
    else:
        ver_label_failure = tk.Button(master=root, text="Update to the latest version", command=lambda:webbrowser.open("https://github.com/willyjwillyj/Undertale-Bingo/releases", new=0, autoraise=True))
        ver_label_failure.grid(row=0,column=1)
else:
    ver_label_failure = tk.Label(master=root, text="Failed to discover latest version")
    ver_label_failure.grid(row=0,column=1)


if bingo.filename_error:
    errorLabel = tk.Label(master=root, text="Goals List not present.\nPlease make sure you have a goals.txt\nIn the same folder as this program\nThen restart the program")
    errorLabel.grid(row=1,column=0)
else:
    genButton = tk.Button(master=root, text="Generate Bingo Board", command=genBoard)
    genOutput = tk.Text(master=root, width=40, height=20)
    genButton.grid(row=1,column=0)
    genOutput.grid(row=2,column=0, columnspan=2)

root.mainloop()
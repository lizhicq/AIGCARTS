import requests
from tkinter import Tk, Label, Button, Entry, messagebox
from PIL import Image, ImageTk
from io import BytesIO

# 设置API密钥
API_KEY = 'wAnuGRsDgloyh9l0LYskg49Gh_27wwUpNYgisX9GZn4'

def search_unsplash(query, page=1, per_page=10):
    base_url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {API_KEY}"
    }
    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def display_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def search_and_display():
    query = entry.get()
    results = search_unsplash(query)

    if results['results']:
        first_photo_url = results['results'][0]['urls']['small']
        display_image(first_photo_url)
    else:
        messagebox.showinfo("Info", "No results found!")

# GUI
root = Tk()
root.title("Unsplash Image Search")

Label(root, text="Enter your query:").pack(pady=10)
entry = Entry(root)
entry.pack(pady=10)
Button(root, text="Search", command=search_and_display).pack(pady=10)
label = Label(root)
label.pack(pady=10)

root.mainloop()

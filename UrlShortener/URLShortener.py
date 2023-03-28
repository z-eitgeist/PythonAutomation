from tkinter import *
import pyshorteners
import clipboard
 
window = Tk()

# Set default window size
window.geometry("420x270")
window.resizable(False, False) # Not resizable

window.title("URL Shortner") # App name

# URL entry
url_input = Entry(window, font = ("Roboto", 16))
url_input.grid(row = 1, column = 2, pady = 16, padx = 90)

#Label shortened url
str_url = StringVar(window)

shortned_url = Label(window, textvariable = str_url, font = ("Roboto", 16), fg = "#ffffff", bg = "#1abc9c") 
shortned_url.grid(row = 3, column = 2, pady = 16, padx = 16)

# Copy short url function
def copy_short_url():
	try: 
		clipboard.copy(str_url.get())
		print("Url copied.")
	except:
		str_url.set("Please try again.") 


# Copy URL button 
copy_btn = Button(window, text = "Copy", bg = "#34495e", fg = "#ffffff", font = ("Roboto", 16), command = copy_short_url)
copy_btn.grid(row = 4, column = 2, pady = 6, padx = 10)


# Short URL function
def short_url():
	try:
		s = pyshorteners.Shortener()
		url = url_input.get()
		final_result = s.tinyurl.short(url)
		str_url.set(final_result)
		url_input.delete(0, END) #clear input
	except:
		str_url.set("Invalid URL.")

# Click button to short URL
btn = Button(window, text ="Short URL", padx = 8, pady = 4, bg = "#2ecc71", fg = "#ffffff", font = ("Roboto", 16), activebackground = "#16a085", command=short_url)
btn.grid(row = 2, column = 2, pady = 2)

window.mainloop()

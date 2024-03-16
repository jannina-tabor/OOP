import pyfiglet 

name = input ("Please enter your name: ")
dream_job = input("Please enter your dream job: ")

font_name = pyfiglet.Figlet(font='js_block_letters')
font_dream_job = pyfiglet.Figlet(font='slant')

# ANSI color codes for pink and cyan 
pink_color = '\033[95m'
cyan_color = '\033[36m'

colored_name = f"{pink_color}{font_name.renderText(name)}"
colored_dream_job = f"{cyan_color}{font_name.renderText(dream_job)}"

print ("Here's your name and dream job: ")
print (colored_name)
print ("=======================================================================")
print (colored_dream_job)
print ("Thank you for using this program!")
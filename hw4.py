user_file=  input("enter the file name:")

def checking (give):
    if give.endswith(".png"):
        print("successfully uploadedd the image!")
    elif  give.endswith(".jpeg"):
        print("successfully uploadedd the jpeg image!")  
    elif  give.endswith(".png"):
        print("successfully uploadedd the png image!")  
    elif  give.endswith(".mp4"):
        print("successfully uploadedd the video!")    
    else:
        print("file not supported")      

checking(user_file) 



sent = input("enter text with a gap after . :")
def capitlize_sentence (text):
    sent_list=(text.split("."))

    length = len(sent_list)
    for i in range(length):
        sent_list[i]= sent_list[i].lstrip(" ").capitalize()
    
    cap_text = (". ").join(sent_list)
    print(cap_text)
    

capitlize_sentence(sent)

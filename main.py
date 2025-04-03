import os
import pwinput
from PyPDF2 import PdfReader, PdfWriter


def banner():
    ascii_art = r"""
    ____  ____  ______   _____ ______________  ______  ____________  __
   / __ \/ __ \/ ____/  / ___// ____/ ____/ / / / __ \/  _/_  __/\ \/ /
  / /_/ / / / / /_      \__ \/ __/ / /   / / / / /_/ // /  / /    \  / 
 / ____/ /_/ / __/     ___/ / /___/ /___/ /_/ / _, _// /  / /     / /  
/_/   /_____/_/       /____/_____/\____/\____/_/ |_/___/ /_/     /_/                                                                       
    """
    print(ascii_art)


def start():
    ori_path = input("Enter the pdf file path or drag and drop here to encrypt: ").strip(" '\"")

    if len(ori_path) == 0:
        os.system('cls')
        start()

    if os.path.isfile(ori_path) and ori_path.lower().endswith(".pdf"):
        os.system('cls')
        print(rf"Your original pdf file path is {ori_path}")
        basename = os.path.splitext(os.path.basename(ori_path))[0]  # get name file
        current_path = os.getcwd()
        pdfWriter = PdfWriter()
        pdf = PdfReader(rf"{ori_path}")

        index = 1
        while True:
            filename = fr"{basename}({index}).pdf"
            file_path = os.path.join(current_path, filename)
            if not os.path.exists(file_path):
                break
            index += 1

        for i in range(len(pdf.pages)):
            pdfWriter.add_page(pdf.pages[i])  # copy to a new pdf
        password = pwinput.pwinput(prompt='Enter your password: ')
        pdfWriter.encrypt(password)

        with open(file_path, "wb") as f:
            pdfWriter.write(f)
        print("Loading...")
        if os.path.exists(file_path):
            print(f"\033[92mYour encrypted file: {file_path}\033[92m\033[96m\033[0m")
            print("\033[92mEncrypt successfully!!!\033[92m\033[96m\033[0m")

    else:
        print("\033[91mYou entered an invalid path or not exists!\033[91m\033[0m")
        start()
    start()
if  __name__ == "__main__":
    banner()
    start()
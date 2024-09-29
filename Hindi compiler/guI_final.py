functions = []

with open('functions.txt', 'r',encoding='utf-8') as function:
    fun = function.readlines()

for line in fun:
    line = line.strip()
    functions.append(line)

# functions

types = []

with open('type.txt', 'r',encoding='utf-8') as typee:
    fun = typee.readlines()

for line in fun:
    line = line.strip()
    types.append(line)

# types

header=[]
with open('header.txt','r',encoding='utf-8') as head:
    fun = head.readlines()

for line in fun:
    line.strip()
    header.append(line)

import tkinter as tk
from tkinter import messagebox

h_code = []

def execute_code():
    text = text_entry.get("1.0", "end-1c")  # Retrieve text from the text entry widget
    text = text.strip()
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    h_code.extend(lines)

    header_line = []
    typ = tuple(types)

    for line in h_code:
        if not line.startswith(typ):
            header_line.append(line)
        else:
            break

    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)

    for head in header_line:
        if not head.startswith('#'):
            messagebox.showerror('Error',"गलत शीर्षक फ़ाइल")
            exit()


    header_divided = []

    for head in header_line:
        head = head.split()
        header_divided.append(head)


    for i in range(len(header_divided)):
        # print(header_divided[i][0])
        if header_divided[i][0] != '#शामिल' and header_divided[i][0] != '#परिभाषित':
            messagebox.showerror('Error',"अमान्य राखीव_शब्द")
            exit()
            
    flag_check = 0   
    for i in range(len(header_divided)):
        if header_divided[i][0] == '#शामिल':
            flag_check = 0 
            for head in header:
                if header_divided[i][1] == head:
                    flag_check = 1
                    break

    if flag_check == 0:
        messagebox.showerror('Error',"गलत शीर्षक फ़ाइल")
        exit()

    for i in range(len(header_divided)):
        if header_divided[i][0] == '#परिभाषित':
            if len(header_divided[i]) != 3:
                messagebox.showerror('Error',"गलत #परिभाषित")
                exit()
            
    ad_h_code = []

    for line in h_code:
        if not line.startswith('#'):
            ad_h_code.append(line.split())

    print(ad_h_code)


    # checking for main function
    flag_check = 0

    for ty in types:
        if ad_h_code[0][0] == ty:
            flag_check = 1
            break

    if flag_check == 0:
        messagebox.showerror('Error',"गलत वापस प्रकार")
        exit()

    if flag_check == 1:
        if ad_h_code[0][1] != 'मुख्य()':
            messagebox.showerror('Error',"मुख्य कार्य नहीं है")
            exit()

    ad_h_code = ad_h_code[1:]

    # for brackets
    with open('input.c', 'r',encoding='utf-8') as file:
        content = file.read()
        if (content.count('(') != content.count(')')) or content.count('{') != content.count('}'):
            messagebox.showerror('Error',"ब्रैकेट लापता")
            exit()
        
    ad_h_code = ad_h_code[1:]
    ad_h_code = ad_h_code[:-1]
    ad_h_code

    for line in ad_h_code:
        if not line[-1].endswith(';'):
            messagebox.showerror('Error',"; लापता")
            exit()
        
    symbol=[]
    for line in ad_h_code:
        if line[0] in types:
            for i in range(len(line)-1):
                symbol.append([line[0],line[i+1][:-1]])

    ad_h_code=ad_h_code[2:]

    i=0
    for line in ad_h_code:
        if '=' in line:
            symbol[i].append(line[-1][:-1])
            i=i+1
        
    #checking for datatypes
    for line in symbol:
        if line[0]=='इंट' and '.' in line[2]:
            messagebox.showerror('Error',"अमान्य पूर्णांक")
            exit()
        elif line[0]=='फ्लोट' and '.' not in line[2]:
            messagebox.showerror('Error',"अमान्य दशमलव")
            exit()
    
    with open('symbol_table.txt', 'w',encoding='utf-8') as output_file:
        for line in symbol: 
                output_file.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
 
    letters=[]
    for line in ad_h_code:
        if line[0]=='लिखो':
            if line[1][1]=='"':
                output_text.insert(tk.END,line[1][2:-3])
                output_text.insert(tk.END,'\n')
            else:
                str = line[1][1:-2]
                # print(str)
                for letter in str:
                    letters.append(letter)
                
                # print(letters)
                
                # finding values of variables
                values=[letters[0],letters[2]]

                column_mapping = {row[1]: row[2] for row in symbol }

                third_column=[column_mapping[value] for value in values]
                
                #arithmetic operation
                if letters[1] == '+':
                    print('hi')
                    output_text.insert(tk.END,letters[0]+' + '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0])+int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '-':
                    output_text.insert(tk.END,letters[0]+' - '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0])-int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '*':
                    output_text.insert(tk.END,letters[0]+' * '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0])*int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '/':
                    output_text.insert(tk.END,letters[0]+' / '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0])/int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '&':
                    output_text.insert(tk.END,letters[0]+' & '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0]) & int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '|':
                    output_text.insert(tk.END,letters[0]+' | '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0]) | int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                elif letters[1] == '^':
                    output_text.insert(tk.END,letters[0]+' ^ '+letters[2]+' :')
                    output_text.insert(tk.END,int(third_column[0]) ^ int(third_column[1]))
                    output_text.insert(tk.END,'\n')
                letters.clear()


    output_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("हिन्दी संकलक")
root.configure(bg='darkgray')

# Text Entry
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Run Button
run_button = tk.Button(root, text="संकलित करें", command=execute_code)
run_button.pack()

output_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack()

root.mainloop()




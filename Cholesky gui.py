from math import sqrt
import tkinter as tk
import customtkinter
import numpy as np
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window 
app.geometry("400x240")
#______________________________________________
error = customtkinter.CTk()
error.title('Error')
error.geometry("400x240")
#_____________________________________________
vectorpage = customtkinter.CTk()
vectorpage.title('vector')
#_____________________________________________
matrixpage = customtkinter.CTk()
matrixpage.title('matrix elements')
#_____________________________________________
resultpage = customtkinter.CTk()
resultpage.title('result')

#_______________________global variable_________________________________
matrix_entries = []
matrix = []
vector = []
vector_entries = []

#_____________________________________________________________________________
def button_function():
    cols = int(entryrow.get())
    rows = int(entrycols.get())
    if cols != rows :
        errorlabel = customtkinter.CTkLabel(master=error, text="please enter the square matrix")
        errorlabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        app.destroy()
        error.mainloop()
    else : 
        def R_CALCULATE(A):
            n = len(A)
            # Create zero matrix for R
            r = [[0.0] * n for i in range(n)]
             # Perform the Cholesky decomposition
            for i in range(n):
                for k in range(i+1):
                    tmp_sum = sum(r[i][j] * r[k][j] for j in range(k))
                    if (i == k): 
                        r[i][k] = sqrt(A[i][i] - tmp_sum)
                    else:
                        r[i][k] = (1.0 / r[k][k] * (A[i][k] - tmp_sum))
            return r
        def R_INVERSE_CALCULATE(A):
            r_inverse =[[0.0] * len(A) for i in range(len(A))]
            for i in range (len(A)):
                for j in range (len(A)):
                    if i == j :
                        r_inverse[i][j]= A[i][j]
                    else :
                        r_inverse [i][j] = A[j][i]
            return r_inverse
        def front_substitution(A ,b):
            y = []
            for i in range (len (A)):
                y.append(0.0)
            for i in range(len(A)):
                y[i] = b[i]
                for j in range(i):
                    y[i] -=(A[i][j] * y[j] )
                y[i] /= A[i][i]
            return y
        def back_substitution(A, b):
            n = len(b)
            x = [0] * n
            x[n-1] = b[n-1] / A[n-1][n-1]
            for i in range(n-2, -1, -1):
                sum = 0
                for j in range(i+1, n):
                    sum += A[i][j] * x[j]
                x[i] = (b[i] - sum) / A[i][i]
            return x
# _____________________________last page_________________________________________
        def cal_page():
            vectorpage.destroy()
            print(matrix)
            print(vector)
            r_matrix =R_CALCULATE(matrix)
            print(r_matrix)
            r_inverse_matrix=R_INVERSE_CALCULATE(r_matrix)
            print(r_inverse_matrix)
            y =front_substitution(r_matrix,vector)
            print(y)
            final = back_substitution(r_inverse_matrix ,y)
            print (final)
            for i in range (len(final)):
                label = customtkinter.CTkLabel(master=resultpage, text=f'x{i+1} = {final[i]}')
                label.grid(row=4, column=i, padx=5, pady=5)
            for i in range (len(r_matrix)):
                for j in range(len(r_matrix)):
                    label_matrix = customtkinter.CTkLabel(master=resultpage, text=f'{r_matrix[i][j]}')
                    label_matrix.grid(row=i+10, column=j, padx=5, pady=5)
            #________________________________________________________________________________
            label1 = customtkinter.CTkLabel(master=resultpage, text=' x :',text_color='red')
            label1.grid(row=1, column=1, padx=5, pady=5)
            label2 = customtkinter.CTkLabel(master=resultpage, text=f'R matrix :' ,text_color='red')
            label2.grid(row=7, column=1, padx=5, pady=5)

            app.destroy()
            resultpage.mainloop()
            
#_________________________vector page_______________________________________________________
        def add_vector():
            global vector_entries  # Declare vector_entries as global
            for i in range(cols):
                element = int(vector_entries[i].get())
                vector.append(element)
            cal_page()
        # _______________________ gui elements of vector__________________________________
        def vector_page():
            global vector_entries  # Declare vector_entries as global
            vector_entries = []
            for j in range(cols):
                vectorelement = customtkinter.CTkEntry(vectorpage, width=45)
                vectorelement.grid(row=j, column=0, padx=5, pady=5)
                vector_entries.append(vectorelement)
            calbutton = customtkinter.CTkButton(master=vectorpage, text="Calculate", command=add_vector)
            calbutton.grid(row=rows, columnspan=1, padx=5, pady=10)
            vectorpage.mainloop()
            matrixpage.destroy()

#_______________________ to give array of matrix ____________________________
        def submit_matrix():
            for i in range(rows):
                row = []
                for j in range(cols):
                    element = int(matrix_entries[i][j].get())
                    row.append(element)
                matrix.append(row)
            print("Matrix:", matrix)
            #________________check eigvals >0 ____________________________
            if np.all(np.linalg.eigvals(matrix)>0):
                matrixpage.destroy()
                vector_page()
            #__________________ eigvals<0______________________________________
            else :
                label = customtkinter.CTkLabel(master=error, text="Your matrix not positive definite" )
                label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)     
                app.destroy()
                matrixpage.destroy()
                error.mainloop()
        #_____________________ gui matrix elements ____________________________
        matrix_entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entryelement = customtkinter.CTkEntry(matrixpage, width=45)
                entryelement.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entryelement)
            matrix_entries.append(row_entries)
        nextbutton = customtkinter.CTkButton(master=matrixpage, text="Next", command=submit_matrix)
        nextbutton.grid(row=rows, columnspan=cols, padx=5, pady=5)
        matrixpage.mainloop()




def ok_func():
    exit()

# Use CTkButton instead of tkinter Button
app.title('Cholesky Solver')
label3 = customtkinter.CTkLabel(master=app, text="Welcome to cholesky calculator " ,fg_color='#000094')
label3.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
button = customtkinter.CTkButton(master=app, text="Create matrix", command=button_function)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
rowlabel = customtkinter.CTkLabel(master=app, text="Enter the number of rows: ")
rowlabel.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
entryrow = customtkinter.CTkEntry (master=app)
entryrow.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
colslabel = customtkinter.CTkLabel(master=app, text="Enter the number of cols: ")
colslabel.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
entrycols = customtkinter.CTkEntry (master=app)
entrycols.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
author = customtkinter.CTkLabel(master=app, text="© Powered by: Mmdreza Zaheri " ,text_color='red')
author.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
button = customtkinter.CTkButton(master=error, text="ok", command=ok_func)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


app.mainloop()
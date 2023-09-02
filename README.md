# **Cholesky Decomposition Linear Equation Solver**

**Introduction :**

This Python project offers an efficient Cholesky decomposition method for solving systems of linear equations involving positive definite matrices. It comes with a user-friendly graphical user interface (GUI) to streamline the input process and provide a clear visualization of the results. If you're working with systems of linear equations and positive definite matrices, this tool can be a valuable addition to your toolkit.

**Features :**

- **Intuitive GUI** :  The program uses the customtkinter library to create an intuitive and visually appealing interface.

- **Matrix Input** :  You start by specifying the dimensions of the square matrix 'A' (number of rows and columns), ensuring it's a square matrix.

- **Matrix Elements Input** : Input the elements of matrix 'A' through an easy-to-use grid of input fields. The program validates that the input matrix is indeed positive definite.

- **Vector Input** : Enter the elements of vector 'b' through another grid of input fields. The program ensures that the matrix is positive definite before proceeding.

- **Cholesky Decomposition** : The Cholesky decomposition is calculated for matrix 'A,' resulting in the upper triangular matrix 'R.' Additionally, the inverse of 'R' is computed to assist in solving linear equations.

- **Linear Equation Solving** : The program employs front substitution to solve for 'y' in the equation 'Ry = b' and back substitution to determine the solution vector 'x' in the equation 'Rx = y.'

- **Results Display** : The solutions to the linear equation system are presented in the final GUI window. Both 'x' and the 'R' matrix are displayed for reference.

- **Error Handling** : If the input matrix is not positive definite, an error message is promptly displayed, ensuring the integrity of the calculations.

**Usage**

To utilize this Cholesky decomposition linear equation solver:

1. Clone this GitHub repository to your local machine.

2. Run the Python script provided, and the GUI will guide you through the process of entering your matrix and vector.

3. The program will calculate and display the solutions for your linear equation system.

4. If any errors are encountered during input or calculations, clear error messages will guide you.

**Author :**

This project is developed and maintained by Mmdreza Zaheri.


**Acknowledgments :**

- The customtkinter library is used to enhance the GUI appearance and functionality.

Feel free to contribute to the project or open issues if you encounter any problems. We hope this Cholesky decomposition solver simplifies your work with systems of linear equations and positive definite matrices.

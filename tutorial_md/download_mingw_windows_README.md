# Setup and Use w64devkit for C/C++ Development

This README provides instructions on how to set up and use `w64devkit` for compiling and running C/C++ programs on Windows.

## 1. Download and Extract w64devkit
   ```bash
   https://github.com/skeeto/w64devkit/releases
   ```

1. Download the `w64devkit` pre-build package from the official repository or site (.exe). Check the correct version x86 or x64 for your pc.
2. Extract the contents of the package into a convenient location on your system, for example, `C:\w64devkit`.

## 2. Add w64devkit to System Path

1. Open **System Properties**:
   - Press `Win + Pause`, or search for "System" in the start menu.
   - Click on **Advanced system settings**.

2. Open **Environment Variables**:
   - Click the **Environment Variables** button.

3. Edit **Path**:
   - In **System variables**, find the variable named `Path`, select it, and click **Edit**.
   - Click **New** and add the path where `w64devkit` was extracted, for example:
     ```
     C:\w64devkit\bin
     ```

4. Click **OK** to save and close all dialogs.

## 3. Verify Installation

1. Open **Command Prompt** and type:
   ```bash
   gcc --version
   ```
2. If the installation was successful, it will display the version of GCC installed.

## 4. Compile and Run C Programs

### Example: Hello World in C

1. Create a file named `hello.c` with the following content:
   ```c
   #include <stdio.h>

   int main() {
       printf("Hello, World!\n");
       return 0;
   }
   ```

2. Compile the program using `gcc`:
   ```bash
   gcc hello.c -o hello.exe
   ```

3. Run the program:
   ```bash
   hello.exe
   ```

## 5. Compile and Run C++ Programs

### Example: Hello World in C++

1. Create a file named `hello_world.cpp` with the following content:
   ```cpp
   #include <iostream>

   int main() {
       std::cout << "Hello, World!" << std::endl;
       return 0;
   }
   ```

2. Compile the program using `g++`:
   ```bash
   g++ hello_world.cpp -o hello_world.exe
   ```

3. Run the program:
   ```bash
   hello_world.exe
   ```

## 6. Troubleshooting

- If you encounter `undefined reference` errors when compiling C++ programs, make sure to use `g++` instead of `gcc` to compile.
- After modifying environment variables, make sure to restart your terminal or, in some cases, reboot your system.

Now you are ready to compile and run C/C++ programs using `w64devkit`!

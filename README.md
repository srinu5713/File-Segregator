# File Segregator

File Segregator is a Python-based tool that helps you organize and manage files in a directory by segregating them based on their extensions or types. The application also allows custom segregation rules and collapsing subdirectory files into the main directory.

## Features

- **Segregate Files by Extension**: Automatically move files into folders based on their extensions.
- **Segregate Files by Type**: Select file types (Images, Videos, Audios, Documents, etc.) for segregation.
- **Custom Segregation**: Define custom rules for moving files based on their names or extensions.
- **Collapse Subdirectories**: Move files from subdirectories into the main directory.

## Installation and Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/srinu5713/File-Segregator.git
    cd file-segregator
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the interface script:**
    ```sh
    python interface.py
    ```

    Use the graphical user interface to:
    - Select a directory for file segregation.
    - Choose the desired segregation option (by extension, by type, or custom).
    - View the results and status messages.

## GUI Overview

- **Main Menu**: Choose between different segregation options and collapse subdirectory files.
- **Directory Selection**: Select the directory where the files are located.
- **Segregation Options**:
  - **Segregate by Extension**: Automatically segregate files based on their extensions.
  - **Segregate by Type**: Select specific file types for segregation.
  - **Custom Segregation**: Add custom rules for file segregation.
  - **Collapse Subdirectory Files**: Move files from subdirectories into the main directory.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to explore the code, experiment with different configurations, and contribute to the advancement of file management tools. For any questions or issues, please open an issue in the repository. Thank you for your interest and contributions!

## Acknowledgements

- Tkinter for the GUI components.
- Python's standard library for file operations.
- Watchdog for file system event handling.

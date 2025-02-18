# Python Module Imports with PyInstaller (Generated by IA)

This project is a simple example to understand how Python handles dynamic module imports and how to make them work when packaging the application with PyInstaller.

## 📌 Project Structure

```
/pmip
  ├── __main__.py        # Main entry point
  ├── commands/          # Directory containing commands
  │   ├── __init__.py    # Marks this directory as a package
  │   ├── count.py       # Example command module
  │   ├── add.py         # Example command module
  ├── __main__.spec      # Information about the build
```

## 🚀 How It Works
- `__main__.py` dynamically imports modules from the `commands/` directory.
- PyInstaller requires explicit knowledge of modules at build time, which can cause issues when using `__import__` dynamically.
- We solve this by modifying the `.spec` file to automatically detect and include all modules inside `commands/`.


## 🛠 Building the Project with PyInstaller
To create an executable, you need to use `PyInstaller`.
Instead of manually specifying `--hidden-import` for each module, we use a `.spec` file to handle dynamic imports.

### 1. Generate the `.spec` file
Run:
```bash
pyinstaller --onefile --hidden-import=commands.count __main__.py --name pmip
```
This creates a `__pmip__.spec` file which we will modify.

### 2. Modify `__pmip__.spec`
Edit `__pmip__.spec` to dynamically include all modules in the `commands/` directory:

```python
import os

commands_dir = "commands"
hidden_imports = [
    f"commands.{filename[:-3]}" for filename in os.listdir(commands_dir)
    if filename.endswith(".py") and filename != "__init__.py"
]

a = Analysis(
    hiddenimports=hidden_imports,  # Automatically include all modules from 'commands/'
    ...
)
```

### 3. Build using the `.spec` file
Run:
```bash
pyinstaller __main__.spec
```
This ensures that all modules inside `commands/` are included automatically in the final binary.

## 📄 Running the Executable
Once the build is complete, the executable will be in the `dist/` folder. Run it as follows:

```bash
./dist/__main__
```

## 📝 Notes
- The key to making this work is to structure the project properly as a package (`commands/` with an `__init__.py` file).
- `importlib.import_module("commands.count")` works better than `__import__` when using PyInstaller.
- Always specify hidden imports explicitly if PyInstaller doesn’t detect them automatically.

## 🔗 References
- [Python importlib Documentation](https://docs.python.org/3/library/importlib.html)
- [PyInstaller Documentation](https://pyinstaller.org/)

This project serves as a learning reference for handling dynamic imports when building Python applications with PyInstaller. 🚀
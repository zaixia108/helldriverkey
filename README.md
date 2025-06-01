# Helldriverkey

## 项目简介

Helldriverkey 是一个专为《地狱潜兵2》（Helldivers II）设计的自动召唤战备程序。它能够自动识别用户输入的按键，并自动执行对应的召唤操作，从而大幅提升游戏中的操作效率和便利性，是“潜兵”们的重要辅助工具。


### 功能特色

- 自动识别并模拟召唤战备的按键操作
- 支持自定义热键和召唤配置
- 高度兼容《地狱潜兵2》当前版本
- 轻量化设计，易于安装和使用

### 安装方法

1. 克隆本仓库：
   ```bash
   git clone https://github.com/zaixia108/helldriverkey.git
   ```
2. 进入项目目录并安装依赖：
   ```bash
   cd helldriverkey
   pip install -r requirements.txt
   ```

### 使用方法

直接运行主程序即可启动自动召唤功能：

```bash
python hd.py
```

根据程序界面提示或配置文件自定义按键与召唤内容，具体请参考文档或源码注释。

### 贡献指南

欢迎提交 Issue 或 Pull Request 来改进本项目！请遵循贡献规范。

### 许可证

本项目采用 MIT 许可证，详情请见 LICENSE 文件。

---

#### 编译为可执行文件（exe）

你可以使用 PyInstaller 或 Nuitka 将本程序编译为 Windows 下的独立可执行文件：

**使用 PyInstaller：**
```bash
pip install pyinstaller
pyinstaller -F hd.py
```
编译完成后，`dist` 目录下会生成 `main.exe`，可直接运行。

**使用 Nuitka：**
```bash
pip install nuitka
nuitka --standalone hd.py
```
编译完成后会在当前目录生成可执行文件。

**注意**： 记得把模型文件放到同目录下，或在代码中指定正确的路径。

## Project Introduction (English)

Helldriverkey is a standalone program for Helldivers II that automatically recognizes and simulates key presses to perform stratagem calls, greatly improving operational efficiency and convenience for players.

**Note: This is a complete standalone application, not a Python library. No import required—just run it directly.**

### Features

- Automatically recognizes and simulates stratagem key sequences
- Supports custom hotkeys and stratagem configurations
- Fully compatible with the current version of Helldivers II
- Lightweight and easy to use

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/zaixia108/helldriverkey.git
   ```
2. Enter the project directory and install dependencies:
   ```bash
   cd helldriverkey
   pip install -r requirements.txt
   ```

### Usage

Simply run the main program to start the auto stratagem feature:

```bash
python hd.py
```

Customize hotkeys and stratagems via the program interface or configuration files. See documentation or source code comments for details.

### Contribution

Pull Requests and Issues are welcome! Please follow the contribution guidelines.

### License

This project is licensed under the MIT License. See LICENSE for details.

#### Compile as Executable (exe)

You can use PyInstaller or Nuitka to compile this program into a standalone Windows executable:

**With PyInstaller:**
```bash
pip install pyinstaller
pyinstaller -F hd.py
```
After compiling, `main.exe` will be in the `dist` folder.

**With Nuitka:**
```bash
pip install nuitka
nuitka --standalone hd.py
```
After compiling, the executable will appear in the current directory.

**Note**: Remember to place the model files in the same directory or specify the correct path in the code.
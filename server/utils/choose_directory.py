import subprocess

def choose_directory():
    # AppleScript命令来弹出文件夹选择对话框
    script = """
    tell application "System Events"
        activate
        set theFolder to choose folder with prompt "Please choose a folder:"
        POSIX path of theFolder
    end tell
    """
    
    # 使用osascript运行AppleScript命令
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    # 返回选择的文件夹路径
    if process.returncode == 0:
        return out.strip().decode('utf-8')
    else:
        raise Exception(f"Error: {err.decode('utf-8')}")

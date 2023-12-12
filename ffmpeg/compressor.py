import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout

class VideoCompressorApp(QWidget):
    def __init__(self):
        super(VideoCompressorApp, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建按钮
        self.selectFolderButton = QPushButton('选择要压缩的文件夹', self)
        self.selectFolderButton.clicked.connect(self.showFolderDialog)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.selectFolderButton)

        # 设置布局
        self.setLayout(vbox)

        # 设置窗口属性
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('视频压缩器')
        self.show()

    def showFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 使用Qt风格的文件对话框

        # 获取用户选择的文件夹路径
        selected_folder = QFileDialog.getExistingDirectory(self, "选择要压缩的文件夹", options=options)

        if selected_folder:
            print(f"选择的文件夹路径: {selected_folder}")
            self.compressVideos(selected_folder)

    def compressVideos(self, input_folder):
        output_folder = os.path.join(os.path.abspath(input_folder), "output")
        os.makedirs(output_folder, exist_ok=True)

        # 获取输入目录中的所有视频文件
        input_files = [f for f in os.listdir(input_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

        # 遍历每个视频文件并压缩
        for input_file in input_files:
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, input_file)

            print(f"正在压缩文件: {input_file}")
            self.compressVideo(input_path, output_path)

        print("压缩完成！")

    def compressVideo(self, input_path, output_path):
        # 构建 ffmpeg 命令
        ffmpeg_cmd = f"ffmpeg -i {input_path} -c:v libx264 -crf 23 -c:a aac -strict experimental -b:a 128k {output_path}"

        # 调用系统命令
        subprocess.run(ffmpeg_cmd, shell=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoCompressorApp()
    sys.exit(app.exec_())

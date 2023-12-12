import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QListWidget

class VideoCompressorApp(QWidget):
    def __init__(self):
        super(VideoCompressorApp, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建按钮
        self.selectFilesButton = QPushButton('选择文件', self)
        self.selectFilesButton.clicked.connect(self.showFilesDialog)

        # 创建列表控件
        self.fileListWidget = QListWidget()

        # 创建压缩按钮
        self.compressButton = QPushButton('压缩选中文件', self)
        self.compressButton.clicked.connect(self.compressSelectedFiles)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.selectFilesButton)
        vbox.addWidget(self.fileListWidget)
        vbox.addWidget(self.compressButton)

        # 设置布局
        self.setLayout(vbox)

        # 设置窗口属性
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('视频压缩器')
        self.show()

    def showFilesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 使用Qt风格的文件对话框

        # 获取用户选择的文件路径列表
        selected_files, _ = QFileDialog.getOpenFileNames(self, "选择文件", "", options=options)

        if selected_files:
            print(f"选择的文件列表: {selected_files}")
            self.updateFileList(selected_files)

    def updateFileList(self, file_paths):
        # 清空列表
        self.fileListWidget.clear()

        # 将文件路径添加到列表中
        for file_path in file_paths:
            self.fileListWidget.addItem(file_path)

    def compressSelectedFiles(self):
        # 遍历列表中的文件路径并压缩
        for row in range(self.fileListWidget.count()):
            input_file = self.fileListWidget.item(row).text()
            output_file = os.path.join(os.path.dirname(input_file), "output", os.path.basename(input_file))

            print(f"正在压缩文件: {input_file}")
            self.compressVideo(input_file, output_file)

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

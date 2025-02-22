import os

from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QPushButton
from PySide6.QtCore import QFile, QTextStream, QUrl


# https://chatgpt.com/c/67b31fa0-cfac-800b-bce1-fb5ca5425051
# Check for help on images and hyperlinks
class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super(HelpDialog, self).__init__(parent=parent)
        self.setWindowTitle('Help')
        self.setGeometry(100, 100, 600, 600)
        self._base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'help'))
        self._text_browser = QTextBrowser(self)
        self._text_browser.setOpenExternalLinks(True)
        self._text_browser.anchorClicked.connect(self.handle_link)
        self._text_browser.setSearchPaths([self._base_path])        
        self._back_button = QPushButton('Back to home', self)
        self._back_button.clicked.connect(lambda: self.load_page("index.html"))
        self._close_button = QPushButton('Close', self)
        self._close_button.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(self._back_button)
        layout.addWidget(self._text_browser, 1)
        layout.addWidget(self._close_button)
        self.setLayout(layout)
        self.load_page('index.html')

    def load_page(self, file_name):
        file_path = os.path.join(self._base_path, file_name)
        f = QFile(file_path)
        if f.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(f)
            html_content = stream.readAll()
            self._text_browser.setHtml(html_content)
            self._text_browser.setSource(QUrl.fromLocalFile(file_path))
            f.close()

    def handle_link(self, url):
        self.load_page(url.toString())
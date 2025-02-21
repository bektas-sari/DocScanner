import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton,
    QFileDialog, QTextEdit, QComboBox, QLabel, QHBoxLayout
)
from PyQt6.QtCore import QThread, pyqtSignal
from ocr_engine import extract_text

class OCRThread(QThread):
    update_text = pyqtSignal(str)

    def __init__(self, image_path, language):
        super().__init__()
        self.image_path = image_path
        self.language = language

    def run(self):
        text = extract_text(self.image_path, self.language)
        self.update_text.emit(text)

class OCRApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DocScanner - OCR Application")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
            }
            QTextEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 2px solid #555;
                font-size: 16px;
                padding: 12px;
                border-radius: 8px;
                font-family: 'Arial', sans-serif;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 12px 20px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QComboBox {
                background-color: #1E1E1E;
                color: #FFFFFF;
                padding: 6px;
                border: 2px solid #555;
                font-size: 14px;
                border-radius: 6px;
            }
            QLabel {
                color: #FFFFFF;
                font-size: 18px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Başlık etiketi
        header_label = QLabel("DocScanner OCR Application")
        header_label.setStyleSheet("font-size: 22px; font-weight: bold; padding: 10px; text-align: center;")
        main_layout.addWidget(header_label)

        controls_layout = QHBoxLayout()
        main_layout.addLayout(controls_layout)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.start_ocr)
        controls_layout.addWidget(self.upload_button)

        self.language_selector = QComboBox()
        self.language_selector.addItems(["eng", "tur"])
        controls_layout.addWidget(self.language_selector)

        self.save_button = QPushButton("Save Text")
        self.save_button.clicked.connect(self.save_text)
        controls_layout.addWidget(self.save_button)

        # Metin görüntüleme alanı
        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit)

        # Footer
        footer_label = QLabel("© Bektas - 2025")
        footer_label.setStyleSheet("color: #FFFFFF; font-size: 12px; padding: 10px; text-align: center;")
        main_layout.addWidget(footer_label)

        self.thread = None

    def start_ocr(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image files (*.jpg *.jpeg *.png *.bmp)")
        if file_name:
            language = self.language_selector.currentText()
            self.thread = OCRThread(file_name, language)
            self.thread.update_text.connect(self.update_text)
            self.thread.start()

    def update_text(self, text):
        self.text_edit.setText(text)

    def save_text(self):
        if self.text_edit.toPlainText():
            file_name, file_type = QFileDialog.getSaveFileName(self, "Save Text", "", "Text Files (*.txt);;PDF Files (*.pdf)")
            if file_name:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec())

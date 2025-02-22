from PySide6.QtWidgets import QPushButton, QLabel, QFileDialog, QVBoxLayout

from mosamaticdesktop.tasks.taskdialog import TaskDialog


class CalculateMetricsTaskDialog(TaskDialog):
    def __init__(self, parent=None):
        super(CalculateMetricsTaskDialog, self).__init__(parent)
        self._image_dir = None
        self._open_image_dir_button = QPushButton('Open image directory', self)
        self._open_image_dir_button.clicked.connect(self.open_model_directory)
        self._image_dir_label = QLabel('Image directory:', self)
        self._patient_heights_file = None
        self._load_patient_heights_file_button = QPushButton('(Optional) Load patient heights file', self)
        self._load_patient_heights_file_button.clicked.connect(self.load_patient_heights_file)
        self._patient_heights_file_label = QLabel('Patient heights:', self)
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._open_image_dir_button)
        self._layout.addWidget(self._image_dir_label)
        self._layout.addWidget(self._load_patient_heights_file_button)        
        self._layout.addWidget(self._patient_heights_file_label)
        self.init_ui()

    def get_content_layout(self):
        return self._layout

    def open_model_directory(self):
        self._image_dir = QFileDialog.getExistingDirectory(self, 'Select directory')
        if self._image_dir:
            self._image_dir_label.setText(f'Model directory: {self._image_dir}')

    def load_patient_heights_file(self):
        self._patient_heights_file, _ = QFileDialog.getOpenFileName(self, 'Select patient heights CSV file')
        if self._patient_heights_file:
            self._patient_heights_file_label.setText(f'Patient heights: {self._patient_heights_file}')

    def update_params(self):
        self.set_param('image_dir', self._image_dir)
        self.set_param('patient_heights_file', self._patient_heights_file)
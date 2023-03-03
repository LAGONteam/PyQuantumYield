from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QSizePolicy, QListWidgetItem
import QuantumYieldsCalculation as QY

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(400,200)
        self.setWindowTitle("PyQuantumYield")

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.create_widget()
        self.show_solvent_sample_data()
        self.show_ref_data()
        self.button_calculate.clicked.connect(self.calculate)

    @property
    def ref_name(self):
        for ref_selected in self.ls_ref.selectedItems():
                return ref_selected.text()

    @property
    def solvent_name(self):
        for solvent_selected in self.ls_solvent_sample.selectedItems():
                return solvent_selected.text()

    @property
    def get_ref_abs(self):
        data =self.le_abs_ref.text()
        try :
            data= float(data)
            return data
        except:
            self.le_abs_ref.setText("Only digits !")
            return False

    @property
    def get_sample_abs(self):
        data= self.le_abs_sample.text()
        try :
            data= float(data)
            return data
        except:
            self.le_abs_sample.setText("Only digits !")
            return False

    @property
    def get_ref_fluo(self):
        data = self.le_fluo_ref.text()
        try :
            data= float(data)
            return data
        except:
            self.le_fluo_ref.setText("Only digits !")
            return False

    @property
    def get_sample_fluo(self):
        data= self.le_fluo_sample.text()
        try :
            data= float(data)
            return data
        except:
            self.le_fluo_sample.setText("Only digits !")
            return False

    def create_widget(self):
        self.lbl_name_ref = QLabel("Reference")
        self.lbl_name_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_name_sample = QLabel("Sample")
        self.lbl_name_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_abs_ref = QLabel("Abs =")
        self.lbl_abs_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_abs_sample = QLabel("Abs = ")
        self.lbl_abs_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_fluo_ref = QLabel("Fluo. intensity =")
        self.lbl_fluo_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_fluo_sample = QLabel("Fluo. intensity = ")
        self.lbl_fluo_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_phi = QLabel("Phi = ")
        self.lbl_phi.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.le_abs_ref = QLineEdit("")
        self.le_abs_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.le_abs_sample = QLineEdit("")
        self.le_abs_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.le_fluo_ref = QLineEdit("")
        self.le_fluo_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.le_fluo_sample = QLineEdit("")
        self.le_fluo_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.le_phi_sample = QLineEdit("")
        self.le_phi_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.void =QLabel("")
        self.void.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button_calculate = QPushButton("Calculate !")

        self.ls_ref = QListWidget()
        self.ls_ref.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ls_solvent_sample = QListWidget()
        self.ls_solvent_sample.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout.addWidget(self.lbl_name_ref, 0, 0, 2, 1)
        self.main_layout.addWidget(self.lbl_name_sample, 2, 0, 2, 1)

        self.main_layout.addWidget(self.ls_ref, 0, 1, 2, 1)
        self.main_layout.addWidget(self.ls_solvent_sample, 2, 1, 2, 1)

        self.main_layout.addWidget(self.lbl_abs_ref, 0, 2, 1, 1)
        self.main_layout.addWidget(self.le_abs_ref, 0, 3, 1, 1)
        self.main_layout.addWidget(self.lbl_fluo_ref, 0, 4, 1, 1)
        self.main_layout.addWidget(self.le_fluo_ref, 0, 5, 1, 1)

        self.main_layout.addWidget(self.void, 1, 2, 1, 1)
        self.main_layout.addWidget(self.void, 1, 3, 1, 1)
        self.main_layout.addWidget(self.void, 1, 4, 1, 1)
        self.main_layout.addWidget(self.void, 1, 5, 1, 1)

        self.main_layout.addWidget(self.lbl_abs_sample, 2, 2, 1, 1)
        self.main_layout.addWidget(self.le_abs_sample, 2, 3, 1, 1)
        self.main_layout.addWidget(self.lbl_fluo_sample, 2, 4, 1, 1)
        self.main_layout.addWidget(self.le_fluo_sample, 2, 5, 1, 1)

        self.main_layout.addWidget(self.button_calculate, 3, 3, 1, 1)
        self.main_layout.addWidget(self.lbl_phi, 3, 4, 1, 1)
        self.main_layout.addWidget(self.le_phi_sample, 3, 5, 1, 1)

    def show_solvent_sample_data(self):
        data = QY.Main().get_solvent_data()
        for solvent_name in data:
            self.ls_solvent_sample.addItem(solvent_name)

    def show_ref_data(self):
        data = QY.Main().get_ref_data()
        for ref_name in data:
            self.ls_ref.addItem(ref_name)

    def calculate(self):
        if self.get_ref_abs == False or self.get_sample_abs == False or self.get_ref_fluo== False or self.get_sample_fluo == False:
            return
        else:
            phi = QY.Main().calcul(fluo_ref= self.get_ref_fluo, fluo_sample=self.get_sample_fluo, abs_sample=self.get_sample_abs, abs_ref=self.get_ref_abs, solvent_sample= self.solvent_name, ref_name=self.ref_name)
            self.le_phi_sample.setText(f"{phi}")

app = QApplication()
main_window=Main()
main_window.show()
app.exec()


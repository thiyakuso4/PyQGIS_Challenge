mb = QMessageBox()
mb.setText("Click OK to confirm")
mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
mb.setIcon(QMessageBox.Warning)
return_value = mb.exec()

if return_value == QMessageBox.Ok:
    print('Pressed ok')
elif return_value == QMessageBox.Cancel:
    print('Pressed Cancel')
import pdfRenamer

gui = pdfRenamer.Gui()
gui.scanFiles("scan-*.pdf")
gui.showAndRename()
gui.loop()
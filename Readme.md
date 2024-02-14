## Конвертация ui файла
`pyside2-uic .\ui_main.ui > ui_main.py`

## Конвертация файла ресурсов
`pyside2-rcc resources.qrc -o resources_rc.py`

## Билд
`pyinstaller app.spec`

# Команда билда, если не получилось с предыдущим
`pyinstaller --noconfirm --onefile --windowed --add-data "ui.py;." --add-data "resources_rc.py;." --add-data "romantic.mp3;." --add-data "tragic.mp3;." "app.py"`
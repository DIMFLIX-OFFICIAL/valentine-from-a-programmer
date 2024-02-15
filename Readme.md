## Конвертация ui файла
`cd ui`
`pyside2-uic .\ui_main.ui > ui.py`

## Конвертация файла ресурсов
`cd ui`
`pyside2-rcc resources.qrc -o resources_rc.py`

## Билд
`pyinstaller app.spec`

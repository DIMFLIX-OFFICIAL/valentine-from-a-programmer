https://github.com/DIMFLIX-OFFICIAL/valentine-from-a-programmer/assets/112165977/2b3fc795-b2c0-4369-bd2f-0401d80c9f5d

## Конвертация ui файла
`cd ui`
`pyside2-uic .\ui_main.ui > ui.py`

## Конвертация файла ресурсов
`cd ui`
`pyside2-rcc resources.qrc -o resources_rc.py`

## Build
`pyinstaller app.spec`
 

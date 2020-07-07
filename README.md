### osuSlice
Программа для генерации тренировочных уровней:

Текущий функционал:
Программа делает поиск по всем папкам находит в них файлы заканчивающиеся на [train].osu, по этому файлу определяется время для отрезка и имя файла mp3, который надо повторять. После этого обрезает музыку, добавляет подъем и затухание громкости и повторяет необходимое количество раз, так же создается файл конфигурации с повторениям игровых элементов.  

Использование с помощью osuSlice.exe:
ВАЖНО!  В случае использования osuSlice.exe будет сгенерировано 15 повторов с интервалом 3,5 сек. до начала и 3.5 сек после повтора.
                
1. Поместить файл osuSlice в дирректорию \OSU!
2. В эдиторе OSU! создать вырезанный участок с необходимыми элементами и сохранить как новую сложность "train"-без ковычек и с маленькой буквы.
3. Запустить файл osuSlice.exe.
4. Автоматически будут созданы mp3 и новые конфиг-файлы во всех дочерних папках в которых есть конфиг файлы *[train].osu.

ГОТОВО: Можно заходить и играть
                
Использование с помощью Python3 (понадобится установка ffmpeg и pydab):

1. Поместить файлы программы в дирректорию \OSU!
2. Если есть необходимость в файле settings определить следующие настройки
    2.1 name_new_mp3 - Определить название новых файла mp3
    2.2 num_repeats - Количество повторов интервалов
    2.3 break_time - Общее время пустого интервала между игровыми эллементами в миллисекундах. Этот интервал делится попалам. Пример: если значение 8000, то к игровым эллементам до начала добавляется 4000 и после 4000. На эти же интервалы приходится подъем и затухание громкости.
3. В эдиторе OSU! создать вырезанный участок с необходимыми элементами и сохранить как новую сложность "train"-без ковычек.
4. Запустить файл main.py

ГОТОВО: Можно заходить и играть
Для создания .exe можно использовать (pyinstaller --onefile)


                
В планах добавить/изменить:

1. Переписать полностью весь код и перевести файлы конфигурации в класс с подклассами
2. Поддержка всех версий "osu file format"

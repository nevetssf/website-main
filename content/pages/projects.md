Title: Projects
Slug: projects
Status: published

## [eInk Device Notebook Generator](https://eink-notebook-templates.streamlit.app/)

Generate printable notebook templates sized for eInk devices. 'Notebooks' are just PDF documents which you can write on using your device. I wrote this app because reMarkable doesn't allow the user to create hypterlinks within documents, but it does honor hyperlinks in PDF's. The notebook it creates is simple: a title page, a table of contents, and a list of pages (dot grid, lined, grid, or blank - your choice). The table of contents has built-in hyperlinks to the associated page. The pages are marked on each page, and they function as a hyperlink back to the table of contents. 

## [DL24 Load Tester Software](https://github.com/nevetssf/aTorch-DL24P)

For anyone in the electronic load testing as a hobby world, the aTorch DL24 has cult status. It's a pretty well-engineered piece of hardware, available for about $40 on Ali Express. I use mine for testing battery capacity of my camera batteries, so I can know when they're pretty much exhausted. 

Not surprisingly, the software that comes with the DL24 is pretty much garbage. It doesn't exactly crash, but it only runs on Windows and even on my recent-model Framework 13, it has a bizarre layout scheme, with oversizes fonts that fill tiny spaces in the GUI. You have to see it to apprecaite the insanity of it. 

So, with Claude Code's help, and a few other github projects, I reprouced the serial protocol and wrote a GUI to interact with the DL24. You can run the DL24 stand-alone of course, but with the testing software it becomes a mini battery and battery charger characterizaton station. 

To test battery capacity, I charge up the battery in its charger, then see see how much total current can be drawn. To test the charger, I apply various voltages to mimic a charging battery to see how much current the carger supplies. It also has a power bank capacity tester, which is similar to the battery tester, but tweaked slightly for a power bank. 

Every test run is stored as a JSON file, and I've added the settings for many standard batteries. Every run is also stored a sqlite database, you can go back and compare earlier measurements. I also implemented a data browser for comparing data sets.

It's still in what I'd call an alpha stage, but I hope to finish it in the next few months. And in my humble opinion it's already much better than the aTorch software. 

It's open-source, free, and written in Qt and Python. In theory it's cross-platform but I've only tested it on MacOS so far. 


# PYQT FAST FRAME WORK

I wanted to make a framework to build and manage my applications so that I can not have to remake the same boiler plate for new apps.

This is a few interations deep now, and slowly over time it gets better and better as I make new apps with the new designs.


Right now the struture is like this 


- apps (Connections, Functions, Layout)
    - Connections handle same page widget connecitons and updating
    - Functions are bits of callable logic 
    - Layout is how the widgets get placed on the app

- Front end
    - Different type of helpers for app Layouts

- Window (Really should be called like widget to app maker)
    - Takes and process the widgets to be placed


- Combiner
    - Multi page connections where updates can happen across apps 
    - app1 <--updates--> app2  
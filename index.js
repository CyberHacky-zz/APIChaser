const  electron = require('electron');

const{ app, BrowserWindow, Menu } = electron;

let mainWindow;
let addWindow;

app.on('ready', () => {
    var path = require('path');
   mainWindow = new BrowserWindow({});
   mainWindow.maximize();
   
   mainWindow.loadURL(path.join(__dirname, './src/index.html'));
   mainWindow.on('closed', () => app.quit());

   const mainMenu = Menu.buildFromTemplate(menuTemplate);
   Menu.setApplicationMenu(mainMenu);

   win = new BrowserWindow({show: false});

});

function createContactWindow(){

    addWindow = new BrowserWindow({
        width: 1000,
        height: 750,
        title: 'Contact us',
    });
    var path = require('path');
    addWindow.loadURL(path.join(__dirname, './src/contact.html'));
} 

function createAboutWindow(){

    addWindow = new BrowserWindow({
        width: 1200,
        height: 750,
        title: 'About',
    });
    var path = require('path');
    addWindow.loadURL(path.join(__dirname, './src/about.html'));
}

function createoldWindow(){

    addWindow = new BrowserWindow({
        width: 1200,
        height: 1000,
        title: 'New Page',
    });
    var path = require('path');
    addWindow.loadURL(path.join(__dirname, './oldinterface/index.html'));
}


const menuTemplate = [
    {
        label: 'File',
        submenu:[
            { label: 'New Project' },

            { 
                label: 'Quit',
                accelerator: process.platform === 'darwin' ? 'Command+Q' : 'Ctrl+Q',
                click (){
                    app.quit();
                }

            }
        ]

    },

    {
        label: 'Edit',
        submenu:[
            { label: 'Undo' },
            { label: 'Redo' },
            { label: 'Cut' },
            { label: 'Copy' },
            { label: 'Paste' },
            { label: 'Delete' },
            { label: 'Select All' },
        ]
    },

    {
        label: 'Help',
        submenu:[
            {label: 'Documentation'},
            {label: 'Community Discussion'},
            {label: 'Search Issue'},
            {label: 'Check for Update'},
            {label: 'Contact us',
                click(){ createContactWindow();}
            },
            {label: 'About',
                click(){createAboutWindow();}
            
            },
            {label: 'Donate'},

        ] 
    },

    



];

if (process.env.NODE_ENV !== 'production') {

    menuTemplate.push({
    
        label: 'Extra',
        submenu:[
            {
                label: 'Toogle Developer Tools',
                accelerator: process.platform === 'darwin' ? 'Command+Alt+I' : 'Ctrl+Shift+I',
                click(item, focusedwindow) {
                    focusedwindow.toggleDevTools();
                    
                }
            },

            {label: 'OLD UI',
                click(){createoldWindow();}
            
            },
        ]

    });
}

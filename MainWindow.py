
import wx
import os

class MainWindow( wx.Frame ):
    def __init__( self, filename="noname.txt" ):
        super( MainWindow, self ).__init__( None, size=( 400, 200 ) )
        self.filename   = filename
        self.dirname    = "."
        self.CreateInteriorWindowComponents()
        self.CreateExteriorWindowComponents()

    def CreateInteriorWindowComponents( self ):
        self.control = wx.TextCtrl( self, style=wx.TE_MULTILINE )

    def CreateExteriorWindowComponents( self ):
        self.CreateMenu()
        self.CreateStatusBar()
        self.SetTitle()

    def CreateMenu( self ):
        file_menu   = wx.Menu()
        about       = ( wx.ID_ABOUT, "&About", "Information about this program", self.OnAbout )
        open_       = ( wx.ID_OPEN, "&Open", "Open a new file", self.OnOpen )
        save        = ( wx.ID_SAVE, "&Save", " Save the current file", self.OnSave )
        save_as     = ( wx.ID_SAVEAS, "Save &As", "Save the curretn file under different name", self.OnSaveAs )
        separator   = ( None, None, None, None )
        exit        = ( wx.ID_EXIT, "Exit", "Terminate the program", self.OnExit )
        items_list  = [ about, open_, save, save_as, separator, exit ]
        for idt, label, help_text, handler in items_list:
            if idt == None:
                file_menu.AppendSeparator()
            else:
                item = file_menu.Append( idt, label, help_text )
                self.Bind( wx.EVT_MENU, handler, item )

        menu_bar    = wx.MenuBar()
        menu_bar.Append( file_menu, "File" )
        self.SetMenuBar( menu_bar )

    def SetTitle( self ):
        super( MainWindow, self ).SetTitle( "Editor %s" % self.filename )

    def DefaultFileDialogOptions( self ):
        return dict(
            message="Choose a file",
            defaultDir=self.dirname,
            wildcard="*.*",
        )

    def AskUserForFilename( self, **dialog_options ):
        dialog = wx.FileDialog( self, **dialog_options )
        if dialog.ShowModal() == wx.ID_OK:
            user_provided_filename  = True
            self.filename           = dialog.GetFilename()
            self.dirname            = dialog.GetDirectory()
            self.SetTitle()
        else:
            user_provided_filename  = False
        dialog.Destroy()
        return user_provided_filename

    def OnAbout( self, event ):
        dialog = wx.MessageDialog( self, "A sample editor\n in wxPython", "About Sample Editor", wx.OK )
        dialog.ShowModal()
        dialog.Destroy()

    def OnExit( self, event ):
        self.Close()

    def OnSave( self, event ):
        textfile = open( os.path.join( self.dirname, self.filename), "w" )
        textfile.write( self.control.GetValue() )
        textfile.close()

    def OnOpen( self, event ):
        if self.AskUserForFilename( style=wx.OPEN, **self.DefaultFileDialogOptions() ):
            textfile = open( os.path.join ( self.dirname, self.filename ), "r" )
            self.control.SetValue( textfile.read() )
            textfile.close()

    def OnSaveAs( self, event ):
        if self.AskUserForFilename( defaultFile=self.filename, style=wx.SAVE, **self.DefaultFileDialogOptions() ):
            self.OnSave( event )

app     = wx.App()
frame   = MainWindow()
frame.Show()
app.MainLoop()

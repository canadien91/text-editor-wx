
import wx

class MainWindow( wx.Frame ):
    def __init__( self, parent, title ):
        wx.Frame.__init__( self, parent, title=title, size=( 200, 100 ) )
        self.control    = wx.TextCtrl( self, style=wx.TE_MULTILINE )
        self.CreateStatusBar()

        filemenu        = wx.Menu()
        filemenu.Append( wx.ID_ABOUT, "&About", " Information about this program" )
        filemenu.AppendSeparator()
        filemenu.Append( wx.ID_EXIT, "&Exit", " Terminate the program" )

        menu_bar        = wx.MenuBar()
        menu_bar.Append( filemenu, "&File" )
        self.SetMenuBar( menu_bar )
        self.Show( True )

app     = wx.App( False )
frame   = MainWindow( None, "Sample editor" )
app.MainLoop()

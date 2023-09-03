# -*- coding: utf-8 -*-
import wx

class base(wx.Menu):
    def __init__(self):
        super(base, self).__init__()
        self.boost = wx.MenuItem(self, wx.ID_ANY, _("&Boost"))
        self.Append(self.boost)
        self.reply = wx.MenuItem(self, wx.ID_ANY, _(u"Re&ply"))
        self.Append(self.reply)
        self.fav = wx.MenuItem(self, wx.ID_ANY, _(u"&Add to favorites"))
        self.Append(self.fav)
        self.unfav = wx.MenuItem(self, wx.ID_ANY, _(u"R&emove from favorites"))
        self.Append(self.unfav)
        self.openUrl = wx.MenuItem(self, wx.ID_ANY, _("&Open URL"))
        self.Append(self.openUrl)
        self.openInBrowser = wx.MenuItem(self, wx.ID_ANY, _(u"&Open in Twitter"))
        self.Append(self.openInBrowser)
        self.play = wx.MenuItem(self, wx.ID_ANY, _(u"&Play audio"))
        self.Append(self.play)
        self.view = wx.MenuItem(self, wx.ID_ANY, _(u"&Show tweet"))
        self.Append(self.view)
        self.copy = wx.MenuItem(self, wx.ID_ANY, _(u"&Copy to clipboard"))
        self.Append(self.copy)
        self.remove = wx.MenuItem(self, wx.ID_ANY, _(u"&Delete"))
        self.Append(self.remove)
        self.userActions = wx.MenuItem(self, wx.ID_ANY, _(u"&User actions..."))
        self.Append(self.userActions)
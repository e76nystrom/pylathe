import wx

class ComboBox(wx.ComboBox):
    def __init__(self, parent, label, indexList,  choiceList, \
                 *args, **kwargs):
        self.label = label
        self.indexList = indexList
        self.choiceList = choiceList
        self.text = None
        super(ComboBox, self).__init__(parent, *args, **kwargs)

    def GetValue(self):
        val = self.GetCurrentSelection()
        rtnVal = self.indexList[val]
        # print("ComboBox GetValue %s %s %s" % (self.label, val, rtnVal))

        # if self.text is not None:
        #     print("label \"%s\" GetValue %d text \"%s\" index %d" % \
        #           (self.label, rtnVal, self.text[val], val))
        #     print("indexList", self.indexList)
        return str(rtnVal)

    def SetValue(self, val):
        # print("ComboBox SetValue %s %s" % (self.label, str(val)))
        if isinstance(val, str):
            if val.isnumeric():
                val = int(val)
            else:
                val = 0
        for (n, index) in enumerate(self.indexList):
            if val == index:
                self.SetSelection(n)
                # if self.text is not None:
                #     print("label \"%s\" SetValue %d text \"%s\" index %d" % \
                #           (self.label, val, self.text[index], n))
                #     print("indexList", self.indexList)


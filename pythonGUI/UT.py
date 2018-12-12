import unittest
from Resources import I18N
from GUI import OOP as GUI

class GuiUnitTest(unittest.TestCase):

    def test_TitleIsEnglish(self):
        i18n = I18N('en')
        self.assertEqual(i18n.title,
                            "Python Graphical User Interface")

    def test_TitleIsGerman(self):
        i18n = I18N('de')
        self.assertEqual(i18n.title,
                            "Python Grafische Benutzeroberfl" + "\u00E4" + 'che')

class WidgetsTestsEnglish(unittest.TestCase):

    def setUp(self):
        self.gui = GUI('en')

    def tearDown(self):
        self.gui = None

    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.file, "File")
        self.asserEqual(self.gui.i18n.mgrFiles, " Manage Files ")
        self.asserEqual(self.gui.i18n.browseTo, "Browse to File...")

    def test_LabelFrameText(self):
        labelFrameText = self.gui.widgetFrame['text']
        self.asserEqual(labelFrameText, " Widgets Frame ")
        self.gui.radVar.set(1)
        self.gui.callBacks.radCall()
        labelFrameText = self.gui.widgetFrame['text']
        self.asserEqual(labelFrameText,
                                    " Widgets Rahmen in Gold")


if __name__=='__main__':
    unittest.main()

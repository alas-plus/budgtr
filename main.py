from kivy.app import App

from res.widgets.entries import BudgtrEntriesView


class BudgtrApp(App):
    def build(self):
        return BudgtrEntriesView()


if __name__ == '__main__':
    BudgtrApp().run()

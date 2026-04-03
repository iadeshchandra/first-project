import sys
from PyQt5.QtWidgets import QApplication

# Entry point for the SHDA Management App
class SHDAApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        # Initialize your screens
        self.login_screen = LoginScreen()
        self.dashboard_screen = DashboardScreen()
        self.members_screen = MembersScreen()
        self.donations_screen = DonationsScreen()
        self.expense_screen = ExpenseScreen()
        self.reports_screen = ReportsScreen()
        self.settings_screen = SettingsScreen()

    def show_login(self):
        self.login_screen.show()


class LoginScreen:
    def show(self):
        print('Displaying Login Screen')


class DashboardScreen:
    def show(self):
        print('Displaying Dashboard Screen')


class MembersScreen:
    def show(self):
        print('Displaying Members Screen')


class DonationsScreen:
    def show(self):
        print('Displaying Donations Screen')


class ExpenseScreen:
    def show(self):
        print('Displaying Expense Screen')


class ReportsScreen:
    def show(self):
        print('Displaying Reports Screen')


class SettingsScreen:
    def show(self):
        print('Displaying Settings Screen')


if __name__ == '__main__':
    app = SHDAApp(sys.argv)
    app.show_login()
    sys.exit(app.exec_())
import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 22/05/2023", color="blue", size=24)
        self._page.controls.append(self._title)


        #row 1
        self.txtAnno = ft.TextField(label="Anno")
        self.txtSalario = ft.TextField(label="Salario")
        self.btnGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handleCreaGrafo)

        row1 = ft.Row([ft.Container(self.txtAnno, width=200),
                       ft.Container(self.txtSalario, width=200),
                       ft.Container(self.btnGrafo, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #row 2
        self.btnConnesse = ft.ElevatedButton(text="Calcola connesse", on_click=self._controller.handleCalcolaConnesse)
        self.btnGradoMassimo = ft.ElevatedButton(text="Grado massimo", on_click=self._controller.handleGradoMassimo)
        self.btnDreamTeam = ft.ElevatedButton(text="Dream Team", on_click=self._controller.handleDreamTeam)
        row2 = ft.Row([ft.Container(self.btnConnesse, width=200),
                       ft.Container(self.btnGradoMassimo, width=200),
                       ft.Container(self.btnDreamTeam, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        #row3
        self.txtResult1 = ft.ListView(auto_scroll=True)
        self._page.controls.append(self.txtResult1)


        self.txtResult2 = ft.ListView(auto_scroll=True)
        self._page.controls.append(self.txtResult2)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

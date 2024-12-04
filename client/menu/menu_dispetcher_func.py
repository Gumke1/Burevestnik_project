import os

import requests

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6.uic.properties import QtWidgets
from pyqtgraph import DateAxisItem

from client.exceptions import ReportException, EmptyLineError
from client.menu import menu_dispetcher
from client.menu.JSONTableModel import JsonTableModel
from client.menu.extra_func import get_users, get_repair_hardware
from client.menu.reporting import docs_report, csv_report
from client.misc.func_with_time import get_dates
from client.settings import API_URL

import pyqtgraph as pg
from datetime import datetime


def create_top_users(data):
    # Проверка наличия необходимых ключей
    required_keys = ['name', 'middle_name', 'surname', 'completed_task', 'post']
    for item in data:
        if not all(key in item for key in required_keys):
            print(f"Ошибка: Отсутствуют необходимые ключи в словаре: {item}")
            return None

    # Обработка completed_task (преобразование в число и обработка)
    for item in data:
        try:
            item['completed_task'] = int(item.get('completed_task', 0))
        except ValueError:
            pass

    # Сортировка пользователей по completed_task в убывающем порядке
    sorted_users = sorted(data, key=lambda x: x['completed_task'], reverse=True)

    # Создание списка названий столбцов
    columns = ['ФИО', 'Выполненные задания', 'Должность']

    # Создание списка строк
    rows = [[
        f"{user['name']} {user['middle_name']} {user['surname']}",
        user['completed_task'],
        user['post']
    ] for user in sorted_users]

    return columns, rows


def create_top_team(data):
    teams = {}
    for item in data:
        team_id = int(item['team'])
        if team_id not in teams:
            teams[team_id] = []
        teams[team_id].append(item)

    team_data = []
    for team_id, team_members in teams.items():

        completed_tasks = sum(int(item.get('completed_task', 0)) for item in team_members if
                              isinstance(item.get('completed_task'), (int, float)))
        try:
            best_worker = max(team_members, key=lambda x: x.get('completed_task', 0))
            best_worker_fio = f"{best_worker['name']} {best_worker['middle_name']} {best_worker['surname']}"
        except (ValueError, KeyError, TypeError):  # Обработка различных ошибок
            best_worker_fio = "N/A"
        team_data.append({'team': team_id, 'completed_tasks': completed_tasks, 'best_worker_fio': best_worker_fio})
    columns = ['team', 'completed_tasks', 'best_worker_fio']

    # Создание списка строк
    rows = [[str(item['team']), str(item['completed_tasks']), item['best_worker_fio']] for item in team_data]

    return columns, sorted(rows, key=lambda x: x[1], reverse=True)


def do_report(name, statistic, docs=True, csv=False):
    if docs:
        return docs_report(name, statistic)
    if csv:
        return csv_report(name, statistic)


def send_to_db(nickname, id_problem, self):  # Notification + send
    repair_hardware = {'nickname': nickname}
    user = {'nickname': nickname, 'busy': 1}
    response_repair_hardware_nickname = requests.get(f'{API_URL}/data/users').json()

    for row in response_repair_hardware_nickname:
        if row.get('nickname') == nickname:
            if row.get('busy') == 1:
                QMessageBox.critical(self, 'Critical', 'Работник уже занят, выберите другого')
                break

    requests.put(f'{API_URL}/data/repair_hardware/{id_problem}',
                 json=repair_hardware)
    requests.put(f'{API_URL}/data/users/{nickname}', json=user)
    requests.post(f'{API_URL}/send_message', json=user)


class DateAxisItem(pg.AxisItem):  # Определение DateAxisItem здесь
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value).strftime('%Y-%m-%d') for value in values]


class Ui_MainWindow1(QMainWindow, menu_dispetcher.Ui_MainWindow):
    # Класс основного окна администратора
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statistic = 'month'
        self.graphicsView_statistic.setBackground('w')
        # Подключение кнопок к соответствующим функциям
        self.pushButton_send_order.clicked.connect(self.send_order)
        self.refresh_btn.clicked.connect(self.refresh_bd)
        self.widget_5.setHidden(True)

        self.pushButton_tracing1.clicked.connect(self.switch_to_work)
        self.pushButton_tracing2.clicked.connect(self.switch_to_work)

        self.pushButton_team.clicked.connect(self.switch_to_top)
        self.pushButton_team2.clicked.connect(self.switch_to_top)

        self.pushButton_money1.clicked.connect(self.switch_to_statistic)
        self.pushButton_money2.clicked.connect(self.switch_to_statistic)

        self.pushButton_graph_4.clicked.connect(self.refresh_top_team)
        self.pushButton_graph_5.clicked.connect(self.refresh_top_users)

        self.pushButton_graph_6.clicked.connect(self.statistic_week)
        self.pushButton_graph_7.clicked.connect(self.statistic_month)
        self.pushButton_graph_9.clicked.connect(self.statistic_year)

        self.pushButton_graph.clicked.connect(self.build_graph)

        self.pushButton_report_2.clicked.connect(self.get_report)

    def statistic_year(self):
        self.statistic = 'year'

    def statistic_month(self):
        self.statistic = 'month'

    def statistic_week(self):
        self.statistic = 'week'

    def send_order(self):
        # Отправка информации о заказе в базу данных
        nik_work = self.lineEdit_nik_work.text()  # Получение ника работника
        id_problem = self.lineEdit_id_problem.text()  # Получение ID проблемы
        send_to_db(nik_work, id_problem, self)  # Отправка в базу данных

    def get_report(self):
        docs = self.radioButton_2.isChecked()
        csv = self.radioButton.isChecked()
        name = self.lineEdit.text()
        statistic = self.statistic
        if name == '':
            QMessageBox.critical(self, 'Critical', 'Заполни поля, дебил')
        else:
            try:
                message = do_report(name, statistic, csv=csv, docs=docs)
                QMessageBox.information(self, 'Успех', message)
            except ReportException:
                QMessageBox.critical(self, 'Critical', 'Error')

    def refresh_top_team(self):
        users = get_users()
        headers, rows = create_top_team(users)
        model_users = JsonTableModel(rows)
        model_users._headers = headers
        self.tableView_top_team.setModel(model_users)
        self.tableView_top_team.setStyleSheet("color: black; background-color: white;")

    def refresh_top_users(self):
        users = get_users()
        headers, rows = create_top_users(users)
        model_users = JsonTableModel(rows)
        model_users._headers = headers
        self.tableView_top_useres.setModel(model_users)
        self.tableView_top_useres.setStyleSheet("color: black; background-color: white;")

    def refresh_bd(self):
        users = get_users()
        repair_hardware = get_repair_hardware()

        headers = list(repair_hardware[0].keys())  # Заголовки из ключей первого словаря
        rows = [[row[header] for header in headers if row['done'] == 0] for row in repair_hardware]
        try:
            if [] in rows:
                while [] in rows:
                    rows.remove([])
        except ValueError:
            pass
        print(rows)
        if not rows:
            model_users = JsonTableModel(['Оборудование'])
            model_users._headers = ['В данный момент на предприятии всё оборудование исправно']
            self.tableView.setModel(model_users)
            self.tableView.setStyleSheet("color: black; background-color: white;")
            print('sdfsdf')
        else:
            print('aaaaaaa')
            model_users = JsonTableModel(rows)
            model_users._headers = headers
            self.tableView.setModel(model_users)
            self.tableView.setStyleSheet("color: black; background-color: white;")

        headers = list(users[0].keys())
        headers.remove('password')
        rows = [[row[header] for header in headers if row['busy'] == 0] for row in users]
        try:
            if [] in rows:
                while [] in rows:
                    rows.remove([])
        except ValueError:
            pass
        print(rows)
        if not rows:
            model_users = JsonTableModel(['Работники'])
            model_users._headers = ['В данный момент на предприятии всё работники заняты']
            self.tableView_2.setModel(model_users)
            self.tableView_2.setStyleSheet("color: black; background-color: white;")
        else:
            model_users = JsonTableModel(rows)
            model_users._headers = headers
            self.tableView_2.setModel(model_users)
            self.tableView_2.setStyleSheet("color: black; background-color: white;")

    def switch_to_statistic(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_top(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_work(self):
        self.stackedWidget.setCurrentIndex(1)

    def build_graph(self):
        self.graphicsView_statistic.clear()
        repair_hardware = get_repair_hardware()
        all_dates = get_dates(self.statistic)
        datas = [i for i in repair_hardware if i.get('done') == 1]
        data = []
        for i in all_dates:
            res = 0
            for j in datas:
                if j.get('end')[:10] == i:
                    res += 1
            data.append((i, res))
        x_data = [datetime.strptime(date_str.split()[0], '%Y-%m-%d').timestamp() for date_str, _ in data]
        y_data = [count for _, count in data]

        self.graphicsView_statistic.plot(x_data, y_data, pen='r', symbol='o')
        self.graphicsView_statistic.setLabel('left', 'Количество работы')
        self.graphicsView_statistic.setLabel('bottom', 'Дата')
        self.graphicsView_statistic.showGrid(x=True, y=True)
        self.graphicsView_statistic.setAxisItems({'bottom': DateAxisItem(orientation='bottom')})
        self.graphicsView_statistic.setTitle("Статистика выполненной работы")

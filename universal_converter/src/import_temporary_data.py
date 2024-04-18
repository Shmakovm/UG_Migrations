#!/usr/bin/python3
#
# Copyright @ 2020-2022 UserGate Corporation. All rights reserved.
# Author: Aleksei Remnev <ran1024@yandex.ru>
# License: GPLv3
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, contact the site <https://www.gnu.org/licenses/>.
#
# init_temporary_data.py
# Version 1.2
#--------------------------------------------------------------------------------------------------- 
#
import os, sys
from PyQt6.QtCore import QThread, pyqtSignal
from services import trans_name, default_urlcategorygroup
from common_func import write_bin_file


class GetTemporaryData(QThread):
    """Получаем конфигурационные данные с NGFW для заполнения служебных структур данных."""
    stepChanged = pyqtSignal(str)
    def __init__(self, utm):
        super().__init__()
        self.utm = utm
        self.ngfw_data = {}
        self.version = float(f'{self.utm.version_hight}.{self.utm.version_midle}')

    def run(self):
        """Заполняем служебные структуры данных"""
        self.stepChanged.emit(f'BLUE|Заполняем служебные структуры данных.')

        # Получаем список зон
        self.stepChanged.emit(f'BLACK|    Получаем список зон')
        err, result = self.utm.get_zones_list()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['zones'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список сертификатов
        self.stepChanged.emit(f'BLACK|    Получаем список сертификатов')
        err, result = self.utm.get_certificates_list()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['certs'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}
        self.ngfw_data['certs'][-1] = -1

        # Получаем список профилей аутентификации
        self.stepChanged.emit(f'BLACK|    Получаем список профилей аутентификации')
        err, result = self.utm.get_auth_profiles()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['auth_profiles'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список локальных групп
        self.stepChanged.emit(f'BLACK|    Получаем список локальных групп')
        err, result = self.utm.get_groups_list()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['local_groups'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список локальных пользователей
        self.stepChanged.emit(f'BLACK|    Получаем список локальных пользователей')
        err, result = self.utm.get_users_list()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['local_users'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список профилей SSL
        if self.version > 5:
            self.stepChanged.emit(f'BLACK|    Получаем список профилей SSL')
            err, result = self.utm.get_ssl_profiles_list()
            if err:
                self.stepChanged.emit(f'iRED|{result}')
                return
            self.ngfw_data['ssl_profiles'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}
        # Получаем список IP-листов

        self.stepChanged.emit(f'BLACK|    Получаем список IP-листов')
        err, result = self.utm.get_nlists_list('network')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['ip_lists'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список URL-листов
        self.stepChanged.emit(f'BLACK|    Получаем список URL-листов')
        err, result = self.utm.get_nlists_list('url')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['url_lists'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список групп категорий URL
        self.stepChanged.emit(f'BLACK|    Получаем список групп категорий URL')
        err, result = self.utm.get_nlists_list('urlcategorygroup')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['url_categorygroups'] = {default_urlcategorygroup.get(x['name'], x['name'].strip().translate(trans_name)): x['id'] for x in result}

        # Получаем список категорий URL
        self.stepChanged.emit(f'BLACK|    Получаем список категорий URL')
        err, result = self.utm.get_url_categories()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['url_categories'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список календарей
        self.stepChanged.emit(f'BLACK|    Получаем список календарей')
        err, result = self.utm.get_nlists_list('timerestrictiongroup')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['calendars'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список сервисов
        self.stepChanged.emit(f'BLACK|    Получаем список сервисов')
        err, result = self.utm.get_services_list()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['services'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список групп сервисов
        if self.version >= 7:
            self.stepChanged.emit(f'BLACK|    Получаем список групп сервисов')
            err, result = self.utm.get_nlists_list('servicegroup')
            if err:
                self.stepChanged.emit(f'iRED|{result}')
                return
            self.ngfw_data['service_groups'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список типов контента
        self.stepChanged.emit(f'BLACK|    Получаем список типов контента')
        err, result = self.utm.get_nlists_list('mime')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['mime'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список групп приложений
        self.stepChanged.emit(f'BLACK|    Получаем список групп приложений')
        err, result = self.utm.get_nlists_list('applicationgroup')
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['application_groups'] = {x['name'].strip().translate(trans_name): x['id'] for x in result}

        # Получаем список категорий приложений
        self.stepChanged.emit(f'BLACK|    Получаем список категорий приложений')
        err, result = self.utm.get_l7_categories()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['l7_categories'] = {x['name']: x['id'] for x in result}

        # Получаем список приложений l7
        self.stepChanged.emit(f'BLACK|    Получаем список приложений l7')
        err, result = self.utm.get_l7_apps()
        if err:
            self.stepChanged.emit(f'iRED|{result}')
            return
        self.ngfw_data['l7_apps'] = {value: key for key, value in result.items()}

        if write_bin_file(self, self.ngfw_data):
            self.stepChanged.emit(f'iRED|Произошла ошибка инициализации импорта! Не удалось сохранить служебные структуры данных.')
        else:
            self.stepChanged.emit(f'GREEN|Служебные структуры данных заполнены.')

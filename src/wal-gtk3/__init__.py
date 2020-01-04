# -*- coding: utf-8 -*-
#
# 	Copyright (C) 2019 by Igor E. Novikov
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .base import Application, PaletteWindow, EntryPopover
from .base import init_clipboard, get_from_clipboard, set_to_clipboard
from .dialogs import color_dialog, properties_dialog
from .dialogs import error_dialog, about_dialog, yesno_dialog
from .dialogs import get_open_file_name, get_save_file_name
from .grab import pick_color, pick_color_zoomed

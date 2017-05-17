# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


column_renames = {
    'product_template': [
        ('auto_create_task', None),
    ],
}


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)

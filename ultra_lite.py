import numpy as np

car_data = np.array([['Nissan', 'juke', 8.5, 1200000],
                     ['Toyota', 'Hilux', 10, 3200000],
                     ['Isuzu', 'Mu-x', 9, 4200000],
                     ])

with open('car_data.txt', 'w') as f:
    num_rows, num_cols = car_data.shape
    for i in range(num_rows):
        for j in range(num_cols):
            f.write(str(car_data[i][j]) + ' ')
        f.write('\n')



import datetime

from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(par_1, par_2): # возвращает словарь аргуменов
    return {
        'param_1': par_1,
        'param_2': par_2,
    }


def from_template(p_1, p_2, template):
    template = DocxTemplate(template)
    context = get_context(p_1, p_2)  # gets the context used to render the document
    template.render(context)
    template.save(p_1 + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(par_1, par_2):
    template = 'tampl_test.docx'
    document = from_template(par_1, par_2, template)


generate_report('Тестовый параметр 1', 'Тестовый параметр 2')

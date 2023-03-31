from docxtpl import DocxTemplate


def work_job_document(number, context, name_file):
    doc = DocxTemplate(f'shablons/shablon{number}.docx')
    doc.render(context)
    path = f'donedocs/Договор №{name_file}.docx'
    doc.save(path)
    return path


def document(number, names, money):
    name_file = f'{number}_{names}'
    context = {
        'full_name': names,
        'money': money
    }
    path = work_job_document(number, context, name_file)
    return path

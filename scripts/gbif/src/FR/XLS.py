from openpyxl import Workbook
import GBIF_XLS


class xlxs(object):
    def __init__(self, archive):
        self.wb = get_wb(archive)

    def get_wb(self, archive):
        wb = []
        wb = load_wordbook(archive)
        ws = wb.active
        target = wb.copy_worksheet(ws)
        return target


    def valida(self):

        gbif = GBIF_XLS.GBIF()
        macro = []
        for cell in row:
            self.wb.cell(row=i,column=1,gbif.ocurrence(self.wb.cell(row=i,column=0)))
        
        self.wb.save('Validado.xlsx')
        print ("Concluido!")



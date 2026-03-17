#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fpdf import FPDF

hualien_foods = [
    {"name": "1. Yixiang Wonton", "type": "Snack", "address": "No.136, Zhongshan Rd, Hualien", "description": "Famous wonton shop, thin skin and juicy filling", "must_try": "Wonton Soup"},
    {"name": "2. Bomb Scallion Pancake", "type": "Snack", "address": "Chongqing Rd & Zhongshan Rd, Hualien", "description": "Crispy pancake with half-boiled egg", "must_try": "Bomb Scallion Pancake"},
    {"name": "3. Gongzheng Steamed Buns", "type": "Snack", "address": "No.14-1, Gongzheng St, Hualien", "description": "24-hour famous steamed bun shop", "must_try": "Pork Buns"},
    {"name": "4. Haipu Oyster Omelette", "type": "Snack", "address": "No.86, Ziyou St, Hualien", "description": "Oldest oyster omelette in Hualien", "must_try": "Oyster Omelette"},
    {"name": "5. Yixin Shaved Ice", "type": "Dessert", "address": "No.27, Jieyue St, Hualien", "description": "Traditional shaved ice with various flavors", "must_try": "Mango Ice"},
    {"name": "6. MiaoKou Curry Rice", "type": "Restaurant", "address": "No.36-6, Fuqian Rd, Hualien", "description": "Japanese curry rice, rich aroma", "must_try": "Curry Rice"},
    {"name": "7. MiTang Thai Food", "type": "Restaurant", "address": "No.78-1, Zhongmei Rd, Hualien", "description": "Authentic Thai cuisine, affordable", "must_try": "Tom Yum Soup"},
    {"name": "8. HeJiaHuan Chinese", "type": "Restaurant", "address": "No.581, Heping Rd, Hualien", "description": "Chinese family-style dishes", "must_try": "Stir-fried Vegetables"},
    {"name": "9. Xinxin Noodle", "type": "Snack", "address": "No.6, Ln.169, Zhongshan Rd, Hualien", "description": "Traditional noodle with braised dishes", "must_try": "Dry Noodles"},
    {"name": "10. Chen's Congee", "type": "Snack", "address": "No.28, Jieyue St, Hualien", "description": "Delicious congee with rich ingredients", "must_try": "Seafood Congee"}
]

class FoodPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(200, 80, 80)
        self.cell(0, 15, 'Hualien Food Guide', 0, 1, 'C')
        self.ln(5)

pdf = FoodPDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Date: 2026-03-17', 0, 1, 'C')
pdf.ln(5)

for f in hualien_foods:
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(0, 100, 200)
    pdf.cell(0, 8, f['name'], 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f'Type: {f["type"]}', 0, 1, 'L')
    pdf.cell(0, 6, f'Address: {f["address"]}', 0, 1, 'L')
    pdf.multi_cell(0, 6, f'Description: {f["description"]}')
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(255, 140, 0)
    pdf.cell(0, 6, f'Must Try: {f["must_try"]}', 0, 1, 'L')
    pdf.ln(5)

pdf.output('Hualien_Food.pdf')
print('OK! PDF created: Hualien_Food.pdf')

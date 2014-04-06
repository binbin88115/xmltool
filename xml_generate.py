# -*- coding: utf-8 -*-
# 该工具用于将excel文件传为xml文件
# 被转换的excel文件需要遵守template.xlsx的标准
# 命令格式：python xml_generate.py excel.xlsx
#			python xml_generate.py ../directory/excel.xls
#			python xml_generate.py directory/excel.xls

from base import *

XML_HEADER 		= '<?xml version="1.0" encoding="utf-8"?>'
XML_TAB			= '  '
XML_LINE_BREAK	= '\r\n'
XML_BLANK		= ''

WRITE_DIRECTORY	= 'xml'

class XMLGenerate(Base):

	_output_xml_tests = {}

	def __init__(self):
		Base.__init__(self)
		self._parse_to_xml()

	def _table_to_xml(self, sheet_name, output_name):
		if sheet_name == TEMPLATE_TABLE_NAME:
			return XML_BLANK

		table = self._try_get_sheet_by_name(sheet_name)
		column_names = table.row_values(TABLE_COLUMN_NAME_ROW_INDEX)
		column_types = table.row_values(TABLE_COLUMN_TYPE_ROW_INDEX)
		
		text = str.format('<{}>{}', output_name, XML_LINE_BREAK)
		for row_index in range(TABLE_OFFSET_ROW_NUM, table.nrows):
			row_text = str.format('{}<{}', XML_TAB, ROW_ELEMENT_NAME)
			for column_index in range(table.ncols):
				cell = table.cell(row_index, column_index)
				cell_value = cell.value
				if cell.ctype == xlrd.book.XL_CELL_NUMBER:
					if column_types[column_index] == COLUMN_INT_TYPE:
						cell_value = int(cell_value)
				row_text += str.format(' {}="{}"', column_names[column_index], cell_value)
			row_text += ' />'
			text += row_text + XML_LINE_BREAK
		text += str.format('</{}>', output_name)
		return text

	def _add_xml_header(self, value):
		return str.format('{}{}{}', XML_HEADER, XML_LINE_BREAK, value)

	def _parse_to_xml(self):
		for row in self._output_config_table:
			output_file_name = row[CONFIG_OUTPUT_FILE_NAME_COLUMN_INDEX]
			output_xml_text = self._output_xml_tests.get(output_file_name)
			if output_xml_text == None:
				output_xml_text = XML_BLANK
			if len(output_xml_text) > 0:
				output_xml_text += XML_LINE_BREAK
			output_xml_text += self._table_to_xml(
				row[CONFIG_SHEET_NAME_COLUMN_INDEX], row[CONFIG_OUTPUT_NAME_COLUMN_INDEX])
			self._output_xml_tests[output_file_name] = output_xml_text

	def _write_xml(self, file_name, text):
		self._write(WRITE_DIRECTORY, file_name, text)

	def exportXML(self):
		for key in self._output_xml_tests.keys():
			value = self._output_xml_tests.get(key)
			if value != None:
				self._write_xml(key, self._add_xml_header(value))

	def printXML(self):
		for key in self._output_xml_tests.keys():
			value = self._output_xml_tests.get(key)
			if value != None:
				value = self._add_xml_header(value)
				self._print_utf8(str.format('{}{}', value, XML_LINE_BREAK))

if __name__ == '__main__':
	xml = XMLGenerate()
	xml.exportXML()
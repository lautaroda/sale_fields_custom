sale_fields_custom

Summary

The sale_fields_custom module adds custom fields to the sales order in Odoo, specifically for laser entries and dimensions.

Description

This module extends the standard sales order form to include additional fields for laser entries, and the dimensions (length, width, height) of items. These fields are added after the payment term field in the sales order form view.

Installation

	1.	Clone or download this repository into your Odoo addons directory.
	2.	Update your Odoo app list by clicking on the “Update Apps List” in the Apps menu.
	3.	Find and install the “sale_fields_custom” module.

Dependencies

This module depends on the sale module.

Configuration

No additional configuration is required for this module.

Usage

Once the module is installed, the following fields will be available in the sales order form:

	•	Número de entradas del láser (laser_entries): This is a character field to specify the number of laser entries.
	•	Longitud (dimension_length): This is a float field to specify the length of the item, including any waste pieces.
	•	Anchura (dimension_width): This is a float field to specify the width of the item, including any waste pieces.
	•	Altura (dimension_height): This is a float field to specify the height of the item, including any waste pieces.

These fields can be filled in during the creation or editing of a sales order.
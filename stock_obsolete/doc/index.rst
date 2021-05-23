==================
Obsolete Inventory
==================

************************************************************************************
May 25th, 2021 - this is a BETA release.  Please send feedback to ray@odoo.com.
************************************************************************************  

This is a "proof of concept" to illustrate how obsolete inventory can be managed.  Products can be marked with a planned obselecence date and documents containing obsolete products - such as transfers, bills of materials and manufacturing orders can be identified so users can enact the obselecence plan for each.

*****
Note:
*****

- This app may require changes before it is suitable to use in a production environment.
- It has only been tested in databases created with a country setting of the United States and may need localization outside the US.
- Discuss your requirements with an Odoo Advisor or Odoo Partner to understand the best way to leverage this functionality.

*************************************
Target Platform, Edition and Version:
*************************************

- Online, Odoo.sh or On-Premise.
- Enterprise Edition.  
- Version 14.0.  

**************
Required Apps:
**************

- Odoo Studio - web_studio
- Manufacturing - mrp
- Inventory - stock

*************************
Summary of Functionality:
*************************

Users can now 

- manage obsolete products (including planning for future obselecence dates); 

- proactively find Inventory Transfers / Bills of Materials / Manufacturing Orders that still reference obsolete products;

- reactively use Warnings and visual cues to discover Inventory Transfers / Bills of Materials / Manufacturing Orders that still reference obsolete products.

***********
Installing:
***********

1. Download the ZIP, do not unzip it.

2. From the Apps Switcher screen, toggle open Odoo Studio:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/odoo_studio_button.png

3. From the Customizations Menu on the left, select Import.

4. Upload the ZIP file and click IMPORT.

******
Setup:
******

None required


************************
User Experience Changes:
************************
	
.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - 
     - 
   * - Fields to manage obselecence are added to the Product Form View: 
     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/product_fields.png

   * - A Warning is shown at the top of all Products that are (or will become) Obsolete:
     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/product_warning.png 

   * - A Smart Button is added to the Product Form View, providing quick access to Open Inventory Transfers referencing the Product:
     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/product_smart_button.png


   * - An icon is added to the Product List View, providing a visual cue for all Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/product_list_view.png

   * - A Filter is added to the Product Search View, providing quick access to all Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/product_filter.png

   * - An Warning and Icon are added to the Inventory Transfer Form View, providing visual cues about Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/stock_picking_form.png

   * - An icon is added to the Inventory Transfer List View, providing a visual cue for all Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/stock_picking_list.png

   * - A Filter is added to the Transfer Search View, providing quick access to all Transfers referencing Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/stock_picking_search.png


   * - An Warning and Icon are added to the Bill of Materials Form View, providing visual cues about Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/bom_form.png

   * - A Smart Button is added to the Bill of Materials Form View, providing quick access to Open Manufacturing Orders referencing the Product:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/bom_smart.png

   * - An icon is added to the Bill of Materials List View, providing a visual cue for all Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/bom_list.png

   * - A Filter is added to the Bill of Materials Search View, providing quick access to any BoM's referencing Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/bom_search.png

   * - An Warning and Icon are added to the Manufacturing Order Form View, providing visual cues about Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/order_form.png

   * - An icon is added to the Manufacturing Orders List View, providing a visual cue for all Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/order_list.png

   * - A Filter is added to the Manufacturing Orders Search View, providing quick access to any MO's referencing Obsolete Products:

     - .. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/stock_obsolete/doc/order_search.png


	

*******************
Functional Changes:
*******************

None

************
Walkthrough:
************

The following example requires the demo data installed.

- TDB 

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/14.0/mrp_services/doc/service_product.png













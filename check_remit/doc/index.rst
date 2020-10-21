====================
Check Remit To (USA)
====================

Note:

- Note that this app may require changes for your particular organization.  
- It has only been tested in databases created with the Country setting of the United States and may need to be localized for other countries. 
- Discuss your requirements with your Odoo Advisor or an Odoo Partner to understand the best way to leverage this kind of functionality.

Target Platform, Edition and Version:

- Online, Odoo.sh or On-Premise.
- Enterprise Edition.  
- Version 13.0.  

Required Apps:

- Odoo Studio - web_studio
- Invoicing - account
- US Checks Layout - l10n_us_check_printing

Installing:

1. Download the ZIP, do not unzip it

2. From the Apps Switcher screen, activate Odoo Studio:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/check_remit/doc/odoo_studio_button.png

3. From the Customizations Menu on the left, select Import

4. Upload the ZIP file and click IMPORT

Setup:

No specific setup is needed, but you may want to review the address formatting if you have limited space on your checks and find that you need to consolidate the "street" and "street2" field and/or remove the "country_id" field from the check.  

To do this, activate Developer Mode and then open the country "United States" from the "Contacts --> Configuration --> Localization --> Countries" Menu sequence

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/check_remit/doc/layout.png

You can remove the line that adds "country_name", or even show "street" and "street2" on one line to have addresses shown in two or three lines instead of four.

This is a global setting that affects all places Odoo displays address information.

Use:

On a Customer, you will see a new field where you can store the Remit To Contact and/or Department:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/check_remit/doc/new_field.png

When printing a check, a payment like this:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/check_remit/doc/payment.png

Will print out like this:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/check_remit/doc/check.png

========================
Manufacturing Timesheets
========================

Target Platform, Edition and Version:

- Online, Odoo.sh or On-Premise.
- Enterprise Edition.  
- Version 13.0.  

Required Apps:

- Odoo Studio - web_studio
- Manufacturing - mrp
- Task Logs - hr_timesheet

Installing:

1. Download the ZIP, do not unzip it

2. From the Apps Switcher screen, activate Odoo Studio:

.. image:: odoo_studio_button.png

3. From the Customizations Menu on the left, select Import

4. Upload the ZIP file and click IMPORT

Setup:

From the Accounting --> Configuration --> Settings Menu, check on Analytic Accounting

Use:

On a Manufacturing Order, you will see a new Timesheets Tab.

On the Analytic Entries Menu, you will see a new Filter "To be Converted" and a new Action "Create Manufacturing Journal Entry"

Periodically, select records that have not yet been converted and convert them.  We recommend doing this AT LEAST once a month, and convert all entries in the same month they are created.

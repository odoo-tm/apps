========================
Manufacturing Timesheets
========================

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
- Manufacturing - mrp
- Task Logs - hr_timesheet

Installing:

1. Download the ZIP, do not unzip it

2. From the Apps Switcher screen, activate Odoo Studio:

.. image:: https://raw.githubusercontent.com/odoo-tm/apps/13.0/mrp_timesheets/doc/odoo_studio_button.png

3. From the Customizations Menu on the left, select Import

4. Upload the ZIP file and click IMPORT

Setup:

From the Accounting --> Configuration --> Settings Menu, check on Analytic Accounting

From your Chart of Accounts, mark one account as "Cost Allocation" and one account as "Labor Expense/Accrual" by checking the relevant box.  You can only have ONE of each kind of account.

"Cost Allocation" - this is the account that the financial cost of Labor will be DEBITED to (to increase it).  You can move this amount to COGS when you sell something.  This should be an asset account, probably shown on your Chart with Inventory.

"Labor Expense/Accrual" - this is the account that the financial cost of Labor will be CREDITED to (to decrease it if it is an expense account or increase it if it is a liability account).  This should be an expense account (if you expense labor as it is performed) or a liability account (if you accrue labor hours between the times where you run payroll). 

Note: You should review with your bookkeeper or accountant which Cost Allocation account and which Labor method is compatible with the way you record your financial records.

From the Employees App, enter a Timesheet Cost per hour for each Employee that will log time on Manufacturing Orders.

Use:

On a Manufacturing Order, you will see a new Timesheets Tab.

On the Analytic Entries Menu, you will see a new Filter "To be Converted" and a new Action "Create Manufacturing Journal Entry"

Periodically, select records that have not yet been converted and convert them.  We recommend doing this AT LEAST once a month, and convert all entries in the same month they are created.

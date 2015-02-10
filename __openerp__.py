{
    'name': "Employee birthday and entry date scheduler",
    'version': '1.0',
    'depends': ['hr','hr_improvements'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Human Resources',
    'description': "This module creates a scheduler that will run every day a method that looks for birthdays or entry date anniversary (at AbAKUS) of employees.
This method works if there are several employees who have their birthday on the same day. When a match is found, a message is generated and sent by email to employees specified as managers.

The email is sent using a Python library. Employee data are retrieved with the Odoo ORM (API).
This module requires the 'hr' and 'hr_improvements' module. 'hr_improvements' is a module developed by Abakus that adds, among others, the entry date in the company.

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
",
    'data': ['hr_scheduler.xml',],
    'demo': [],
}
